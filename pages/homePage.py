from pages.base import BasePage
from selenium.webdriver import ActionChains
from Locators.locators import HomeLocators


class HomePage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = "https://www.labirint.ru"
        self.driver.get(url)
        # main header elements
        self.logo = driver.find_element(*HomeLocators.logo)
        self.search_field = driver.find_element(*HomeLocators.search_field)
        self.search_btn = driver.find_element(*HomeLocators.search_btn)
        self.notification_btn = driver.find_element(*HomeLocators.notification_btn)
        self.my_lab_btn = driver.find_element(*HomeLocators.my_lab_btn)
        self.put_order_btn = driver.find_element(*HomeLocators.put_order_btn)
        self.cart_btn = driver.find_element(*HomeLocators.cart_btn)
        self.recommendations_link = driver.find_element(*HomeLocators.recommendations_link)

        # main menu
        self.books_menu_link = driver.find_element(*HomeLocators.books_menu_link)
        self.best_menu_link = driver.find_element(*HomeLocators.best_menu_link)
        self.school_menu_link = driver.find_element(*HomeLocators.school_menu_link)
        self.games_menu_link = driver.find_element(*HomeLocators.games_menu_link)
        self.office_menu_link = driver.find_element(*HomeLocators.office_menu_link)
        self.more_btn = driver.find_element(*HomeLocators.more_btn)
        self.club_menu_link = driver.find_element(*HomeLocators.club_menu_link)
        # additional menu links
        self.delivery_and_payment_link = driver.find_element(*HomeLocators.delivery_and_payment_link)
        self.certificates_link = driver.find_element(*HomeLocators.certificates_link)
        self.rating_link = driver.find_element(*HomeLocators.rating_link)
        self.novelty_link = driver.find_element(*HomeLocators.novelty_link)
        self.sale_link = driver.find_element(*HomeLocators.sale_link)
        self.contact_link = driver.find_element(*HomeLocators.contact_link)
        self.support_link = driver.find_element(*HomeLocators.support_link)

        self.in_social_media_btn = driver.find_element(*HomeLocators.in_social_media_btn)

    def move_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()




