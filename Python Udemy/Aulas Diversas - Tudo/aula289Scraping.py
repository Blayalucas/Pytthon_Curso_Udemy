

import requests

from bs4 import BeautifulSoup

url = 'https://www.youtube.com/'

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser' )

if parsed_html.title is not None: 
    print(parsed_html.title.text)


top_jobs_heading = parsed_html.select_one("#intro > div> div > article > h2")

if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    print(article)