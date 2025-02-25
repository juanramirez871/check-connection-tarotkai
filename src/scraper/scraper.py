import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self):
        self.session = requests.Session()

    def get_page_content(self, panel_url):
        protected_url = panel_url
        protected_page = self.session.get(protected_url)
        soup = BeautifulSoup(protected_page.content, "html.parser")
        print(soup.prettify())
        return soup

    def login(self, payload, url_login):
        response = self.session.post(url_login, data=payload)
        if response.status_code == 200:
            return response
        else:
            print(f"Error in the login: {response.status_code}")
