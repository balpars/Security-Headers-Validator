def get_info():
    return info_dict


desc_str = ("This header has been deprecated by all major browsers and is no longer recommended. Avoid using it, "
            "and update existing code if possible")
best_practice_str = ""

info_dict = {
    'title': 'Public-Key-Pins',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "1"
}
