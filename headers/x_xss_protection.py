def get_info():
    return info_dict

vuln_str = "Bu header'in bu sekilde kullanimi bu zafiyete sebep olur, su sekilde ayarlanmalidir"

# priority'yi şimdilik kafama göre yazdım :)
info_dict = {
    'title':'X-XSS-Protection',
    'best-practice': [0, None],
    'priority': 2,
    'description': vuln_str,
    'obsolote': 1 # var ama aslında kaldırılması gerekli
}