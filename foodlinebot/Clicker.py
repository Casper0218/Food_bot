# 載入需要的套件
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def clicker(storename):

    # 開啟瀏覽器視窗(Chrome)
    driver = webdriver.Chrome()

    #前往目標網頁google地圖
    driver.get('https://www.google.com.tw/maps')

    #暫停1秒鐘等網頁開好
    time.sleep(1)

    # 定位搜尋框
    searchbox = driver.find_element(By.ID, 'searchboxinput')
    # searchbox = driver.find_element_by_css_selector('[role="combobox"]') #Google首頁的搜尋框供參考

    # 填入關鍵字
    searchbox.send_keys(storename)

    # 模拟按下ENTER键执行搜索
    searchbox.send_keys(Keys.RETURN)

    # # 等待第一個店家元素被定位並可點擊
    # first_restaurant = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div:nth-child(3) > div > a'))
    # )

    # # 點擊第一個店家元素
    # first_restaurant.click()

    # 等待一段时间以确保頁面加载完成
    time.sleep(5)  # 可以根据实际情况调整等待时间, 如果沒等到網頁開完，會按不到想要的按鈕

    # 找到"更多評論"按鈕
    # classMoreReview = "button.M77dve" 
    # MoreReviewBtn = driver.find_elements_by_css_selector(classMoreReview) #舊版webdriver用
    # MoreReviewBtn = driver.find_elements(By.CSS_SELECTOR, classMoreReview)

    #點擊"更多評論"按鈕
    # MoreReviewBtn[2].click()

    #time.sleep(5) #用這段暫停的時間；瘋狂地用手上的滑鼠捲動畫面，叫進更多的評論

    #印出目前頁面網址
    current_url = driver.current_url

    #print(current_url)

    #用評論文字的class去尋找目前頁面裡已經叫進來的所有評論文字，但是會連商家的回應一起抓下來
    #class_review= "wiI7pd"
    #review = driver.find_elements(By.CLASS_NAME, class_review)
    #for review in review:
    #    print(review.text)
        
    # 最後，關閉瀏覽器
    driver.quit()
    return current_url
