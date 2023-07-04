terraform {
  required_version = ">= 1.1.0"
}

provider "aws" {
  region = var.region

  access_key = var.aws_access_key
  secret_key = var.aws_secret_key

  # other options for authentication
}