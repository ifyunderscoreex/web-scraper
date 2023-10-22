import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [

]

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        page_content = response.content
    else:
        print(f"Failed to retrieve the webpage at {url}. Status code:", response.status_code)
        continue

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page_content, "lxml")

    # Find and retrieve the <body> tag
    body_tag = soup.find("body")

    if body_tag:
        # Get the HTML content of the <body> tag, including its contents
        body_content = str(body_tag)
        print(f"Body content for {url}:\n{body_content}\n")
    else:
        print(f"No <body> tag found on the page {url}.\n")
