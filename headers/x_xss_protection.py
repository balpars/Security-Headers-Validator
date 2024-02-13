def get_info():
    return info_dict


desc_str = ("Warning: The X-XSS-Protection header has been deprecated by modern browsers and its use can introduce\n"
            "additional security issues on the client side. Use Content-Security-Policy instead.")
best_practice_str = "0"

info_dict = {
    'title': 'X-XSS-Protection',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "1"
}
