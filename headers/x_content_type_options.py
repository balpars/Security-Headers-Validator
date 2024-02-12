def get_info():
    return info_dict


desc_str = "Setting this header will prevent the browser from interpreting files as a different MIME type to what is specified in the Content-Type HTTP header (e.g. treating text/plain as text/css)."
<<<<<<< HEAD
best_practice_str = "nosniff"
=======
best_practice_str = "1"
>>>>>>> 844cbb506ca08b9e0be29a65f16b93edc1a30ee0

info_dict = {
    'title': 'X-Content-Type-Options',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "0"
}
