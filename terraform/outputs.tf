output "instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.virasat.id
}

output "public_ip" {
  description = "EC2 public IP"
  value       = aws_instance.virasat.public_ip
}

output "public_dns" {
  description = "EC2 public DNS"
  value       = aws_instance.virasat.public_dns
}

output "website_url" {
  description = "Website URL"
  value       = "http://${aws_instance.virasat.public_ip}"
}