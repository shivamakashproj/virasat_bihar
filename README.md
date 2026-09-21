# 🏛️ Virasat Bihar

<div align="center">

### Experience the Royal Heritage of Bihar — A Digital Journey Through Ancient and Majestic Lands

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Responsive](https://img.shields.io/badge/Responsive-Design-4CAF50?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

**🔗 Live Site:** [shivamakashproj.github.io/virasat_bihar](https://shivamakashproj.github.io/virasat_bihar/)

</div>

---

## 🎯 Objective

**Virasat Bihar** is a web application built to showcase the cultural, historical, and spiritual heritage of Bihar. Acting as a digital "Royal Emissary," it guides tourists and history enthusiasts through all 38 districts — delivering travel information, historical context, and immersive image galleries in a responsive, visually striking format. The app is also containerized and deployed on AWS with a full CI/CD pipeline, making it a complete front-end-to-cloud project.

## ⚠️ The Problem

Bihar is the birthplace of Buddhism and Jainism, home to the world's oldest university (Nalanda), and the seat of ancient empires like Magadha — yet its tourism potential remains vastly underrepresented online. Existing regional tourism sites lack a cohesive heritage aesthetic or are difficult to navigate.

**Virasat Bihar** solves this with a clean, distraction-free, immersive experience — built on a scalable, containerized architecture that needs no backend database for content management and deploys automatically on every code change.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| 🗺️ **Comprehensive Coverage** | Dedicated detail pages for all 38 districts of Bihar |
| 🖼️ **Dynamic Image Galleries** | Automated JavaScript gallery system, builds grids seamlessly |
| 📱 **Fully Responsive** | Flawless scaling across Desktop, Tablet, and Mobile |
| 🎨 **Heritage Aesthetic** | Elegant fonts (*Cinzel*, *Playfair Display*), Chhath Puja–themed visuals, royal creamy-brown palette |
| 📞 **Direct Admin Contact** | One-tap links for WhatsApp, Email, and Phone inquiries |
| 🐳 **Containerized** | Packaged with Docker + Nginx for reproducible, portable deployment |
| ☁️ **Cloud Hosted** | Deployed on AWS EC2, provisioned via Terraform (Infrastructure as Code) |
| 🔁 **CI/CD Automated** | GitHub Actions builds and pushes Docker images, then auto-deploys to EC2 on every push |

---

## 🏗️ Architecture & Deployment Stack

```
Developer Push (git push)
        │
        ▼
GitHub Actions (CI)
        │  build Docker image
        │  push to Docker Hub (tagged latest)
        ▼
GitHub Actions (CD)
        │  SSH into AWS EC2
        │  pull latest image
        │  recreate running container
        ▼
AWS EC2 (Ubuntu) + Nginx
        │  serves static site over HTTP
        ▼
        End User
```

- **Docker** — static site containerized with Nginx as the web server; images published to Docker Hub.
- **Terraform** — provisions AWS infrastructure as code: EC2 instance, Security Groups (HTTP/SSH access), and EC2 User Data to auto-install Docker and run the initial container on first boot.
- **GitHub Actions** — CI builds and pushes the Docker image on every push to `main`; CD then SSHes into EC2 to pull the latest image and recreate the container — zero manual deployment steps.
- **Secrets Management** — Docker Hub PAT and EC2 SSH credentials stored securely as GitHub Actions Secrets, never committed to the repo.

---

## 🛠️ Admin Guide: Managing Content

No coding knowledge required to update images.

### 1. Updating Destination Galleries
- Inside `assets/`, find each district's subfolder (e.g. `assets/patna/`, `assets/rajgir/`)
- Save images as `.jpg` or `.png`
- Name them sequentially: `1.jpg`, `2.jpg`, `3.jpg`, …
- Drop them into the matching district folder

The site's JavaScript auto-detects and renders them in the gallery grid.

### 2. Updating Contact Information
1. Open any HTML file (e.g. `index.html`) in a code editor
2. Scroll to `<section class="inquiry-footer">`
3. Update:
   - WhatsApp: `href="https://wa.me/..."`
   - Phone: `href="tel:..."`
   - Email: `href="mailto:..."`

### 3. Redeploying After Changes
Just `git push` to `main` — GitHub Actions handles the rest: build → push to Docker Hub → pull on EC2 → container recreated with the update live.

---

## 🔮 Roadmap

- [ ] **Interactive Web Map** — clickable SVG map of Bihar for geographic district selection
- [ ] **Multi-language Support** — Hindi, Bhojpuri, Maithili translations
- [ ] **Backend / CMS Integration** — migrate to Node.js/MongoDB or Firebase for admin-uploaded content
- [ ] **360° Virtual Tours** — panoramic views of Golghar, Bodhi Tree, Nalanda Ruins
- [ ] **Booking API Integration** — direct booking with local guides, transport, and hotels
- [ ] **HTTPS / Load Balancing** — add an AWS Application Load Balancer + ACM certificate for secure, scalable traffic

---

<div align="center">
<i>Made with ❤️ to celebrate the golden heritage of Bihar.</i>
</div>
