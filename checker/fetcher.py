import requests
from bs4 import BeautifulSoup

def fetch_site_content(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        return {
            "title": soup.title.string if soup.title else "No title",
            "text_sample": soup.get_text()[:200]
        }
    except Exception as e:
        return {"error": str(e)}