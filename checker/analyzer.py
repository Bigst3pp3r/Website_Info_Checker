from checker.trust_signals import check_https, get_whois_info, check_contact_info
from checker.fetcher import fetch_site_content

def analyze_site(url: str) -> dict:
    return {
        "https": check_https(url),
        "whois": get_whois_info(url),
        "contact_info": check_contact_info(url),
        "content": fetch_site_content(url)
    }