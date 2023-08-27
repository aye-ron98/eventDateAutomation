from selenium.webdriver.common.by import By


class CalendarLocators:
    # about
    event_title_input = (By.XPATH, '//*[@id="yui_3_17_2_1_1693099828102_29805"]')
    event_info_btn = (By.XPATH, '//*[@id="block-6880ac79582955a662f5"]')
    publish_event_btn = (By.XPATH, '//*[@id="yui_3_17_2_1_1693099828102_30010"]/div[3]/div[3]/div[4]/input')

    # event start date
    start_date_btn = (By.XPATH, '//*[@id="yui_3_17_2_1_1693103160671_20926"]/span')
    calendar_body = (By.XPATH, '//*[@id="yui_3_17_2_1_1693103160671_17191"]/div/table')
    start_hour_input = (By.XPATH, '//*[@id="yui_3_17_2_1_1693103160671_20999"]')
    start_hour_minute = (By.XPATH, '//*[@id="yui_3_17_2_1_1693103160671_21127"]')
    start_AM_PM = (By.XPATH, '//*[@id="yui_3_17_2_1_1693103160671_17225"]/input[3]')

    # event end date


    # location
    event_location_btn = (By.XPATH, '//*[@id="yui_3_17_2_1_1693099828102_30010"]/div[1]/div[2]/div/div/div/div[3]')
    location_title_input = (By.XPATH, '//*[@id="yui_3_17_2_1_1693099828102_33406"]/input[1]')
    location_address_input = (By.XPATH, '//*[@id="yui_3_17_2_1_1693099828102_33296"]')
    location_city_input = (By.XPATH, '//*[@id="yui_3_17_2_1_1693099828102_33406"]/input[3]')
