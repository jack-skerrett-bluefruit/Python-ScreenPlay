from selenium.webdriver.common.by import By


class feature_modal:
    title_textbox = (By.ID, "feature-name")
    description_textbox = (By.ID, "description")
    save_button = (By.XPATH, "/html/body/app/div[3]/div[2]/div/div/div/button[1]")
