from data_class import Data


def find_missing_headers(local_header_dict, response_header_dict):
    local_header_key_list = list(local_header_dict.keys())
    response_header_key_list = list(response_header_dict.keys())
    local_header_set = set(local_header_key_list)
    response_header_set = set(response_header_key_list)
    missing_response_headers = list(local_header_set - response_header_set)

    missing_header_data_list = []
    for key in missing_response_headers:
        data = local_header_dict[key]
        title = data['title']
        best_practice = data['best-practice']
        priority = data['priority']
        description = data['description']
        is_obsolete = data['deprecated']

        if is_obsolete == "1":
            continue

        missing_header_data_list.append(
            Data(title=title, best_practice=best_practice, priority=priority, description=description,
                 is_obsolete=is_obsolete))

    return missing_header_data_list


def find_deprecated_headers(local_header_dict, response_header_dict):
    local_header_key_list = list(local_header_dict.keys())
    response_header_key_list = list(response_header_dict.keys())
    local_header_set = set(local_header_key_list)
    response_header_set = set(response_header_key_list)
    common_response_headers = list(local_header_set & response_header_set)

    deprecated_response_headers = []

    for key in common_response_headers:
        data = local_header_dict[key]
        title = data['title']
        best_practice = data['best-practice']
        priority = data['priority']
        description = data['description']
        is_obsolete = data['deprecated']

        if is_obsolete == "0":
            continue

        deprecated_response_headers.append(
            Data(title=title, best_practice=best_practice, priority=priority, description=description,
                 is_obsolete=is_obsolete))

    return deprecated_response_headers


def find_security_headers(local_header_dict, response_header_dict):
    local_header_key_list = list(local_header_dict.keys())
    response_header_key_list = list(response_header_dict.keys())
    local_header_set = set(local_header_key_list)
    response_header_set = set(response_header_key_list)
    common_response_headers = list(local_header_set & response_header_set)

    data_list = []
    for key in common_response_headers:
        data = local_header_dict[key]
        title = data['title']
        best_practice = data['best-practice']
        priority = data['priority']
        description = data['description']
        is_obsolete = data['deprecated']

        if is_obsolete == "1":
            continue

        data_list.append(Data(title=title, best_practice=best_practice, priority=priority, description=description,
                              is_obsolete=is_obsolete))

    return data_list
