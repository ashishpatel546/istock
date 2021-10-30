import requests

url = "https://latest-mutual-fund-nav.p.rapidapi.com/fetchLatestNAV"

headers = {
    'x-rapidapi-host': "latest-mutual-fund-nav.p.rapidapi.com",
    'x-rapidapi-key': "bbdc55e275mshd5fbb490f999f4cp1300fbjsn631c6dc46a59"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)