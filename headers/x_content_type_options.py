def get_info():
    return info_dict


desc_str = "Setting this header will prevent the browser from interpreting files as a different MIME type to what is specified in the Content-Type HTTP header (e.g. treating text/plain as text/css)."
best_practice_str = "nosniff"

info_dict = {
    'title': 'X-Content-Type-Options',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "0"
}
