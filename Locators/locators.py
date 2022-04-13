from selenium.webdriver.common.by import By


class AuthFormLocators:
    auth_form = (By.CSS_SELECTOR, 'div.lab-modal-content')
    close_btn = (By.CSS_SELECTOR, 'form#auth-by-code>div.new-auth__close')
    phone_num_field = (By.CSS_SELECTOR, 'input[placeholder="Введите свой код скидки, телефон или эл.почту"]')
    enter_btn = (By.CSS_SELECTOR, 'input#g-recap-0-btn')
    agreement_check_box = (By.CSS_SELECTOR, 'label.new-auth__info')

    # another ways to enter locators
    another_ways_to_enter = (By.CSS_SELECTOR, 'a.js-show-soc')
    auth_social_links_box = (By.CSS_SELECTOR, 'div.new-auth__auth-social')
    vk_link = (By.CSS_SELECTOR, 'span.new-auth__auth-social_vk')
    ok_link = (By.CSS_SELECTOR, 'span.new-auth__auth-social_ok')
    mail_ru_link = (By.CSS_SELECTOR, 'span.new-auth__auth-social_mailru')
    yandex_link = (By.CSS_SELECTOR, 'span.new-auth__auth-social_yandex')
    gmail_link = (By.CSS_SELECTOR, 'span.new-auth__auth-social_gl')



    my_lab_btn = (By.CSS_SELECTOR, 'a.top-link-main_cabinet')
    log_out_btn = (By.CSS_SELECTOR, 'a.user-top-menu-link_logout')
    service_unavailable_help_message = (By.XPATH, '//small[contains(text(), "Сервис недоступен")]')

    # google auth
    google_email_field = (By.CSS_SELECTOR, 'input[type="email"]')
    google_password_field = (By.CSS_SELECTOR, 'input[type="password"]')
    google_email_passw_next_btn = (By.CSS_SELECTOR, 'button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ')


class HomeLocators:
    # -------------------main init locators
    # main header elements
    logo = (By.CSS_SELECTOR, 'span.b-header-b-logo-e-logo')
    search_field = (By.CSS_SELECTOR, 'input#search-field')
    search_btn = (By.CSS_SELECTOR, 'button[type="submit"]')
    notification_btn = (By.CSS_SELECTOR, 'a.top-link-main_notification')
    my_lab_btn = (By.CSS_SELECTOR, 'a.top-link-main_cabinet')
    put_order_btn = (By.CSS_SELECTOR, 'a.top-link-main_putorder')
    cart_btn = (By.CSS_SELECTOR, 'a.cart-icon-js')
    recommendations_link = (By.CSS_SELECTOR, 'a.b-header-b-logo-e-discount')
    games_menu_link = (By.CSS_SELECTOR, 'span>a[href="/games/"]')
    office_menu_link = (By.CSS_SELECTOR, 'span>a[href="/office/"]')

    # main menu
    books_menu_link = (By.CSS_SELECTOR, 'span>a[href="/books/"]')
    best_menu_link = (By.CSS_SELECTOR, 'span>a[href="/best/"]')
    school_menu_link = (By.CSS_SELECTOR, 'span>a[href="/school/"]')
    more_btn = (By.CSS_SELECTOR, 'li[data-toggle="header-more"]')
    club_menu_link = (By.CSS_SELECTOR, 'span>a[href="/club/"]')

    # additional menu links
    delivery_and_payment_link = (By.CSS_SELECTOR, 'li[data-event-label]>a[href="/help/"]')
    certificates_link = (By.CSS_SELECTOR, 'li[data-event-label]>a[href="/top/certificates/"]')
    rating_link = (By.CSS_SELECTOR, 'li[data-event-label]>a[href="/rating/?id_genre=-1&nrd=1"]')
    novelty_link = (By.CSS_SELECTOR, 'li[data-event-label]>a[href="/novelty/"]')
    sale_link = (By.CSS_SELECTOR, 'li[data-event-label]>a[href="/sale/"]')
    contact_link = (By.CSS_SELECTOR, 'li[data-event-content="Контакты"]>a[href="/contact/"]')
    support_link = (By.CSS_SELECTOR, 'li[data-event-label]>a[href="/support/"]')

    # social media buttons
    in_social_media_btn = (By.CSS_SELECTOR, 'a.b-labirint-all-social-network')

    notification_btn_popup_mess = (By.CSS_SELECTOR, 'div.b-header-login-e-enter>div.b-menu-list-title')
    my_lab_btn_popup_mess = (By.CSS_SELECTOR, 'div.b-header-login-action-logo-e-wrap')
    put_order_btn_mess = (By.CSS_SELECTOR, 'div.b-menu-list-title.font_regular.tac')
    cart_btn_mess_indicator = (By.CSS_SELECTOR, 'li.b-header-b-personal-e-list-item.have-dropdown.last-child')  # true
    # if it has "have-dropdown-selected" class in test_home_page test_07
    amount_in_cart = (By.CSS_SELECTOR, 'span.b-header-b-personal-e-wrapper-m-closed>span.basket-in-cart-a')  # .text

    # drop_down menus
    books_dropdown_menu = (By.CSS_SELECTOR, 'div#header-genres>div>ul')
    school_dropdown_menu = (By.CSS_SELECTOR, 'div.b-sub-menu-school-container')
    games_dropdown_menu = (By.CSS_SELECTOR, 'div#header-toys')
    office_dropdown_menu = (By.CSS_SELECTOR, 'div#header-office')
    more_dropdown_menu = (By.CSS_SELECTOR, 'div#header-more')
    club_dropdown_menu = (By.CSS_SELECTOR, 'div#header-club')
    social_media_vk_link = (By.CSS_SELECTOR, 'a[data-event-label="vk"]')

    # elements of drop_down menus (find_elementS)
    books_menu_elements = (By.CSS_SELECTOR, 'div#header-genres>div>ul>li.b-menu-second-item')
    games_menu_elements = (By.CSS_SELECTOR, 'div#header-toys>div>ul>li.b-menu-second-item')
    office_menu_elements = (By.CSS_SELECTOR, 'div#header-office>div>ul>li.b-menu-second-item')
    more_menu_elements = (By.CSS_SELECTOR, 'div#header-more>div>ul>li[class="b-menu-second-item"]')

    # search/found elements (find_elementS)
    found_books = (By.CSS_SELECTOR, 'div.product')
    book_images = (By.CSS_SELECTOR, 'a.cover>img')
    books_prices = (By.CSS_SELECTOR, 'span.price-val>span')
    add_to_cart_buttons = (By.XPATH, '//a[contains(text(), "В КОРЗИНУ")]')

    # sort by
    sort_by_btn = (By.CSS_SELECTOR, 'span.navisort-part-7')
    sort_by_low_price = (By.CSS_SELECTOR, 'span.navisort-part-7>span>span>span>ul>li>a[data-event-content="дешевые"]')
    sort_by_high_price = (By.CSS_SELECTOR, 'span.navisort-part-7>span>span>span>ul>li>a[data-event-content="дорогие"]')





