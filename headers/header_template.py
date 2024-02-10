def get_info():
    return info_dict

vuln = "Bu header'ın kullanımı şu zafiyetleri doğurur"

# var olmaması lazımsa (eski bir header gibi) best practice'e None diyelim
# priority'yi şimdilik kafama göre yazdım :)
info_dict = {
    'tite':'sample_header',
    'best-practice': [None], 
    'priority': 1
}