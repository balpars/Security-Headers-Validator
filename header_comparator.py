from data_class import Data

def compare(local_header_dict, response_header_dict):
    
    veri_listesi = []

    # local'de olup da response'ta olmayan elemanları fark sözlüğüne ekle
    # örnek
    fark = {'key0':{
                    'title':'X-Content-Type-Options',
                    'best_practice': ['nosniff'],
                    'priority': 1,
                    'description': "vuln_str",
                    'obsolete': 1 # var ama aslında kaldırılması gerekli
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
    
    return veri_listesi