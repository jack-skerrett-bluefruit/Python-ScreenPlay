from selenium.webdriver.common.by import By


class login_page:
    username_textbox = (By.ID, "Input_Email")
    password_textbox = (By.ID, "Input_Password")
    log_in_button = (By.XPATH, "//*[@id=\"account\"]/div[5]/button")
