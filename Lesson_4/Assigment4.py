from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 1
driver_chrome = webdriver.Chrome(service=Service("C:/Users/zhada/Downloads/chromedriver_win32/chromedriver.exe"))
driver_firefox = webdriver.Firefox(service=Service("C:/Users/zhada/Downloads/geckodriver-v0.31.0-win64/geckodriver.exe"))
driver_chrome.implicitly_wait(10)
driver_firefox.implicitly_wait(10)
driver_chrome.get("http://www.walla.co.il")
driver_firefox.get("http://www.ynet.co.il")

# 2
website_title = driver_chrome.title  # a
driver_chrome.refresh()  # b
website_title2 = driver_chrome.title  # c
print(website_title == website_title2)

# 3 - Yes.

# 4
driver_chrome.get("https://translate.google.co.il")
driver_chrome.find_element(by=By.CLASS_NAME, value="er8xn").send_keys("שלום")

# 5
driver_chrome.get("https://www.youtube.com/")
search_box = driver_chrome.find_element(by=By.XPATH, value="/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_box.send_keys("עקיבא - יש בך הכל")
search_button = driver_chrome.find_element(by=By.ID, value="search-icon-legacy")
search_button.click()

# 6
driver_chrome.get("https://translate.google.com/")
text_field1 = driver_chrome.find_element(by=By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
text_field2 = driver_chrome.find_element(by=By.CLASS_NAME, value="er8xn")
text_field3 = driver_chrome.find_element(by=By.XPATH, value="//textarea[@aria-autocomplete='list']")
print(text_field1 == text_field2 == text_field3)
print(text_field1)

# 7
driver_chrome.get("https://www.facebook.com/")
user_name = driver_chrome.find_element(by=By.NAME, value="email")
user_name.send_keys("my email address or phone number")
password = driver_chrome.find_element(by=By.NAME, value="pass")
password.send_keys("my password")
login_button = driver_chrome.find_element(by=By.NAME, value="login")
login_button.click()

# 8
driver_chrome.get("https://www.lessin.co.il/")
cookies_list = driver_chrome.get_cookies()
print("cookies list =", len(cookies_list), ":", cookies_list)
driver_chrome.delete_all_cookies()
cookies_new_list = driver_chrome.get_cookies()
print("cookies list =", len(cookies_new_list), ":", cookies_new_list)

# 9
driver_chrome.get("https://github.com/")
search_textfield = driver_chrome.find_element(by=By.XPATH, value="/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
search_textfield.send_keys("Selenium")
search_textfield.send_keys(Keys.ENTER)

driver_chrome.quit()
driver_firefox.quit()
