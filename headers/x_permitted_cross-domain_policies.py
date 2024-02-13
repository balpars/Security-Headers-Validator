def get_info():
    return info_dict


desc_str = ("A cross-domain policy file is an XML document that grants a web client, such as Adobe Flash Player or\n"
            "Adobe Acrobat (though not necessarily limited to these), permission to handle data across domains")
best_practice_str = "none"

info_dict = {
    'title': 'X-Permitted-Cross-Domain-Policies',
    'best-practice': best_practice_str,
    'priority': "1",
    'description': desc_str,
    'deprecated': "0"
}
