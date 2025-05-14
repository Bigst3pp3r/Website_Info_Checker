def format_report(data: dict) -> str:
    lines = ["### Site Legitimacy Report"]
    lines.append(f"- **HTTPS**: {'Yes' if data['https'] else 'No'}")
    whois = data['whois']
    if 'error' in whois:
        lines.append(f"- **WHOIS**: Error - {whois['error']}")
    else:
        lines.append(f"- **Domain Age**: {whois['domain_age']}")
        lines.append(f"- **Registrar**: {whois['registrar']}")
    content = data['content']
    if 'error' in content:
        lines.append(f"- **Content Fetch**: Error - {content['error']}")
    else:
        lines.append(f"- **Title**: {content['title']}")
    return "\n".join(lines)
