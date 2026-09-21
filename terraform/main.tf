terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# -------------------------
# Default VPC
# -------------------------

data "aws_vpc" "default" {
  default = true
}

# -------------------------
# Default subnet
# -------------------------

data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# -------------------------
# Ubuntu 24.04 LTS AMI
# -------------------------

data "aws_ami" "ubuntu" {
  most_recent = true

  owners = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# -------------------------
# Existing EC2 Key Pair
# -------------------------

data "aws_key_pair" "virasat" {
  key_name = var.key_name
}

# -------------------------
# Security Group
# -------------------------

resource "aws_security_group" "virasat" {
  name        = "${var.project_name}-sg"
  description = "Security group for Virasat Bihar"
  vpc_id      = data.aws_vpc.default.id

  # SSH
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTP
  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-sg"
  }
}

# -------------------------
# EC2
# -------------------------

resource "aws_instance" "virasat" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  subnet_id = data.aws_subnets.default.ids[0]

  key_name = data.aws_key_pair.virasat.key_name

  vpc_security_group_ids = [
    aws_security_group.virasat.id
  ]

  user_data = file("${path.module}/user_data.sh")

  root_block_device {
    volume_size = 8
    volume_type = "gp3"
  }

  tags = {
    Name = var.project_name
  }
}