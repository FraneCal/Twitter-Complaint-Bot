from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path = r"C:\Users\Zemmente\Desktop\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'stststst1231@outlook.com'
TWITTER_PASSWORD = 'In71948N'

# driver.get('https://www.speedtest.net/')
# time.sleep(3)
# go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
# go_button.click()
#
# time.sleep(40)
# download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]')
# upload_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]')
#
# print(download_speed.text)
# print(upload_speed.text)

driver.get("https://twitter.com/")
time.sleep(3)
log_in_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a')
log_in_button.click()

time.sleep(3)
#base_window = driver.window_handles[0]
#twitter_login_window = driver.window_handles[1]

#driver.switch_to.window(twitter_login_window)
email = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
email.click()
email.send_keys(TWITTER_EMAIL)
next_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
next_button.click()

time.sleep(2)
password = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.click()
password.send_keys(TWITTER_PASSWORD)
sign_in = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
sign_in.click()

time.sleep(6)
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)

new_cookies = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
new_cookies.click()
time.sleep(2)
write_a_tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
write_a_tweet.click()
# write_a_tweet.send_keys(f'Hey internet provider, why is my internet speed {download_speed.text}down/{upload_speed.text}up when I pay for 150down/10up?')
write_a_tweet.send_keys('Hey')


# class InternetSpeedTwitterBot:
#
#     def __init__(self):
#         self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
#         self.up = 0
#         self.down = 0
#
#     def get_internet_speed(self):
#         self.driver.get("twitter.com")
#         time.sleep(2)
#         go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
#         go_button.click()
#
#     def tweet_at_provider(self):
#         pass

# bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
# bot.tweet_at_provider()
