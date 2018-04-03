from selenium import webdriver
import webbrowser
import random
import os

USER = "おれさま"

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

shindan_view_page = "https://shindanmaker.com/c/list?mode=hot"
browser.get(shindan_view_page)
print("診断一覧ページにアクセスしました")

elements = browser.find_elements_by_class_name("list_title")
shindan_pages = []

for e in elements:
    shindan_pages.append(e.get_attribute('href'))

shindan_page = random.choice(shindan_pages)
browser.get(shindan_page)
print("診断ページにアクセスしました")

with open('shindan_page.html', 'w', encoding='utf-8') as f:
    f.write(browser.page_source)

e = browser.find_element_by_name("u")
e.clear()
e.send_keys(USER)

frm = browser.find_element_by_id("shindan_submit")
frm.submit()
print("情報を入力してログインボタンを押しました")

with open('shindan_result_page.html', 'w', encoding='utf-8') as f:
    f.write(browser.page_source)

path_to_page = os.path.dirname(__file__)
webbrowser.open_new_tab('file://' + path_to_page + '/shindan_result_page.html')

