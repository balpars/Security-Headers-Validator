import header_compiler
import response_headers
import argparse
import header_comparator
import report_writer


def main():
    parser = argparse.ArgumentParser(description="Scan HTTP responses for vulnerable headers")
    parser.add_argument('-t', '--target', metavar='', help='Target url eg. https://abc.com', required=True)
    args = parser.parse_args()

    local_header_dict = header_compiler.load_headers()
    response_header_dict = response_headers.get_header(url=args.target)

    found_security_headers = header_comparator.find_security_headers(local_header_dict, response_header_dict)
    missing_headers = header_comparator.find_missing_headers(local_header_dict, response_header_dict)
    deprecated_headers= header_comparator.find_deprecated_headers(local_header_dict, response_header_dict)

    report_writer.write_report_short(data_list=found_security_headers, desc_str="These are the security headers found in target:", color="green")
    print()
    report_writer.write_report(data_list=missing_headers,desc_str="These are the missing headers in target", color="red")
    print()
    report_writer.write_report(data_list=deprecated_headers, desc_str= "These headers are deprecated, and should no longer be used", color="yellow")

if __name__ == "__main__":
    main()
