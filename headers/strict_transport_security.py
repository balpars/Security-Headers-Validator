def get_info():
    return info_dict


desc_str = ("HTTP Strict Transport Security (also named HSTS) is a web security policy mechanism which helps to\n"
            "protect websites against protocol downgrade attacks and cookie hijacking. It allows web servers to\n"
            "declare that web browsers (or other complying user agents) should only interact with it using secure\n"
            "HTTPS connections, and never via the insecure HTTP protocol.")
best_practice_str = "max-age=31536000; includeSubDomains"

info_dict = {
    'title': 'Strict-Transport-Security',
    'best-practice': best_practice_str,
    'priority': "1", 
    'description': desc_str,
    'deprecated': "0"
}
