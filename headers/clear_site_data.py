def get_info():
    return info_dict


desc_str = ("The Clear-Site-Data header clears browsing data (cookies, storage, cache) associated with the requesting "
            "website. It allows web developers to have more control over the data stored by a client browser for "
            "their origins.")
best_practice_str = "\"cache\", \"cookies\", \"storage\""

info_dict = {
    'title': 'Clear-Site-Data',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "0"
}
