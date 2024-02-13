import importlib.util
import os

# add new headers to this list
header_files = [
    "cache_control.py",
    "clear_site_data.py",
    "content_security_policy.py",
    "cross_origin_embedder_policy.py",
    "cross_origin_opener_policy.py",
    "cross_origin_resource_policy.py",
    "expect_ct.py",
    "feature_policy.py",
    "permissions_policy.py",
    "pragma.py",
    "public_key_pins.py",
    "referrer_policy.py",
    "strict_transport_security.py",
    "x_content_type_options.py",
    "x_frame_options.py",
    "x_permitted_cross-domain_policies.py",
    "x_xss_protection.py"
]


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

        # Add the header dictionary to headers dictionary
        header_info = {key.lower(): value.lower() for key, value in module.get_info().items()}
        header_title = header_info['title']
        headers[header_title] = header_info

    return headers


def main():
    headers = load_headers()
    print(headers)


if __name__ == "__main__":
    main()
