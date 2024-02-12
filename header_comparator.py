from data_class import Data


def sort_data(data_list):
    return data_list


def compare(local_header_dict, response_header_dict):
    local_header_key_list = list(local_header_dict.keys())
    response_header_key_list = list(response_header_dict.keys())

    local_header_set = set(local_header_key_list)
    response_header_set = set(response_header_key_list)
    missing_response_headers = list(local_header_set - response_header_set)

    data_list = []
    for key in missing_response_headers:
        data = local_header_dict[key]
        title = data['title']
        best_practice = data['best-practice']
        priority = data['priority']
        description = data['description']
        is_obsolete = data['deprecated']

        data_list.append(Data(title=title, best_practice=best_practice, priority=priority, description=description,
                              is_obsolete=is_obsolete))

    return data_list
