# 🛡️ URL Safety Checker

A lightweight cybersecurity tool built with **Python** and **Streamlit** that analyzes URLs for common phishing indicators and generates a risk score with security recommendations.

---

## 📌 Overview

URL Safety Checker helps users determine whether a URL appears suspicious by performing multiple rule-based security checks. The application evaluates phishing-related patterns such as IP-based URLs, missing HTTPS, excessive subdomains, suspicious keywords, and more.

Based on these checks, the system calculates a **Risk Score (0–100)** and classifies the URL as **Low Risk**, **Medium Risk**, or **High Risk**.

---

## 🚀 Features

- Analyze URLs for phishing indicators
- Generate a Risk Score (0–100)
- Detect suspicious URL patterns
- Display detected security issues
- Provide safety recommendations
- Simple and user-friendly Streamlit interface
- Real-time URL analysis

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **urllib.parse**
- **tldextract**
- **Regular Expressions (Regex)**

---

## 📂 Project Structure

```text
URL-Safety-Checker/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

```text
User Enters URL
        │
        ▼
URL Parsing
        │
        ▼
Security Rule Checks
        │
        ▼
Risk Score Calculation
        │
        ▼
Issue Detection
        │
        ▼
Risk Classification
        │
        ▼
Recommendation
```

---

## 🔍 Security Checks Performed

### 1. IP Address Detection

Checks whether the URL uses a direct IP address instead of a domain name.

**Example**

```text
http://192.168.1.1/login
```

**Risk Added:** +30

---

### 2. HTTPS Verification

Checks whether the URL uses secure HTTPS encryption.

**Example**

```text
http://example.com
```

**Risk Added:** +20

---

### 3. Long URL Detection

Detects unusually long URLs often used to hide malicious content.

**Condition**

```text
URL Length > 75 Characters
```

**Risk Added:** +15

---

### 4. @ Symbol Detection

Detects the presence of the '@' symbol, which is commonly used in phishing attacks.

**Example**

```text
http://trusted.com@fake-site.com
```

**Risk Added:** +25

---

### 5. Excessive Hyphen Detection

Checks for domains containing multiple hyphens.

**Example**

```text
secure-bank-login-update.com
```

**Risk Added:** +20

---

### 6. Multiple Subdomains Detection

Detects URLs with an unusually high number of subdomains.

**Example**

```text
login.verify.account.bank.example.com
```

**Risk Added:** +15

---

### 7. Suspicious Keyword Detection

Searches for phishing-related keywords such as:

```text
login
verify
update
secure
bank
account
free
gift
winner
```

**Risk Added:** +5 per keyword

---

## 📊 Risk Classification

| Risk Score | Classification |
|------------|---------------|
| 0 – 20 | 🟢 Low Risk |
| 21 – 50 | 🟡 Medium Risk |
| 51 – 100 | 🔴 High Risk |

---

## 💻 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/url-safety-checker.git
```

```bash
cd url-safety-checker
```

### Install Dependencies

```bash
pip install streamlit tldextract
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📷 Example

### Input

```text
http://secure-bank-login-update.com
```

### Output

```text
Risk Level : High Risk

Risk Score : 65/100

Detected Issues:
• Not using HTTPS
• Suspicious Keyword: secure
• Suspicious Keyword: bank
• Suspicious Keyword: login
• Suspicious Keyword: update

Recommendation:
Avoid opening this URL.
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- URL Parsing and Analysis
- Rule-Based Phishing Detection
- Cybersecurity Risk Assessment
- Streamlit Web Application Development
- Python Security Programming
- Risk Scoring Systems

---

## 🔮 Future Enhancements

- Machine Learning-Based Phishing Detection
- WHOIS Lookup Integration
- Domain Age Analysis
- Blacklist Verification
- VirusTotal API Integration
- URL Reputation Scoring
- Browser Extension Support
- Real-Time Threat Intelligence

---

## 👨‍💻 Author

**Advik Saxena**

B.Tech Computer Engineering (CSE)  
Fr. Conceicao Rodrigues Institute of Technology (FCRIT), Navi Mumbai

---

## ⭐ Project Description

Developed a Streamlit-based cybersecurity application that analyzes URLs using rule-based phishing detection techniques and generates risk scores with actionable security recommendations.
