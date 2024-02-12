def get_info():
    return info_dict


<<<<<<< HEAD
desc_str = "This header holds directives (instructions) for caching in both requests and responses. If a given directive is in a request, it does not mean this directive is in the response. Specify the capability of a resource to be cached is important to prevent exposure of information via the cache."
best_practice_str = "no-store, max-age=0"

info_dict = {
    'title': 'Cache-Control',
    'best-practice': best_practice_str,
    'priority': "1", 
    'description': desc_str,
    'deprecated': "0" 
=======
desc_str = "Bu header'in bu sekilde kullanimi bu zafiyete sebep olur, su sekilde ayarlanmalidir"
best_practice_str = "no-store, max-age=0"

info_dict = {
    'title': 'Sample-Header',
    'best-practice': best_practice_str,
    'priority': "1", # 2 if it's not a security header, but is used to hide server info
    'description': desc_str,
    'deprecated': "1" # 1 if it should no longer be used
>>>>>>> 844cbb506ca08b9e0be29a65f16b93edc1a30ee0
}
