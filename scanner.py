import header_compiler
import response_headers
import argparse
import header_comparator
import report_writer

def main():
    
    parser = argparse.ArgumentParser(description="Scan HTTP responses for vulnerable headers")
    parser.add_argument('-t','--target', metavar='', help='Target url eg. https://abc.com', required=True)
    args = parser.parse_args()
    
    local_header_dict = header_compiler.load_headers()
    response_header_dict = response_headers.get_header(url=args.target)
    
    comparison_result = header_comparator.compare(local_header_dict,response_header_dict)
    report_writer.write_report(data_list=comparison_result)

if __name__ == "__main__":
    main()