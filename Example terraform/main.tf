resource "tls_private_key" "example_ssh" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "local_file" "private_key" {
  content         = tls_private_key.example_ssh.private_key_pem
  filename        = "${path.module}/example-key.pem"
  file_permission = "0600"
}

resource "local_file" "public_key" {
  content  = tls_private_key.example_ssh.public_key_openssh
  filename = "${path.module}/example-key.pub"
}

resource "google_compute_instance" "frontend" {
  name         = var.instance_name
  machine_type = "e2-small"
  zone         = "us-central1-c"

  boot_disk {
    initialize_params {
      image = "ubuntu-2004-focal-v20240307b"
    }
  }

  network_interface {
    network       = "default"
    access_config {}
  }

  metadata = {
    ssh-keys = "brandonromero1964:${tls_private_key.example_ssh.public_key_openssh}"
  }

  provisioner "remote-exec" {
    connection {
      type        = "ssh"
      user        = "brandonromero1964"
      private_key = tls_private_key.example_ssh.private_key_pem
      host        = self.network_interface[0].access_config[0].nat_ip //ip publica de forma automatica
    }

  inline = [
    "sudo apt-get update",
    "sudo apt-get install -y software-properties-common",
    "sudo add-apt-repository --yes --update ppa:ansible/ansible",
    "sudo apt-get install -y ansible",
    "sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common",
    "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
    "sudo add-apt-repository \"deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\"",
    "sudo apt-get update",
    "sudo apt-get install -y docker-ce docker-ce-cli containerd.io",
  ]
  }

  # Agregar el file provisioner para copiar la carpeta local al destino remoto
  provisioner "file" {
    source      = "C:/Users/Mauricio/Desktop/Segundo Semestre 2024/Análisis y Diseño de Sistemas 2/9. Ejemplos practicos/Example terraform/ansible"
    destination = "/home/brandonromero1964/ansible"

    connection {
      type        = "ssh"
      user        = "brandonromero1964"
      private_key = tls_private_key.example_ssh.private_key_pem
      host        = self.network_interface[0].access_config[0].nat_ip
    }
  }

    provisioner "remote-exec" {
    connection {
      type        = "ssh"
      user        = "brandonromero1964"
      private_key = tls_private_key.example_ssh.private_key_pem
      host        = self.network_interface[0].access_config[0].nat_ip
    }

    inline = [
      "ansible-playbook /home/brandonromero1964/ansible/playbook.yml"
    ]
  }
}

resource "google_compute_firewall" "allow_http" {
  name    = "allow-http"
  network = "default"  # Cambia esto si tu red tiene otro nombre

  allow {
    protocol = "tcp"
    ports    = ["3000"]
  }

  source_ranges = ["0.0.0.0/0"]  # Permitir acceso desde cualquier IP
}