from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from scraper.whatsapp import send_message
from scraper.utils import update_count_mistakes
import tempfile
import time


class WebScraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.binary_location = "/snap/bin/chromium"
        user_data_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.binary_location = "/usr/bin/chromium"

        self.driver = webdriver.Chrome(
            service=Service("/usr/bin/chromedriver"),
            options=options,
        )

    def check_connection_panel(self, soup):
        time.sleep(10)
        try:
            connected_element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(text(), 'Connected')]")
                )
            )

            if not connected_element:
                update_count_mistakes("report.json", "count_mistakes", 1)
                send_message(
                    "🤖 Detecto que la línea de Isabel está desconectada. Por favor, revisar. 🤖"
                )

        except TimeoutException:
            update_count_mistakes("report.json", "count_mistakes", 1)
            send_message(
                "🤖 Detecto que la línea de Isabel está desconectada. Por favor, revisar. 🤖"
            )

    def get_page_content(self, panel_url):
        self.driver.get(panel_url)
        try:
            time.sleep(10)
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "ember282"))
            )

            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")
            return soup

        except Exception as e:
            raise Exception(f"error getting page content: {e}")

    def login(self, payload, url_login):
        self.driver.get(url_login)

        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "input_user"))
            )
            username_input = self.driver.find_element(By.ID, "input_user")
            password_input = self.driver.find_element(By.NAME, "input_pass")

            username_input.send_keys(payload["input_user"])
            password_input.send_keys(payload["input_pass"])
            login_button = self.driver.find_element(By.NAME, "submit_login")
            login_button.click()

            WebDriverWait(self.driver, 10).until(EC.url_changes(url_login))

        except NoSuchElementException as e:
            raise Exception(f"Login error: Item could not be found: {e}")

        except TimeoutException as e:
            raise Exception(f"Login failed: Timeout: {e}")

        except Exception as e:
            raise Exception(f"Error at the login: {e}")

    def close(self):
        self.driver.quit()
