def get_info():
    return info_dict

vuln_str = "Bu header'ın bu şekilde kullanımı şu zafiyeti doğurur"

# priority'yi şimdilik kafama göre yazdım :)
info_dict = {
    'tite':'X-Content-Type-Options',
    'best-practice': ['nosniff'],
    'priority': 1,
    'description': vuln_str
}