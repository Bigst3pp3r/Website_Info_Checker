import whois
from urllib.parse import urlparse

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