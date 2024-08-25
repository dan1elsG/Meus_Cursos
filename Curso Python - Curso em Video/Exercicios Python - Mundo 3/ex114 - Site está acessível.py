import requests

try:
    url = "https://www.youtube.com"
    response = requests.get(url)
    if response.status_code == 200:
        print("\033[32mEsse site esta acessivel\033[m")
except:
    print('\033[31mINDISPONIVEL\033[m')

