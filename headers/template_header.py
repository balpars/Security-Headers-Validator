def get_info():
    return info_dict

vuln_str = "Bu header'in bu sekilde kullanimi bu zafiyete sebep olur, su sekilde ayarlanmalidir"
info_dict = {
    'title':'Sample-Header',
    'best-practice': [None], 
    'priority': 1, 
    'description': vuln_str, 
    'obsolete': 1 
}