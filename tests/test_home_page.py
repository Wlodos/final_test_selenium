from pages.homePage import HomePage
from selenium.webdriver import ActionChains
from Locators.locators import HomeLocators


def test_01_home_page_is_opened(driver):
    """check if home page is opened"""
    page = HomePage(driver)
    assert page.driver.current_url == "https://www.labirint.ru/"


def test_02_logo_links_to_home_page(driver):
    """check if logo link provides to home page"""
    page = HomePage(driver)
    page.logo.click()
    assert page.driver.current_url == "https://www.labirint.ru/"


def test_03_search_field_opens_page_with_results_of_searching(driver):
    page = HomePage(driver)
    page.search_field.send_keys("book")
    page.search_btn.click()
    assert "book" in page.driver.current_url


def test_04_popup_message_displayed_when_the_mouse_is_on_the_notification_btn(driver):
    """check if the notification message is popped up when the mouse pointer is on notification button(Сообщения)"""
    page = HomePage(driver)
    ActionChains(driver).move_to_element(page.notification_btn).perform()
    assert page.driver.find_element(*HomeLocators.notification_btn_popup_mess).is_displayed() is True


def test_05_popup_message_displayed_when_the_mouse_is_on_the_my_lab_btn(driver):
    """check if message is popped up when the mouse pointer is on my_lab_btn(Мой лаб)"""
    page = HomePage(driver)
    ActionChains(driver).move_to_element(page.my_lab_btn).perform()
    assert page.driver.find_element(*HomeLocators.my_lab_btn_popup_mess).is_displayed() is True


def test_06_popup_message_displayed_when_the_mouse_is_on_the_put_order_btn(driver):
    """check if message is popped up when the mouse pointer is on put_order_btn(Отложено)"""
    page = HomePage(driver)
    ActionChains(driver).move_to_element(page.put_order_btn).perform()
    assert page.driver.find_element(*HomeLocators.put_order_btn_mess).is_displayed() is True


def test_07_popup_message_displayed_when_the_mouse_is_on_the_cart_btn(driver):
    """check if message is popped up when the mouse pointer is on cart_btn(Корзина)"""
    page = HomePage(driver)
    ActionChains(driver).move_to_element(page.cart_btn).perform()
    assert "have-dropdown-selected" in \
           page.driver.find_element(*HomeLocators.cart_btn_mess_indicator).get_attribute("class")


def test_08_notification_my_lab_put_order_and_cart_btn_have_links(driver):
    """check if notification btn, my_lab btn, put_order btn and cart bnt have links("Сообщения", "Мой лабиринт",
    "Отложено" и "Корзина")"""
    page = HomePage(driver)
    assert page.notification_btn.get_attribute("href") and page.my_lab_btn.get_attribute("href") \
           and page.put_order_btn.get_attribute("href") and page.cart_btn.get_attribute("href") != ""


def test_09_menu_btns_have_links(driver):
    """check if menu buttons("Книги", "Главное", "Школа", "Игрушки", "Канцтовары", "Клуб") have links"""
    page = HomePage(driver)
    assert page.books_menu_link.get_attribute("href") and page.best_menu_link.get_attribute("href") and \
           page.school_menu_link.get_attribute("href") and page.games_menu_link.get_attribute("href") and \
           page.office_menu_link.get_attribute("href") and page.club_menu_link.get_attribute("href") != ""


def test_10_dropdown_menu_appears_when_mouse_is_on_books_btn(driver):
    """check if drop down menu appears once mouse pointer is on "books"("Книги") menu button"""
    page = HomePage(driver)
    ActionChains(driver).move_to_element(page.books_menu_link).perform()
    assert page.driver.find_element(*HomeLocators.books_dropdown_menu).is_displayed() is True


def test_11_dropdown_menu_appears_when_mouse_is_on_school_btn(driver):
    """check if drop down menu appears once mouse pointer is on "school"("Школа") menu button"""
    page = HomePage(driver)
    ActionChains(driver).move_to_element(page.school_menu_link).perform()
    assert page.driver.find_element(*HomeLocators.school_dropdown_menu).is_displayed() is True


def test_12_dropdown_menu_appears_when_mouse_is_on_games_btn(driver):
    """check if drop down menu appears once mouse pointer is on "games"("Игрушки") menu button"""
    page = HomePage(driver)
    ActionChains(driver).move_to_element(page.games_menu_link).perform()
    assert page.driver.find_element(*HomeLocators.games_dropdown_menu).is_displayed() is True


def test_13_dropdown_menu_appears_when_mouse_is_on_office_btn(driver):
    """check if drop down menu appears once mouse pointer is on "office"("Канцтовары") menu button"""
    page = HomePage(driver)
    ActionChains(driver).move_to_element(page.office_menu_link).perform()
    assert page.driver.find_element(*HomeLocators.office_dropdown_menu).is_displayed() is True


def test_14_dropdown_menu_appears_when_mouse_is_on_more_btn(driver):
    """check if drop down menu appears once mouse pointer is on "more"("Ещё") menu button"""
    page = HomePage(driver)
    ActionChains(driver).move_to_element(page.more_btn).perform()
    assert page.driver.find_element(*HomeLocators.more_dropdown_menu).is_displayed() is True


def test_15_dropdown_menu_appears_when_mouse_is_on_club_btn(driver):
    """check if drop down menu appears once mouse pointer is on "club"("Клуб") menu button"""
    page = HomePage(driver)
    page.move_to_element(page.club_menu_link)
    assert page.driver.find_element(*HomeLocators.club_dropdown_menu).is_displayed() is True


def test_16_clicking_on_books_btn_provide_to_page_books(driver):
    """check if "books"(Книги) button/link provide to another page - "books" """
    page = HomePage(driver)
    page.books_menu_link.click()
    assert page.get_relative_link() == "/books/"


def test_17_clicking_on_best_btn_provide_to_page_best(driver):
    """check if "best"(Главное) button/link provide to another page - "best" """
    page = HomePage(driver)
    page.best_menu_link.click()
    assert page.get_relative_link() == "/best/"


def test_18_clicking_on_school_btn_provide_to_school_page(driver):
    """check if "school"(Школа) button/link provide to another page - "school" """
    page = HomePage(driver)
    page.school_menu_link.click()
    assert page.get_relative_link() == "/school/"


def test_19_clicking_on_games_btn_provide_to_games_page(driver):
    """check if "games"(Игрушки) button/link provide to another page - "games" """
    page = HomePage(driver)
    page.games_menu_link.click()
    assert page.get_relative_link() == "/games/"


def test_20_clicking_on_office_btn_provide_to_office_page(driver):
    """check if "office"(Канцтовары) button/link provide to another page - "office" """
    page = HomePage(driver)
    page.office_menu_link.click()
    assert page.get_relative_link() == "/office/"


def test_21_clicking_on_club_btn_provide_to_club_page(driver):
    """check if "club"(Клуб) button/link provide to another page - "club" """
    page = HomePage(driver)
    page.club_menu_link.click()
    assert page.get_relative_link() == "/club/"


def test_22_clicking_on_delivery_and_payment_btn_provide_to_help_page(driver):
    """check if "delivery and payment"(Доставка и оплата) button/link provide to another page - "help"
    with needed information """
    page = HomePage(driver)
    page.delivery_and_payment_link.click()
    assert page.get_relative_link() == "/help/"


def test_23_clicking_on_certificates_btn_provide_to_certificates_page(driver):
    """check if "certificates"(Сертификаты) button/link provide to another page - "certificates" """
    page = HomePage(driver)
    page.certificates_link.click()
    assert page.get_relative_link() == "/top/certificates/"


def test_24_clicking_on_rating_btn_provide_to_rating_page(driver):
    """check if "rating"(Рейтинги) button/link provide to another page - "rating" """
    page = HomePage(driver)
    page.rating_link.click()
    assert page.get_relative_link() == "/rating/"


def test_25_clicking_on_novelty_btn_provide_to_novelty_page(driver):
    """check if "novelty"(Новинки) button/link provide to another page - "novelty" """
    page = HomePage(driver)
    page.novelty_link.click()
    assert page.get_relative_link() == "/novelty/"


def test_26_sale_on_novelty_btn_provide_to_sale_page(driver):
    """check if "sale"(Скидки) button/link provide to another page - "sale" """
    page = HomePage(driver)
    page.sale_link.click()
    assert "/search/?discount" in page.driver.current_url


def test_27_contact_on_novelty_btn_provide_to_contact_page(driver):
    """check if "contact"(Контакты) button/link provide to another page - "contact" """
    page = HomePage(driver)
    page.contact_link.click()
    assert page.get_relative_link() == "/contact/"


def test_28_support_on_novelty_btn_provide_to_support_page(driver):
    """check if "support"(Поддержка) button/link provide to another page - "support" """
    page = HomePage(driver)
    page.support_link.click()
    assert page.get_relative_link() == "/support/"


def test_29_background_color_of_each_books_menu_element_is_changed_while_mouse_pointer_is_on_it(driver):
    """check if background color of book's menu elements is changed while mouse pointer is on it"""
    page = HomePage(driver)
    page.move_to_element(page.books_menu_link)
    menu_elements = page.driver.find_elements(*HomeLocators.books_menu_elements)
    for element in menu_elements:
        page.move_to_element(element)
        assert "active" in element.get_attribute("class")


def test_30_background_color_of_each_games_menu_element_is_changed_while_mouse_pointer_is_on_it(driver):
    """check if background color of games's menu elements is changed while mouse pointer is on it"""
    page = HomePage(driver)
    page.move_to_element(page.games_menu_link)
    menu_elements = page.driver.find_elements(*HomeLocators.games_menu_elements)
    for element in menu_elements:
        page.move_to_element(element)
        assert "active" in element.get_attribute("class")


def test_31_background_color_of_each_offices_menu_element_is_changed_while_mouse_pointer_is_on_it(driver):
    """check if background color of office's menu elements is changed while mouse pointer is on it"""
    page = HomePage(driver)
    page.move_to_element(page.office_menu_link)
    menu_elements = page.driver.find_elements(*HomeLocators.office_menu_elements)
    for element in menu_elements:
        page.move_to_element(element)
        assert "active" in element.get_attribute("class")


def test_32_background_color_of_each_more_menu_element_is_changed_while_mouse_pointer_is_on_it(driver):
    """check if background color of more's(Ещё) menu elements is changed while mouse pointer is on it"""
    page = HomePage(driver)
    page.move_to_element(page.more_btn)
    menu_elements = page.driver.find_elements(*HomeLocators.more_menu_elements)
    for element in menu_elements:
        page.move_to_element(element)
        assert "active" in element.get_attribute("class")


def test_33_dropdown_menu_appears_when_mouse_is_on_social_media_btn(driver):
    """check if drop down menu appears once mouse pointer is on "social media"("в соцсетях") menu button"""
    page = HomePage(driver)
    page.move_to_element(page.in_social_media_btn)
    assert page.driver.find_element(*HomeLocators.social_media_vk_link).is_displayed() is True


def test_34_all_found_books_have_image(driver):
    """check if all found books have images """
    page = HomePage(driver)
    page.search_field.send_keys("парап")
    page.search_btn.click()
    quantity_of_book_on_the_page = len(page.driver.find_elements(*HomeLocators.found_books))
    images = page.driver.find_elements(*HomeLocators.book_images)
    assert len(images) == quantity_of_book_on_the_page


def test_35_sort_by_low_price(driver):
    """Make sure that sort by low price works fine"""
    page = HomePage(driver)
    page.search_field.send_keys("парап")
    page.search_btn.click()
    page.driver.find_element(*HomeLocators.sort_by_btn).click()
    page.driver.find_element(*HomeLocators.sort_by_low_price).click()
    page.wait_page_loaded()
    prices = page.driver.find_elements(*HomeLocators.books_prices)
    all_prices = []
    for price in prices:
        all_prices.append(float(price.text.replace(' ', '')))
    assert all_prices == sorted(all_prices)


def test_36_sort_by_high_price(driver):
    """Make sure that sort by high price works fine"""
    page = HomePage(driver)
    page.search_field.send_keys("парап")
    page.search_btn.click()
    page.driver.find_element(*HomeLocators.sort_by_btn).click()
    page.driver.find_element(*HomeLocators.sort_by_high_price).click()
    page.wait_page_loaded()
    prices = page.driver.find_elements(*HomeLocators.books_prices)
    all_prices = []
    for price in prices:
        all_prices.append(float(price.text.replace(' ', '')))
    assert all_prices == sorted(all_prices, reverse=True)


def test_37_add_to_cart(driver):
    page = HomePage(driver)
    page.search_field.send_keys("парап")
    page.search_btn.click()
    page.driver.find_elements(*HomeLocators.add_to_cart_buttons)[1].click()  # first book - click "to cart"
    page.wait_page_loaded()
    assert "1" in page.driver.find_element(*HomeLocators.amount_in_cart).text
