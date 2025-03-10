from scraper.scraper import WebScraper
from scraper.utils import validate_url, get_value_from_json, update_count_mistakes
from scraper.whatsapp import send_message
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv("/src/.env")

if __name__ == "__main__":
    if validate_url(os.environ.get("PANEL_URL")) and validate_url(
        os.environ.get("LOGIN_URL")
    ):
        current_time = datetime.now()

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

        if get_value_from_json("report.json", "count_checks") == 107:
            update_count_mistakes("report.json", "count_mistakes", 0, "count_checks", 0)

            if get_value_from_json("report.json", "count_mistakes") == 0:
                send_message(
                    "✅🤖 en 18 horas a transcurrido con exito, sin fallas detectadas  🤖✅"
                )
            else:
                send_message(
                    f"👀🤖 hubieron {get_value_from_json('report.json', 'count_mistakes')} errores en 18 horas 🤖👀"
                )

    else:
        print("❌ url is not valid ❌")
