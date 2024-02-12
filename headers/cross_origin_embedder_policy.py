def get_info():
    return info_dict


desc_str = ("This response header prevents a document from loading any cross-origin resources that don\'t explicitly "
            "grant the document permission.")
best_practice_str = "require-corp"

info_dict = {
    'title': 'Cross-Origin-Embedder-Policy',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "0"
}
