from scraper.scraper import WebScraper
from scraper.utils import validate_url
import os

if __name__ == "__main__":
    if validate_url(os.getenv("URL_LOGIN")) and validate_url(os.getenv("URL_LOGIN")):
        scraper = WebScraper()
        scraper.login(
            {
                "input_user": os.getenv("USER"),
                "input_pass": os.getenv("PASSWORD"),
                "submit_login": "",
            },
            os.getenv("URL_LOGIN"),
        )

        soupPanel = scraper.get_page_content(os.getenv("PANEL_URL"))
    else:
        print("❌ url is not valid ❌")
