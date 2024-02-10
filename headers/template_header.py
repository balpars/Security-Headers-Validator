def get_info():
    return info_dict

vuln_str = "Bu header'in bu sekilde kullanimi bu zafiyete sebep olur, su sekilde ayarlanmalidir"

# var olmaması lazımsa (eski bir header gibi) best practice'e None diyelim
# priority'yi şimdilik kafama göre yazdım :)
info_dict = {
    'title':'Sample-Header',
    'best-practice': [None], 
    'priority': 1,
    'description': vuln_str,
    'obsolote': 1 # var ama aslında kaldırılması gerekli
}