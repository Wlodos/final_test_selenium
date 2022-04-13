from pages.base import BasePage
from Locators.locators import AuthFormLocators


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = "https://www.labirint.ru/cabinet"
        self.driver.get(url)
        self.auth_form = driver.find_element(*AuthFormLocators.auth_form)
        self.close_btn = driver.find_element(*AuthFormLocators.close_btn)
        self.phone_num_field = driver.find_element(*AuthFormLocators.phone_num_field)
        self.enter_btn = driver.find_element(*AuthFormLocators.enter_btn)
        self.agreement_check_box = driver.find_element(*AuthFormLocators.agreement_check_box)

    def enter_phone_number(self, number: str):
        self.phone_num_field.clear()
        self.phone_num_field.send_keys(number)

    def another_ways_to_enter_bnt_click(self):
        self.another_ways_to_enter = self.driver.find_element(*AuthFormLocators.another_ways_to_enter)
        self.another_ways_to_enter.click()
        self.auth_social_links_box = self.driver.find_element(*AuthFormLocators.auth_social_links_box)
        self.vk_link = self.driver.find_element(*AuthFormLocators.vk_link)
        self.ok_link = self.driver.find_element(*AuthFormLocators.ok_link)
        self.mail_ru_link = self.driver.find_element(*AuthFormLocators.mail_ru_link)
        self.yandex_link = self.driver.find_element(*AuthFormLocators.yandex_link)
        self.gmail_link = self.driver.find_element(*AuthFormLocators.gmail_link)







