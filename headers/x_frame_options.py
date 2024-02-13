def get_info():
    return info_dict


desc_str = ("The X-Frame-Options response header (also named XFO) improves the protection of web applications against\n"
            "clickjacking")
best_practice_str = "deny"

info_dict = {
    'title': 'X-Frame-Options',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "0"
}
