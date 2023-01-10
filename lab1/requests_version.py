import requests
print(requests.__version__)
print(requests.get("http://www.google.com/").content)
print(requests.get("https://raw.githubusercontent.com/Gerrinator/404labs/master/lab1/requests_version.py").content)