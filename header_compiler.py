import importlib.util
import os

# yeni header'lar buraya
header_files = ["x_content_type_options.py", "x_xss_protection.py"]

HEADER_DIR = os.path.join(os.getcwd(), "headers")

def load_headers():
    headers = {}

    for file_name in header_files:
        header_name = file_name.split(".")[0]
        module_name = f"{header_name}"
        file_path = os.path.join(HEADER_DIR, file_name)

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        #header_info = module.get_info() # sözlüğün tamamı burada geldi
        header_info = {key.lower():value.lower() for key,value in module.get_info().items()}
        header_title = header_info['title']
        headers[header_title] = header_info

    return headers


def main():
    headers = load_headers()
    print(headers)
    

if __name__ == "__main__":
    main()
