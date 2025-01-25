from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import os


things = ['https://rus-ege.sdamgia.ru/', 'https://inf-ege.sdamgia.ru/', 'https://mathb-ege.sdamgia.ru/', 'https://math-ege.sdamgia.ru/']
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def text_to_file(xpath):
    links = driver.find_elements('xpath', xpath)
    for link in links:
        with open('links.txt', 'a', encoding='utf-8') as file:
            file.write(f'{link.get_attribute("href")}\n')

# получение ссылок на варианты
def get_links():
    for thing in things:
        driver.get(thing)
        sleep(5)
        text_to_file('//a[@class="Link VariantLink OurVariants-Link"]')
        text_to_file('//a[@class="Link Link_black"]')
        if thing == 'https://math-ege.sdamgia.ru/':
            text_to_file('//a[@class="Link VariantLink LarinVariants-Link"]')

# переход на корневой каталог
def leave():
    pass
      
# получение задач из вариантов
def get_tasks():
    with open('links.txt', 'r', encoding='utf-8') as file:
        links = ''.join(file.readlines()).split('\n')
    for link in links:
        driver.get(link)
        sleep(5)
        tasks = driver.find_elements('xpath', '//div[@class="nobreak"]')
        for task in tasks:
            text = task.text.split('\n')
            text = '\n'.join([word for word in text if word != ''])
            with open('texts.txt', 'a', encoding='utf-8') as file:
                file.write(f'{text}\n')
    
get_tasks()