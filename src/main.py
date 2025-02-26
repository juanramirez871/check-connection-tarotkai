from scraper.scraper import WebScraper
from scraper.utils import validate_url
import os

if __name__ == "__main__":
    if validate_url(os.environ.get("PANEL_URL")) and validate_url(
        os.environ.get("LOGIN_URL")
    ):
        scraper = WebScraper()
        scraper.login(
            {
                "input_user": os.environ.get("USER"),
                "input_pass": os.environ.get("PASSWORD"),
                "submit_login": "",
            },
            os.environ.get("LOGIN_URL"),
        )

        soupPanel = scraper.get_page_content(os.environ.get("PANEL_URL"))
        scraper.check_connection_panel(soupPanel)
        scraper.close()

    else:
        print("❌ url is not valid ❌")
