import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

#driver = webdriver.Firefox()
# 通知の無効化
options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
driver = webdriver.Firefox(firefox_options=options)
driver.implicitly_wait(10)

url = "https://www.facebook.com"
driver.get(url)

email_elem = driver.find_element_by_name("email")
email_elem.send_keys("メールアドレス")
password_elem = driver.find_element_by_name("pass")
password_elem.send_keys("パスワード")
password_elem.submit()
time.sleep(2)

# 検索
input_keyword = driver.find_element_by_name("q")
input_keyword.send_keys("codecamp")
input_keyword.submit()
time.sleep(2)

# CodeCampの項目を確定
link = driver.find_element_by_link_text("CodeCamp")
link.click()
time.sleep(2)

# 自動スクロールダウン
#page = driver.find_element_by_tag_name("html")
#page.send_keys(Keys.END)

# 自動スクロール繰り返し
i = 1
scroll = 120

while i < scroll:
    try:
        print("\nループ開始：" + str(i) + "回目")
        page = driver.find_element_by_tag_name("html")
        page.send_keys(Keys.END)
        time.sleep(1.5)

    except:
        print("error...")

    finally:
        #element = driver.find_elements_by_class_name("_4-u2 _4-u8")
        #element = len(element)
        html = driver.page_source
        post = html.count("_4-u2 _4-u8")
        #print(html[0:200])
        print("ループOK: " + str(i) + "回目")
        print("投稿数:" + str(post))
        #file = open("facebook-html-" + str(i) + ".html", "w")
        #file.write(html)
        #file.close()
        
        i = i + 1

print("【ループ終了】" )
print("記事数:" + str(post))

x = re.findall(r'\brel="dialog">\w+', html)
print(x)
print("シェアのあった投稿数：" + str(len(x)))

# CSV用にデータ加工　1次元配列を 2次元配列に変換
import numpy as np
item = np.array(x)
item_count = len(x)
x = item.reshape(item_count,1)
print(x)
np.savetxt("fb_data.csv", x, delimiter = ",", fmt = "%s")