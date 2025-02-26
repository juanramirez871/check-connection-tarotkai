from scraper.scraper import WebScraper
from scraper.utils import validate_url, get_count_bad_status, set_count_bad_status
from scraper.whatsapp import send_message
from datetime import datetime
import os
import time

if __name__ == "__main__":
    if validate_url(os.environ.get("PANEL_URL")) and validate_url(
        os.environ.get("LOGIN_URL")
    ):
        while True:
            current_time = datetime.now()

            if current_time.minute % 30 == 0 and current_time.second == 0:
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

                if current_time.hour == 0 and current_time.minute == 0:
                    set_count_bad_status(True)

                    if get_count_bad_status() == 0:
                        send_message(
                            "✅🤖 El dia a transcurrido con exito, sin fallas  🤖✅"
                        )
                    else:
                        send_message(
                            f"👀🤖 hubieron {get_count_bad_status()} errores en el dia 🤖👀"
                        )

                time.sleep(1)

            time.sleep(10)

    else:
        print("❌ url is not valid ❌")
