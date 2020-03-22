from selenium.webdriver.common.by import By


class nav_header:
    login_link  = (By.XPATH, "/html/body/app/div[2]/div[1]/a[1]")
    project_dropdown = (By.XPATH, "/html/body/app/div[2]/div[1]/div/div/select")
    project_dropdown_test_project = (By.XPATH, "/html/body/app/div[2]/div[1]/div/div/select/option[2]")
