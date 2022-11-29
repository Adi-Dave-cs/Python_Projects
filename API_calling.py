import requests
# https://www.webfx.com/web-development/glossary/http-status-codes/

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if(response.status_code == 200):
    # prints data directly in the text format
    # print(response.text)
    data = response.json()
    print(data)
else:
    print("Error Reported")