from selenium.webdriver.common.by import By

from Features.pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    account_information_link_text = "Edit your account information"

    def status_of_account_information(self):
        return self.driver.find_element(By.LINK_TEXT,self.account_information_link_text).text.__eq__('Edit your account information')