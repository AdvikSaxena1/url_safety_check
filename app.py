import streamlit as st
from urllib.parse import urlparse
import tldextract
import re

st.set_page_config(
    page_title="URL Safety Checker",
    page_icon="🛡️",
    layout="centered"
)

# -------------------------
# Risk Analysis Function
# -------------------------

def analyze_url(url):

    score = 0
    reasons = []

    parsed = urlparse(url)

    domain = parsed.netloc

    extracted = tldextract.extract(url)

    # IP Address Check
    if re.match(r'^\d+\.\d+\.\d+\.\d+$', domain):
        score += 30
        reasons.append("Uses IP Address")

    # HTTPS Check
    if not url.startswith("https://"):
        score += 20
        reasons.append("Not using HTTPS")

    # Long URL Check
    if len(url) > 75:
        score += 15
        reasons.append("Very Long URL")

    # @ Symbol
    if "@" in url:
        score += 25
        reasons.append("Contains @ Symbol")

    # Multiple Hyphens
    if domain.count("-") >= 2:
        score += 20
        reasons.append("Too Many Hyphens")

    # Too Many Subdomains
    if len(extracted.subdomain.split(".")) > 2:
        score += 15
        reasons.append("Too Many Subdomains")

    # Suspicious Words
    suspicious_words = [
        "login",
        "verify",
        "update",
        "secure",
        "bank",
        "account",
        "free",
        "gift",
        "winner"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 5
            reasons.append(f"Suspicious Keyword: {word}")

    if score > 100:
        score = 100

    return score, reasons


# -------------------------
# UI
# -------------------------

st.title("🛡️ URL Safety Checker")

st.write(
    "Check whether a URL looks suspicious using rule-based phishing detection."
)

url = st.text_input(
    "Enter URL",
    placeholder="https://example.com"
)

if st.button("Analyze URL"):

    if not url:
        st.warning("Enter a URL")
    else:

        score, reasons = analyze_url(url)

        st.subheader("Analysis Result")

        if score <= 20:
            st.success("Low Risk")
        elif score <= 50:
            st.warning("Medium Risk")
        else:
            st.error("High Risk")

        st.metric("Risk Score", f"{score}/100")

        st.progress(score)

        st.subheader("Detected Issues")

        if reasons:
            for item in reasons:
                st.write("•", item)
        else:
            st.success("No suspicious patterns found.")

        st.subheader("Recommendation")

        if score > 50:
            st.error("Avoid opening this URL.")
        elif score > 20:
            st.warning("Proceed with caution.")
        else:
            st.success("URL appears safe.")