from data_class import Data

x = "BEDIRHAN".lower()

def compare(local_header_dict, response_header_dict):
    local_header_key = list(local_header_dict.keys())
    response_header_key = list(response_header_dict.keys())
    print(response_header_key)
    different_keys = []

    ilk_set = set(local_header_key)
    ikinci_set = set(response_header_key)

    fark = list(ilk_set - ikinci_set)

    print("Birinci listede olan ancak ikinci listede olmayanlar:", fark)

    veri_listesi = []

    # local'de olup da response'ta olmayan key'leri fark sözlüğüne eklemek
    
    for key in fark:
        veri = local_header_dict[key]

        title = veri['title']
        best_practice =veri['best-practice']
        priority = veri['priority']
        description = veri['description']
        is_obsolete = veri['obsolete']

        veri_listesi.append(Data(title=title, best_practice=best_practice , priority=priority, description=description, is_obsolete=is_obsolete))
    
    # Veri listesini get_priority'den faydalanarak sıralamak

    return veri_listesi
