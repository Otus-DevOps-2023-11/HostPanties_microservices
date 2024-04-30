provider "yandex" {
  service_account_key_file = file(var.service_account_key_file)
  cloud_id                 = var.cloud_id
  folder_id                = var.folder_id
  zone                     = var.zone
}

resource "yandex_compute_instance" "monolith" {
  for_each    = toset( [for num in range(var.monolith_number): tostring(num) ])
  name        = "docker-monolith-${each.key}"
  platform_id = "standard-v1"
  zone        = var.zone
  
  labels = {
    tags = "monolith"
    env = "docker"
  }

  resources {
    cores   = 2
    memory  = 4
  }

  boot_disk {
    disk_id = yandex_compute_disk.monolith_disk[each.key].id
  }

  network_interface {
    subnet_id = var.subnet_id
    nat = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file(var.public_key_path)}"
  }
}

resource "yandex_compute_disk" "monolith_disk" {
  for_each    = toset( [for num in range(var.monolith_number): tostring(num) ])
  
  name      = "monolith-${each.key}-disk"
  image_id  = "${var.image_id}"
  zone      = "${var.zone}"
}
