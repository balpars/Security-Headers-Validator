import requests


def get_header(url):
    response = requests.get(url)
    headers = {key.lower(): value.lower() for key, value in response.headers.items()}
    return headers


def main():
    headers = get_header("https://google.com")
    print(headers)


if __name__ == "__main__":
    main()
