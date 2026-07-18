import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

url='https://app.100daysofpython.dev/services/share-a-naan/welcome'
similar_account='target username'
username='your@gmail.com'
passw='yourpass'

class InstaFollower:
    def __init__(self):
        self.driver=webdriver.Chrome()

    def login(self):
        self.driver.get(url)
        time.sleep(2)
        emailbut = self.driver.find_element(By.XPATH, value='/html/body/div/aside/div/form/input[1]')
        emailbut.send_keys(username)
        passbut = self.driver.find_element(By.XPATH, value='/html/body/div/aside/div/form/input[2]')
        passbut.send_keys(passw , Keys.ENTER)
        popup= self.driver.find_element(By.XPATH, value='//*[@id="popup-save-login"]/div/div[2]')
        popup.click()
        popup2= self.driver.find_element(By.XPATH, value='//*[@id="popup-notifications"]/div/button[2]')
        popup2.click()


    def find_followers(self):
        search_but= self.driver.find_element(By.XPATH, value='/html/body/div[1]/nav/button')
        search_but.click()
        search_bar = self.driver.find_element(By.XPATH, value='/html/body/aside/div[2]/input')
        search_bar.click()
        search_bar.send_keys(similar_account)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        
        wait = WebDriverWait(self.driver, 10)
        followers = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a')))
        followers.click()
        time.sleep(1)

        scrollable_div = self.driver.find_element(By.CLASS_NAME, value='followers-scroll')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
            time.sleep(1)

        

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, value="//button[text()='Follow']")
        
        for button in follow_buttons:
            try:
                self.driver.execute_script("arguments[0].click();", button)
                time.sleep(1)
            except:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div/button[2]')
                self.driver.execute_script("arguments[0].click();", cancel_button)
                time.sleep(1)



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
