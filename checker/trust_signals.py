import whois
from urllib.parse import urlparse
import requests

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
    # Placeholder; could scan for 'contact' keywords in HTML
    return "Not implemented"

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