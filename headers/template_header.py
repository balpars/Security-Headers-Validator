def get_info():
    return info_dict


desc_str = "Bu header'in bu sekilde kullanimi bu zafiyete sebep olur, su sekilde ayarlanmalidir"
best_practice_str = "1, None"

info_dict = {
    'title': 'Sample-Header',
    'best-practice': best_practice_str,
    'priority': "1", # 2 if it's not a security header, but is used to hide server info
    'description': desc_str,
    'deprecated': "1" # 1 if it should no longer be used
}
