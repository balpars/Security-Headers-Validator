def get_info():
    return info_dict


<<<<<<< HEAD
desc_str = "Warning: The X-XSS-Protection header has been deprecated by modern browsers and its use can introduce additional security issues on the client side. use Content-Security-Policy instead."
best_practice_str = "0"
=======
desc_str = "Bu header'in bu sekilde kullanimi bu zafiyete sebep olur, su sekilde ayarlanmalidir"
best_practice_str = "1"
>>>>>>> 844cbb506ca08b9e0be29a65f16b93edc1a30ee0

info_dict = {
    'title': 'X-XSS-Protection',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "1"
}
