def get_info():
    return info_dict


desc_str = "CSP prevents a wide range of attacks, including cross-site scripting and other cross-site injections."
best_practice_str = ("Set CSP as needed. for info https://owasp.org/www-project-secure-headers/#content-security-policy")

info_dict = {
    'title': 'Content-Security-Policy',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "0"
}
