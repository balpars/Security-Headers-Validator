

## About Security Headers Validator

Security Headers Validator is a Python tool designed to detect missing security headers and use of deprecated headers, based on the OWASP Secure Headers Project. 
It provides a simple way to identify potential security risks associated with the headers sent by web servers.

Security Headers Validator detects:
 - Missing security headers
 - Use of deprecated security headers
 - Use of recommended security headers

Security Headers Validator is written to be modular and hackable, you can easily add your custom headers and it's best practices.

## Security Headers Validator in Action

<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/89816332/304434905-3738fa09-045a-4f68-bc52-ad5c9301d92d.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240213T140321Z&X-Amz-Expires=300&X-Amz-Signature=b7989db5491c453d1dd359ac2c293b968ad51461b1a8f6579c016d449a2700b3&X-Amz-SignedHeaders=host&actor_id=159152213&key_id=0&repo_id=753684265](https://private-user-images.githubusercontent.com/89816332/305702379-7567c2bc-75ff-4b2d-955d-57e3c848ea9f.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDgyNDg2NDksIm5iZiI6MTcwODI0ODM0OSwicGF0aCI6Ii84OTgxNjMzMi8zMDU3MDIzNzktNzU2N2MyYmMtNzVmZi00YjJkLTk1NWQtNTdlM2M4NDhlYTlmLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMTglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjE4VDA5MjU0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQzYzU4ZmJkZDQxN2RmNmQ0MTEyMmFlM2Q4MmI5MzU0ZTZjODQxYTgzNzIyMTAxYzE2ZDZhOTM2MGIwZDkyOTMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ts0hnpYeBufmU-qxnECaWBSCy3UGzxmfQW8mQFBMhYc)" width=800px>

## Installation

Security Headers Validator supports **Python 3**. Just clone the repository and and all is set. Install the requests library if needed.

```
$ git clone https://github.com/balpars/Security-Headers-Validator.git
$ cd Security-Headers-Validator
$ pip3 install -r requirements.txt
```

## Dependencies

Security Headers Validator depends on the `requests` Python module. 
This dependency can be installed using [pip](https://pypi.python.org/pypi/pip).
```
$ pip3 install -r requirements.txt
```

## Usage

Short Form    | Long Form | Description
------------- |-----------|-------------
-t            | --target  | target url eg. https://example_site.com
-h            | --help    | show the help message and exit


* Specify target with -t variable. Provide the full url as below.

`python scanner.py -t https://example_site.com`

## How do I add a new header?

By following steps below you can add and integrate your headers to Security Headers Validator.

1 - Navigate to headers folder and create the <header_name>.py file eg. user_agent.py

2 - Copy the contents of template_header.py into your header file.

3 - Modify your header file as needed.

4 - Find the list variable "header_files" in the header_compiler.py

5 - Append the file name to header_files eg.   
    ```
    header_files = ["x_content_type_options.py", "user_agent.py"]
    ```

Optinal: Test your headers. Append the file name to header_files in test_headers.py. 
Run the test_headers.py to ensure that your header file works correctly. 
    ```
    pytest test_headers.py
    ```

#### Warnings
Header file names should not contain dashes. Instead use underscore. This is to prevent import errors.

Correct: user_agent.py
Incorrect: user-agent.py


## Unit-test

* Requires pytest

Navigate to projects directory and run the command below to test if your
headers work.

`pytest tests/test_headers.py`

## Planned Future Improvements

- [ ] List argument to scan a url list.
- [ ] Detect information disclosures in headers
- [ ] Detect weak CSP configurations.

## Final remarks
- This is the first time we publicly release a tool. Contributions are much appreciated!

- This project will be regularly updated and continued to be improved.

- If you'd like to get in touch with us for any suggestions regarding the project, feel free to open an issue or send a pull request.

- We thank you!

## Contributors
```
Yasin Çelik
Bedirhan Alp Arslan
```
