

## About Security Headers Validator

Security Headers Validator is a Python tool designed to detect missing security headers and use of deprecated headers, based on the OWASP Secure Headers Project. 
It provides a simple way to identify potential security risks associated with the headers sent by web servers.

Security Headers Validator detects:
 - Missing security headers
 - Use of deprecated security headers
 - Use of recommended security headers

Security Headers Validator is written to be modular and hackable, you can easily add your custom headers and it's best practices.

## Security Headers Validator in Action

<img src="https://private-user-images.githubusercontent.com/89816332/305702379-7567c2bc-75ff-4b2d-955d-57e3c848ea9f.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDkxODIxMjEsIm5iZiI6MTcwOTE4MTgyMSwicGF0aCI6Ii84OTgxNjMzMi8zMDU3MDIzNzktNzU2N2MyYmMtNzVmZi00YjJkLTk1NWQtNTdlM2M4NDhlYTlmLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjI5VDA0NDM0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTE3MjkzNjU4MDIxZmRkMjRhMTBhODkxMWRiNmRmNzE4MmZhYjg3MDY4MzQyM2ViYWM1ODFiYjJmYjEyMDQxYjkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.eTx-Q--5gErQ1Ot3v_3f7Cxxa4eY4WxD-0YxZ13LD1k" width=800px>

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
