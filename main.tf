terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  backend "s3" {
    bucket       = "emmanuelgana-tf-state"
    key          = "phase1/terraform.tfstate"
    region       = "us-east-1"
    profile      = "lab"
    use_lockfile = true
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "lab"
}