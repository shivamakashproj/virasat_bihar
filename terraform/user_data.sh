#!/bin/bash

set -e

apt-get update

apt-get install -y docker.io

systemctl enable docker
systemctl start docker

docker pull shivam804453/virasat-bihar:latest

docker rm -f virasat-bihar || true

sudo docker run -d --name virasat-bihar --restart unless-stopped -p 80:80 shivam804453/virasat-bihar:latest
