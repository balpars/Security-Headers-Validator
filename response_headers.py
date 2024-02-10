import requests

def get_header(url):
    response = requests.get(url)
    headers = response.headers
    return headers

def main():
    headers = get_header()
    print(headers)

if __name__ == "__main__":
    main()