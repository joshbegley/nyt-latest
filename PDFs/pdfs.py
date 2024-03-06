import requests
from datetime import datetime

today = datetime.now().strftime("%Y/%m/%d")
url = "https://static01.nyt.com/images/{0}/nytfrontpage/scan.pdf".format(today)

save_path = "{0}.pdf".format(datetime.now().strftime('%Y-%m-%d'))

response = requests.get(url)
if response.status_code == 200:
    with open(save_path, 'wb') as f:
        f.write(response.content)
