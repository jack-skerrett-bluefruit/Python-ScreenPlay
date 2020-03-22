from selenium.webdriver.common.by import By


class blast_off:
    new_feature_button = (By.ID, "NewFeature")
    feature_list = (By.ID, "FeatureList")
    edit_feature_button = (By.XPATH, "//*[contains(@id,'EditFeature-')]")
