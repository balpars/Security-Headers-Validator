def get_info():
    return info_dict


desc_str = ("This header holds directives (instructions) for caching in both requests and responses. If a given\n"
            "directive is in a request, it does not mean this directive is in the response. Specify the capability of\n"
            "a resource to be cached is important to prevent exposure of information via the cache.")
best_practice_str = "no-store, max-age=0"

info_dict = {
    'title': 'Cache-Control',
    'best-practice': best_practice_str,
    'priority': "1", 
    'description': desc_str,
    'deprecated': "0" 
}
