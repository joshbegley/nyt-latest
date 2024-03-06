import requests
from datetime import datetime

today = datetime.now().strftime("%Y/%m/%d")
url = f"https://static01.nyt.com/images/{today}/nytfrontpage/scan.pdf"

save_path = f"{datetime.now().strftime('%Y-%m-%d')}.pdf"

response = requests.get(url)
if response.status_code == 200:
    with open(save_path, 'wb') as f:
        f.write(response.content)
