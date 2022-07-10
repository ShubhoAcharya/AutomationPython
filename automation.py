from webbrowser import Chrome
from selenium import webdriver

Chrome_browser= webdriver.Chrome('./chromedriver')
Chrome_browser.maximize_window()
Chrome_browser.get("https://www.youtube.com/")
Chrome_browser.driver.find_element_by_class_name("style-scope ytd-searchbox")
