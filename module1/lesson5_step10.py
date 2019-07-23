from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Код, который заполняет обязательные поля
# Код, который заполняет обязательное поле Имя*
name = browser.find_element_by_css_selector(".first_block .first")
name.send_keys("TestName")
# Код, который заполняет обязательное поле Фамилия*
second_name = browser.find_element_by_css_selector(".first_block .second")
second_name.send_keys("TestSecondName")
# Код, который заполняет обязательное поле Email*
email = browser.find_element_by_css_selector(".first_block .third")
email.send_keys("TestEmail@gmail.com")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# Ждем загрузки страницы
time.sleep(1)
# Находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# Записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text
# Проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

