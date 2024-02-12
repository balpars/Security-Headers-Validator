def get_info():
    return info_dict


desc_str = "The HTTP Cross-Origin-Resource-Policy response header conveys a desire that the browser blocks no-cors cross-origin/cross-site requests to the given resource"
best_practice_str = "same-origin"

info_dict = {
    'title': 'Cross-Origin-Resource-Policy',
    'best-practice': best_practice_str,
    'priority': "1", 
    'description': desc_str,
    'deprecated': "0" 
}