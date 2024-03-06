import requests
from datetime import datetime

# Generate the URL with today's date
today = datetime.now().strftime("%Y/%m/%d")
url = f"https://static01.nyt.com/images/{today}/nytfrontpage/scan.pdf"

# Define the path to save the PDF
save_path = f"PDFs/{datetime.now().strftime('%Y-%m-%d')}.pdf"

# Download and save the PDF
response = requests.get(url)
if response.status_code == 200:
    with open(save_path, 'wb') as f:
        f.write(response.content)
