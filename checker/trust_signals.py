import whois
from urllib.parse import urlparse
import requests
import re
from bs4 import BeautifulSoup
def check_https(url):
    return url.lower().startswith("https")

def get_whois_info(url):
    try:
        domain = urlparse(url).netloc
        info = whois.whois(domain)
        return {
            "domain_age": str(info.creation_date),
            "registrar": info.registrar
        }
    except Exception as e:
        return {"error": str(e)}

def check_contact_info(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text().lower()

        indicators = ["contact", "email", "phone", "call us", "reach us"]
        found_keywords = [word for word in indicators if word in text]

        emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
        phones = re.findall(r"\+?\d[\d\s\-().]{7,}\d", text)

        result = []
        if found_keywords:
            result.append(f"Keywords found: {', '.join(found_keywords)}")
        if emails:
            result.append(f"Emails: {', '.join(set(emails))}")
        if phones:
            result.append(f"Phones: {', '.join(set(phones))}")

        return " | ".join(result) if result else "No contact info found"
    except Exception as e:
        return f"Contact info scan failed: {str(e)}"

def check_blacklists(url):
    domain = urlparse(url).netloc
    try:
        # Simple check using OpenPhish public list (for illustration purposes only)
        openphish_url = "https://openphish.com/feed.txt"
        resp = requests.get(openphish_url, timeout=10)
        if domain in resp.text:
            return "Listed in OpenPhish"
        return "Not found in known blacklists"
    except Exception as e:
        return f"Blacklist check failed: {str(e)}"
    
def classify_content_tone(text):
    scam_indicators = [
        "urgent", "limited time", "click here", "act now", "congratulations",
        "you won", "free", "risk-free", "guaranteed", "credit card", "bitcoin"
    ]
    legit_indicators = [
        "about us", "contact", "privacy policy", "terms of service",
        "customer service", "secure", "verified", "registered company"
    ]

    scam_count = sum(1 for word in scam_indicators if word in text.lower())
    legit_count = sum(1 for word in legit_indicators if word in text.lower())

    if scam_count > legit_count:
        return "⚠️ Suspicious/Scam-like"
    elif legit_count > scam_count:
        return "✅ Likely Legitimate"
    else:
        return "❓ Unclear"
    
    
    