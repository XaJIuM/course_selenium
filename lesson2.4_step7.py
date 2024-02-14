from selenium.webdriver.common.by import By                            # Используем для работы с элементами "By"
from selenium.webdriver.support.ui import WebDriverWait                # Используем для работы с явными ожиданиями
from selenium.webdriver.support import expected_conditions as EC       # Используем еще один инструмент для работы с явными ожиданиями
from selenium import webdriver                                         # Используем для работы с Selenium                     
import time                                                            # Скачиваем библиотеку для работы со временем и датами

# Переменные
link = "http://suninjuly.github.io/wait2.html"

try:     
    browser = webdriver.Chrome()                                                                      # Открываем браузер     
    browser.get(link)                                                                                 # Переходим по ссылке(В данном случае по переменной)                                                   
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify"))).click()   # Говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной и кликаем по ней                                                                          
    message = browser.find_element(By.ID, "verify_message")                                           # Находим появившийся текст и фиксируем в переменной "message"
    assert "successful" in message.text                                                               # Проверяем что в тексте переменной "message", присутствует слово "successful"
    button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, "verify")))       # Говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной

finally:
    time.sleep(10)                                                       # Устанавливаем задержку 30 сек перед закрытием браузера
    browser.quit()                                                       # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!