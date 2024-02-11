def get_info():
    return info_dict

vuln_str = "Bu header'in bu sekilde kullanimi bu zafiyete sebep olur, su sekilde ayarlanmalidir"
best_practice_str = "1"

info_dict = {
    'title':'X-Content-Type-Options',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': vuln_str,
    'obsolete': "1"
}