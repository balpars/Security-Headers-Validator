def get_info():
    return info_dict


desc_str = ("The Referrer-Policy HTTP header governs which referrer information, sent in the Referer header,\n"
            "should be included with requests made.")
best_practice_str = "no-referrer"

info_dict = {
    'title': 'Referrer-Policy',
    'best-practice': best_practice_str,
    'priority': "1", 
    'description': desc_str,
    'deprecated': "0" 
}
