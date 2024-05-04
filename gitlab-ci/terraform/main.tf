provider "yandex" {
  service_account_key_file = file(var.service_account_key_file)
  cloud_id                 = var.cloud_id
  folder_id                = var.folder_id
  zone                     = var.zone
}

resource "yandex_compute_instance" "gitlab" {

  name        = "gitlab"
  platform_id = "standard-v1"
  zone        = var.zone

  labels = {
    tags = "gitlab"
  }
  resources {
    cores   = 4
    memory  = 8
  }

  boot_disk {
    initialize_params {
      image_id = yandex_compute_image.gitlab_disk.id
      size = 50
    }
  }

  network_interface {
    subnet_id = var.subnet_id
    nat = true
  }

  metadata = {
    ssh-keys = "debian:${file(var.public_key_path)}"
  }
}

resource "yandex_compute_image" "gitlab_disk" {
  name   = "gitlab-disk"
  source_family = "debian-11-oslogin"
}
