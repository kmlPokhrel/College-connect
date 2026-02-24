# 🎓 College Connect  
### A Networking Hub for Students Powered by Streamlit & Firebase

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg"/>
  <img src="https://img.shields.io/badge/streamlit-WebApp-red"/>
  <img src="https://img.shields.io/badge/firebase-Firestore-orange"/>
  <img src="https://img.shields.io/badge/auth-Google%20OAuth-green"/>
  <img src="https://img.shields.io/badge/status-Active-brightgreen"/>
</p>

---

## 📌 Overview

**College Connect** is a student networking web application designed to help students within a college discover and connect with each other based on:

- 🎓 Branch
- 🧠 Skills
- 📄 Bio

The platform features secure **Google Authentication** and real-time cloud storage using **Firebase Firestore**.

> Built as a practical implementation of authentication, cloud databases, and interactive web applications.

---

## ✨ Features

- 🔐 **Secure Login**
  - Google OAuth 2.0 integration
  - Only authenticated users can access the platform

- 👤 **Student Profiles**
  - Name
  - Branch
  - Skills
  - Bio

- 🔍 **Searchable Student Directory**
  - Real-time filtering
  - Skill-based discovery

- ☁️ **Cloud Powered**
  - Data stored securely in Firebase Firestore
  - Real-time updates

---

## 🏗️ Application Flow

```
User Login (Google OAuth)
        │
        ▼
Authentication Verification
        │
        ▼
Profile Creation / Update
        │
        ▼
Data Stored in Firebase Firestore
        │
        ▼
Search & Discover Students
```

---

## 🛠️ Tech Stack

- **Frontend / UI:** Streamlit  
- **Backend:** Python  
- **Database:** Google Firebase Firestore  
- **Authentication:** Google Cloud OAuth 2.0  
- **Data Handling:** Pandas  

---

## 🚀 Setup Instructions

### 1️⃣ Prerequisites

Ensure Python 3.11+ is installed.

Install required libraries:

```bash
pip install streamlit firebase-admin google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas
```

---

### 2️⃣ Secret Keys (Required for Local Run)

For security reasons, configuration files are **NOT included** in this repository.

You must configure:

#### 🔹 Google Cloud Setup

1. Create a new project
2. Enable **Google People API**
3. Configure OAuth Consent Screen
4. Create OAuth Credentials
5. Download:
   ```
   client_secret.json
   ```

---

#### 🔹 Firebase Setup

1. Create a Firebase project
2. Enable Firestore Database
3. Go to:
   ```
   Project Settings → Service Accounts
   ```
4. Generate new private key
5. Download and rename it to:
   ```
   serviceAccountKey.json
   ```

---

### 3️⃣ File Placement

Place both files in the root directory:

```
College-Connect/
│
├── main_app.py
├── client_secret.json
├── serviceAccountKey.json
└── README.md
```

---

### 4️⃣ Run the Application

Open terminal inside the project folder:

```bash
streamlit run main_app.py
```

Your application will launch in the browser automatically.

---

## 📂 Project Structure

```
College-Connect/
│
├── main_app.py
├── client_secret.json        (Not included in repo)
├── serviceAccountKey.json    (Not included in repo)
└── README.md
```

---

## 🔐 Security Note

Sensitive credentials such as:

- `client_secret.json`
- `serviceAccountKey.json`

are intentionally excluded from version control.

If deploying, ensure these files are securely managed using environment variables or a secure secrets manager.

---

## 🌱 Future Improvements

- 📱 Mobile-responsive UI improvements
- 💬 Direct messaging feature
- 📸 Profile picture upload
- 🏫 Multi-college support
- 🛡️ Admin dashboard for moderation
- 🚀 Deployment on Streamlit Cloud

---

## 📜 License

This project is developed for educational purposes as part of a college assignment.

---

<p align="center">
Built with ❤️ to strengthen student collaboration.
</p>
