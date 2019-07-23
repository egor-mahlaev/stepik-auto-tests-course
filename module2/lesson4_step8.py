from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
)

browser.find_element(By.ID, "book").click()

x = browser.find_element(By.ID, "input_value").text
result = calc(x)

result_field = browser.find_element(By.ID, "answer")
result_field.send_keys(result)

browser.find_element(By.ID, "solve").click()

