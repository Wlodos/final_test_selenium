import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from Locators.locators import AuthFormLocators
from pages.auth_page import AuthPage


def test_01_auth_page_is_opened(driver):
    """check if authorisation page is opened"""
    page = AuthPage(driver)
    assert page.get_relative_link() == "/cabinet"


def test_02_enter_button_is_disabled_when_phone_num_field_isnt_filed(driver):
    """check if enter button isn't clickable while the phone number field isn't filled"""
    page = AuthPage(driver)
    page.phone_num_field.clear()
    assert page.enter_btn.get_attribute("disabled") == "true"


def test_03_enter_button_is_enabled_when_phone_num_field_is_filed(driver):
    """check if enter button is clickable when the phone number field is filled"""
    page = AuthPage(driver)
    page.enter_phone_number("+73234567890")
    assert page.enter_btn.get_attribute("disabled") is None


def test_04_help_message_appears_when_entered_phone_num_is_wrong(driver):
    """check if help message appears when entered phone number is wrong"""
    page = AuthPage(driver)
    page.enter_phone_number("+72234567890")
    page.enter_btn.click()
    assert driver.find_element(*AuthFormLocators.service_unavailable_help_message).is_displayed() is True


def test_05_all_auth_btn_and_links_are_disabled_when_agreement_checkbox_is_turned_off(driver):
    """check if there is no ways to be authorised when agreement checkbox is turned off"""
    page = AuthPage(driver)
    page.enter_phone_number("+71134567890")
    page.another_ways_to_enter_bnt_click()
    page.agreement_check_box.click()
    assert page.enter_btn.get_attribute("value") == "Необходимо принять соглашение" and \
           "disabled-block" in page.auth_social_links_box.get_attribute("class")


def test_06_auth_social_links_are_displayed_once_another_ways_to_enter_btn_clicked(driver):
    """check if all authorisation social links are displayed after "Другие способы входа" btn is clicked """
    page = AuthPage(driver)
    page.another_ways_to_enter_bnt_click()
    assert page.auth_social_links_box.is_displayed() is True


def test_07_close_btn_closes_auth_form(driver):
    """check if close_btn can close the authorisation for"""
    page = AuthPage(driver)
    page.close_btn.click()
    assert page.auth_form.is_displayed() is False


def test_08_vk_auth_link_opens_vk_auth_page(driver):
    """check if vk authorisation page is opened by clicking vk_auth_link"""
    page = AuthPage(driver)
    page.another_ways_to_enter_bnt_click()
    page.vk_link.click()
    assert "vk.com" in page.driver.current_url


def test_09_ok_auth_link_opens_ok_auth_page(driver):
    """check if ok authorisation page is opened by clicking ok_auth_link"""
    page = AuthPage(driver)
    page.another_ways_to_enter_bnt_click()
    page.ok_link.click()
    assert "ok.ru" in page.driver.current_url


def test_10_mail_ru_auth_link_opens_mail_ru_auth_page(driver):
    """check if mail.ru authorisation page is opened by clicking mailru_auth_link"""
    page = AuthPage(driver)
    page.another_ways_to_enter_bnt_click()
    page.mail_ru_link.click()
    assert "mail.ru" in page.driver.current_url


def test_11_yandex_auth_link_opens_yandex_auth_page(driver):
    """check if yandex authorisation page is opened by clicking yandex_auth_link"""
    page = AuthPage(driver)
    page.another_ways_to_enter_bnt_click()
    page.yandex_link.click()
    assert "yandex.ru" in page.driver.current_url


def test_12_gmail_auth_link_opens_gmail_auth_page(driver):
    """check if gmail authorisation page is opened by clicking gmail_auth_link"""
    page = AuthPage(driver)
    page.another_ways_to_enter_bnt_click()
    page.gmail_link.click()
    assert "accounts.google.com" in page.driver.current_url


def test_13_authorisation_via_google(driver):
    """check user can be authorised via google"""
    page = AuthPage(driver)
    page.another_ways_to_enter_bnt_click()
    page.gmail_link.click()
    page.driver.find_element(*AuthFormLocators.google_email_field).send_keys("ssotest194@gmail.com")
    page.driver.find_element(*AuthFormLocators.google_email_passw_next_btn).click()
    password = WebDriverWait(driver, 5).until(ec.element_to_be_clickable(AuthFormLocators.google_password_field))
    password.send_keys("Test@test123")
    page.driver.find_element(*AuthFormLocators.google_email_passw_next_btn).click()
    ActionChains(driver).move_to_element(page.driver.find_element(*AuthFormLocators.my_lab_btn)).perform()
    assert page.driver.find_element(*AuthFormLocators.log_out_btn).is_displayed() is True




















