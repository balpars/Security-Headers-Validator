def get_info():
    return info_dict

vuln_str = "Bu header'ın bu şekilde kullanımı şu zafiyeti doğurur"

# priority'yi şimdilik kafama göre yazdım :)
info_dict = {
    'tite':'X-XSS-Protection',
    'best-practice': [0, None],
    'priority': 2,
    'description': vuln_str
}