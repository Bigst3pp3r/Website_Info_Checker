from checker.trust_signals import check_https, get_whois_info, check_contact_info, check_blacklists, classify_content_tone
from checker.fetcher import fetch_site_content

def analyze_site(url: str) -> dict:
    content = fetch_site_content(url)
    return {
        "https": check_https(url),
        "whois": get_whois_info(url),
        "contact_info": check_contact_info(url),
        "content": content,
        "blacklist": check_blacklists(url),
        "tone": classify_content_tone(content.get("text_sample", "")) if "text_sample" in content else "No content"
    }
