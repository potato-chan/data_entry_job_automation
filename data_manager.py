from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class DataManager:

    def __init__(self, otodom_link: str, google_form_link: str, limit=36):
        self.otodom_link = otodom_link.replace("limit=36", f"limit={limit}")
        self.google_form_link = google_form_link
        self.all_ads = []

    def create_list_with_ads(self):
        page_source = self.get_ads_data()

        soup = BeautifulSoup(page_source, "html.parser")
        all_ads_data = soup.select('main div:nth-child(2) div > ul li')

        for ad in all_ads_data:
            try:
                price = ad.select_one('article div span:nth-child(1)').getText()
            except AttributeError:
                pass
            else:
                rent = ad.select_one('article div span:nth-child(4)').getText()
                address = ad.select_one('article p span').getText()
                url_data = ad.select_one('a')
                url = url_data.get("href")
                url = "https://www.otodom.pl" + url
                full_price = price + " " + rent
                ad_data = {
                    "price": full_price,
                    "address": address,
                    "link": url,
                }
                self.all_ads.append(ad_data)

    def get_ads_data(self):
        otodom_browser = webdriver.Chrome()
        otodom_browser.get(self.otodom_link)

        otodom_browser.implicitly_wait(10)
        accept_button = otodom_browser.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
        accept_button.click()

        time.sleep(2)

        for i in range(50):
            otodom_browser.execute_script(f"window.scrollBy(0, 2000)")
            time.sleep(0.1)

        page_source = otodom_browser.page_source

        otodom_browser.quit()

        return page_source

    def send_all_ads_to_google_forms(self):
        for ad in self.all_ads:
            google_form_browser = webdriver.Chrome()
            google_form_browser.get(self.google_form_link)

            google_form_browser.implicitly_wait(10)
            google_form_inputs = google_form_browser.find_elements(By.CSS_SELECTOR, "form div div div input")

            google_form_input_address = WebDriverWait(driver=google_form_browser, timeout=5).until(
                expected_conditions.element_to_be_clickable(google_form_inputs[0])
            )
            google_form_input_address.send_keys(ad["address"])

            google_form_input_full_price = WebDriverWait(driver=google_form_browser, timeout=5).until(
                expected_conditions.element_to_be_clickable(google_form_inputs[1])
            )
            google_form_input_full_price.send_keys(ad["price"])

            google_form_input_link = WebDriverWait(driver=google_form_browser, timeout=5).until(
                expected_conditions.element_to_be_clickable(google_form_inputs[2])
            )
            google_form_input_link.send_keys(ad["link"])

            google_form_submit = google_form_browser.find_element(By.CSS_SELECTOR, "form div div > div > span > span")
            google_form_submit.click()

            time.sleep(1)
            google_form_browser.quit()
