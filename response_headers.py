import requests

def response_header(url):
    response = requests.get(url)
    headers = response.headers
    return headers

def main():
    headers = response_header()
    print(headers)

if __name__ == "__main__":
    main()