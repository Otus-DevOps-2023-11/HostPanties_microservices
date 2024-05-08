provider "yandex" {
  service_account_key_file = file(var.service_account_key_file)
  cloud_id                 = var.cloud_id
  folder_id                = var.folder_id
  zone                     = var.zone
}

resource "yandex_compute_instance" "docker-host" {

  name        = "docker-host"
  platform_id = "standard-v1"
  zone        = var.zone

  labels = {
    tags = "docker-host"
  }
  resources {
    cores   = 2
    memory  = 2
  }

  boot_disk {
    initialize_params {
      image_id = yandex_compute_image.docker-host_disk.id
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

resource "yandex_compute_image" "docker-host_disk" {
  name   = "docker-host-disk"
  source_family = "debian-11-oslogin"
}
