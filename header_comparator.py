from data_class import Data

def compare(local_header_dict, response_header_dict):
    
    veri_listesi = []

    # local'de olup da response'ta olmayan key'leri fark sözlüğüne eklemek
    
    # örnek bir fark sözlüğü
    fark = {'key1':{
                    'title':'X-Content-Type-Options',
                    'best_practice': ['nosniff'],
                    'priority': 1,
                    'description': "vuln_str",
                    'obsolete': 1
                    },
            'key12':{
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