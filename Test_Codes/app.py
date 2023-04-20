import select
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import pytest
from Test_Locators import locators
from Test_Data import data

class Test_code1:
    @pytest.fixture
    def booting_function(self):
          self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
          self.driver.get(data.Amazon_data().url)
          self.driver.maximize_window()
          self.driver.implicitly_wait(10)
        


    def test_search(self, booting_function):
        #self.driver.find_element(by=By.XPATH, value=locators.Amazon_Locators().serchbar).send_keys(data.Amazon_data.serch_name)
        self.driver.find_element(by=By.XPATH, value=locators.Amazon_Locators().serchbar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Amazon_Locators().laptop).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Amazon_Locators().pricevalue).click()

    def test_selcting(self, booting_function):
         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
         self.driver.find_element(by=By.XPATH, value=locators.Amazon_Locators().slect_Laptop).click()
         sleep(5)
         self.driver._switch_to.window(self.driver.window_handles[1])
         sleep(5)
         self.driver.find_element(by=By.XPATH, value=locators.Amazon_Locators().addtocart).click()
         sleep(5)
         self.driver.refresh()
         self.driver.find_element(by=By.XPATH,value=locators.Amazon_Locators().cart).click()
         self.driver.find_element(by=By.XPATH,value=locators.Amazon_Locators().quantity).click()
         self.driver.find_element(by=By.XPATH,value=locators.Amazon_Locators().Quantity).click()
         sleep(5)
         self.driver.find_element(by=By.XPATH,value=locators.Amazon_Locators().delete).click()
         self.driver.refresh()
         self.driver.close()
         
