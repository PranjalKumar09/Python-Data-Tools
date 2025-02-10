# Python Data Tools  

![Python Data Tools](static/image.png)  

A collection of Python scripts for automation, data processing, and utility tasks. This repository includes tools for file handling, encryption, API integration, media conversion, and more. Additionally, it contains Docker and Kubernetes deployment configurations.  

## 📌 Features  

- **Automation & Notifications**  
  - `break_notifier.py` – Notifies users to take breaks  
  - `InstagramBot.py` – Automates Instagram interactions  
  - `Mass_Email.py` – Sends bulk emails using SMTP  

- **File Processing & Encryption**  
  - `merge_pdf.py`, `split_pdf.py`, `MergeAllPdf.py`, `Roate_pdf.py` – PDF merging, splitting, and rotation  
  - `encrpt_pdf.py` – Encrypts PDF files  
  - `convert_to_ascii_image.py` – Converts images to ASCII art  
  - `QR_Generator.py`, `QR_Generator2.py` – Generates QR codes  

- **Media Tools**  
  - `mergeVideo.py` – Merges multiple videos  
  - `video_to_gif.py` – Converts videos to GIFs  
  - `Video_to_audio.py` – Extracts audio from videos  
  - `Screen_recoder.py` – Screen recording tool  

- **APIs & Networking**  
  - `news_api.py` – Fetches news articles from an API  
  - `playlist.py` – Manages music playlists  
  - `send Email (smtplib).py` – Sends emails using Python’s `smtplib`  
  - `email_validationUsingRegEx.py` – Validates email addresses using regex  

- **Miscellaneous**  
  - `encoding_decoding.py` – Encodes and decodes data  
  - `textedditor.py` – A simple text editor  

## 📦 Setup & Installation  

1. **Clone the repository**  
   ```sh
   git clone https://github.com/PranjalKumar09/Python-Data-Tools.git  
   cd Python-Data-Tools  
   ```  

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt  
   ```  

3. **Run any script**  
   ```sh
   python src/news_api.py  
   ```  

## 🐳 Docker Setup  

You can run the tools inside a Docker container:  

```sh
docker build -t python-data-tools .  
docker run -it python-data-tools  
```  

## ☸️ Kubernetes Deployment  

To deploy using Kubernetes, apply the provided YAML files:  

```sh
kubectl apply -f k8s-deployement.yaml  
kubectl apply -f k8s-service.yaml  
```  

## 📜 License  

This project is licensed under the [License](LICENSE).  

## 🔗 Connect  

- GitHub: [Python Data Tools](https://github.com/PranjalKumar09/Python-Data-Tools)  

---
