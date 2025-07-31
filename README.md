To set up CI/CD for auto-deployment from GitHub to an Ubuntu server, you can use GitHub Actions with SSH to deploy your code every time you push to a branch (e.g., main). Here's a full setup:

✅ Requirements
Ubuntu server (with SSH access)

GitHub repository

UFW allowed for SSH and your app port (e.g., 22 and 8000)

A FastAPI app or any backend project set up on the Ubuntu server

🧩 Step-by-Step CI/CD with GitHub Actions
🔐 1. Generate SSH Keys (on local machine or GitHub runner)
bash
Copy
Edit
ssh-keygen -t rsa -b 4096 -C "deploy-key"
# Save as: deploy-key (private) and deploy-key.pub (public)
🛠️ 2. Set Up Ubuntu Server
Add public key to authorized_keys:

bash
Copy
Edit
nano ~/.ssh/authorized_keys
# Paste content of deploy-key.pub here
Ensure permissions:

bash
Copy
Edit
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
🔒 3. Add Secrets to GitHub Repository
Go to GitHub repo → Settings → Secrets → Actions and add:

SSH_HOST: your.server.ip or domain

SSH_USER: e.g., ubuntu or your_user

SSH_KEY: content of deploy-key (private key)

📂 4. Create .github/workflows/deploy.yml
yaml
Copy
Edit
name: 🚀 Deploy to Ubuntu Server

on:
  push:
    branches:
      - main

jobs:
  deploy:
    name: 🔄 Deploy via SSH
    runs-on: ubuntu-latest

    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v3

      - name: 📂 Deploy over SSH
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.SSH_HOST }}
          username: ${{ secrets.SSH_USER }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /home/your_user/your_project_dir
            git pull origin main
            source venv/bin/activate
            pip install -r requirements.txt
            sudo systemctl restart your-app.service
🧪 5. Create systemd Service on Ubuntu
bash
Copy
Edit
sudo nano /etc/systemd/system/your-app.service
Example:

ini
Copy
Edit
[Unit]
Description=FastAPI App
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user/your_project_dir
ExecStart=/home/your_user/your_project_dir/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
bash
Copy
Edit
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable your-app
sudo systemctl start your-app
✅ Done! Now Every Push to main Will:
SSH into your server

Pull the latest code

Install dependencies

Restart your app

To set up CI/CD for auto-deployment from GitHub to an Ubuntu server, you can use GitHub Actions with SSH to deploy your code every time you push to a branch (e.g., main). Here's a full setup:

✅ Requirements
Ubuntu server (with SSH access)

GitHub repository

UFW allowed for SSH and your app port (e.g., 22 and 8000)

A FastAPI app or any backend project set up on the Ubuntu server

🧩 Step-by-Step CI/CD with GitHub Actions
🔐 1. Generate SSH Keys (on local machine or GitHub runner)
bash
Copy
Edit
ssh-keygen -t rsa -b 4096 -C "deploy-key"
# Save as: deploy-key (private) and deploy-key.pub (public)
🛠️ 2. Set Up Ubuntu Server
Add public key to authorized_keys:

bash
Copy
Edit
nano ~/.ssh/authorized_keys
# Paste content of deploy-key.pub here
Ensure permissions:

bash
Copy
Edit
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
🔒 3. Add Secrets to GitHub Repository
Go to GitHub repo → Settings → Secrets → Actions and add:

SSH_HOST: your.server.ip or domain

SSH_USER: e.g., ubuntu or your_user

SSH_KEY: content of deploy-key (private key)

📂 4. Create .github/workflows/deploy.yml
yaml
Copy
Edit
name: 🚀 Deploy to Ubuntu Server

on:
  push:
    branches:
      - main

jobs:
  deploy:
    name: 🔄 Deploy via SSH
    runs-on: ubuntu-latest

    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v3

      - name: 📂 Deploy over SSH
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.SSH_HOST }}
          username: ${{ secrets.SSH_USER }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /home/your_user/your_project_dir
            git pull origin main
            source venv/bin/activate
            pip install -r requirements.txt
            sudo systemctl restart your-app.service
🧪 5. Create systemd Service on Ubuntu
bash
Copy
Edit
sudo nano /etc/systemd/system/your-app.service
Example:

ini
Copy
Edit
[Unit]
Description=FastAPI App
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user/your_project_dir
ExecStart=/home/your_user/your_project_dir/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
bash
Copy
Edit
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable your-app
sudo systemctl start your-app
✅ Done! Now Every Push to main Will:
SSH into your server

Pull the latest code

Install dependencies

Restart your app

