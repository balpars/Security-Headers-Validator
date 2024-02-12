# test_load_headers.py
import importlib.util
import os
import pytest

HEADER_DIR = os.path.join(os.path.dirname(os.getcwd()), "headers")
header_files = ["x_content_type_options.py", "x_xss_protection.py"]


@pytest.mark.parametrize("header_file", header_files)
def test_header_file_exists(header_file):
    file_path = os.path.join(HEADER_DIR, header_file)
    assert os.path.exists(file_path), f"Header file '{header_file}' does not exist"


@pytest.mark.parametrize("header_file", header_files)
def test_header_module_has_get_info_function(header_file):
    module = load_header_module(header_file)
    assert hasattr(module, "get_info"), f"Header module '{module.__name__}' does not contain 'get_info()' function"


@pytest.mark.parametrize("header_file", header_files)
def test_get_info_returns_dictionary(header_file):
    info_dict = load_header_get_info(header_file)
    assert isinstance(info_dict, dict), f"get_info() in '{info_dict['__module__']}' did not return a dictionary"


@pytest.mark.parametrize("header_file", header_files)
def test_get_info_keys_exist(header_file):
    info_dict = load_header_get_info(header_file)
    required_keys = ['title', 'best-practice', 'priority', 'description', 'obsolete']
    assert all(
        key in info_dict for key in required_keys), f"Some required keys are missing in '{info_dict['__module__']}'"


@pytest.mark.parametrize("header_file", header_files)
def test_get_info_keys_not_empty(header_file):
    info_dict = load_header_get_info(header_file)
    assert all(info_dict[key] for key in info_dict), f"Some values in '{info_dict['__module__']}' are empty"


@pytest.mark.parametrize("header_file", header_files)
def test_priority_is_number_string(header_file):
    info_dict = load_header_get_info(header_file)
    priority_value = info_dict.get('priority')
    assert priority_value is not None and priority_value.isdigit(), f"The value of 'priority' in '{info_dict['__module__']}' is not a number string"


def load_header_module(header_file):
    file_path = os.path.join(HEADER_DIR, header_file)
    header_name = header_file.split(".")[0]
    module_name = header_name

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_header_get_info(header_file):
    module = load_header_module(header_file)
    return module.get_info()
