def get_info():
    return info_dict


desc_str = ("The HTTP Cross-Origin-Opener-Policy (COOP) response header allows you to ensure a top-level document does\n"
            "not share a browsing context group with cross-origin documents.")
best_practice_str = "same-origin"

info_dict = {
    'title': 'Cross-Origin-Opener-Policy',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "0"
}
