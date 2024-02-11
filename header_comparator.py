from data_class import Data

def compare(local_header_dict, response_header_dict):
    local_header_key = list(local_header_dict.keys())
    response_header_key = list(response_header_dict.keys())
    print(response_header_key)
    different_keys = []

    ilk_set = set(local_header_key)
    ikinci_set = set(response_header_key)

    fark_listesi = list(ilk_set - ikinci_set)
    print("Birinci listede olan ancak ikinci listede olmayanlar:", fark_listesi)

    veri_listesi = []

    # local'de olup da response'ta olmayan key'leri fark sözlüğüne eklemek
    
    # örnek bir fark sözlüğü
    fark = {'X-Content-Type-Options':{
                    'title':'X-Content-Type-Options',
                    'best_practice': ['nosniff'],
                    'priority': 1,
                    'description': "vuln_str",
                    'obsolete': 1
                    },
            'User-Agent':{
                    'title':'User-Agent',
                    'best_practice': ['idk :)'],
                    'priority': 2,
                    'description': "vuln_str",
                    'obsolete': 1
                    }
            }
    
    for key in fark.keys():
        veri = fark[key]

        title = veri['title']
        best_practice =veri['best_practice']
        priority = veri['priority']
        description = veri['description']
        is_obsolete = veri['obsolete']

        veri_listesi.append(Data(title=title, best_practice=best_practice , priority=priority, description=description, is_obsolete=is_obsolete))
    
    # Veri listesini get_priority'den faydalanarak sıralamak

    return veri_listesi
