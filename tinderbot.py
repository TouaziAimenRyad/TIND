from selenium import webdriver
from time import sleep
class TinderBot():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        conx_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        conx_btn.click()

      #  plusopt_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')

       # plusopt_btn.click()

        try:
          fb_btn = self.driver.find_element_by_xpath( '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
          fb_btn.click()
        except:
           try:
                plusopt_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
                plusopt_btn.click()
                fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[2]/span/div[3]/button')
                fb_btn.click()
           except:
               fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
               fb_btn.click()




        #switching to pop up window
        fb_btn.click()
        sleep(10)
        base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('touazi2001@outlook.com')
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys('lord2001')
        login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login.click()
        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
            like_btn = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
            like_btn.click()

    def dislike(self):
            dislike_btn = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
            dislike_btn.click()

    def auto_swipe(self):
            while True:
                sleep(0.5)
                try:
                    self.like()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        self.close_match()

    def close_popup(self):
            popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
            popup_3.click()

    def close_match(self):
            match_popup = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
            match_popup.click()





bot=TinderBot()
bot.login()

