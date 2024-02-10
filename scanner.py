import header_compiler
import response_headers
import sys
import argparse


local_dict = header_compiler.load_headers()
header_dict = response_headers.get_header()

compare_result = compare(local_dict,header_dict)
