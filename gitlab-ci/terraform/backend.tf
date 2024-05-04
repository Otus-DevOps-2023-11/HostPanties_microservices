terraform {
  backend "s3" {
    endpoints = {
      s3 = "https://storage.yandexcloud.net"
    }
    bucket = "hostpanties-otus-tfstate"
    region = "ru-central1-b"
    key    = "otus/gitlab-ci/terraform.tfstate"

    skip_region_validation      = true
    skip_credentials_validation = true
    skip_requesting_account_id  = true
    skip_s3_checksum            = true

    access_key = "YCAJEK_S-y_ldauR0Ch_pgUgY"
    secret_key = "YCOTLvCltGSV9cQoYJZfUqxH_E4-GuFxPdGU4S8-"
  }
}
