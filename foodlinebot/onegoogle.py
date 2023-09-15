import re
import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .gotourl import *

def tmd(url):

    # Define the XPath
    xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]'

    # Configure the WebDriver with proxy settings and run it in headless mode
    chrome_options = webdriver.ChromeOptions()

    ######uncomment when deploy to Linux Ubuntu 22
    #chrome_options.add_argument('--headless')  # Run headless browser
    #chrome_options.add_argument('--no-sandbox')  # Required for Linux servers
    #chrome_options.add_argument('--disable-dev-shm-usage')  # Required for Linux servers
    #service = Service(executable_path=ChromeDriverManager().install())
    ######uncomment whe deploy to Linux Ubuntu 22
    
    # Initialize the WebDriver with selenium-wire
    #print('Opening chrome')
    driver = webdriver.Chrome(#service=service,       #executable_path='/path/to/chromedriver', 
        options=chrome_options
        )  # Replace with the actual path

    # Open a webpage
    #start = time.time()
    #url = 'https://www.google.com/maps/place/%E8%B6%85%E5%90%89%E9%A3%AF%E6%A1%B6-%E5%B7%A5%E5%AD%B8%E5%BA%97/@24.1171034,120.6569651,17z/data=!4m8!3m7!1s0x34693c50d802033b:0xd54cd319a0c199b8!8m2!3d24.1171034!4d120.65954!9m1!1b1!16s%2Fg%2F11xlgm6bn?entry=ttu'  # Replace with the target website URL
    #url=storeurl
    driver.get(url)
    #print('goto website')
    Current_url=driver.current_url
    driver.get(gotourl(Current_url))
    # Wait for the page to load (adjust the waiting time as needed)
    #time.sleep(5)
    scrolltimes=0
    #print(scrolltimes)
    gotit=False
    # Find the scrollable element using XPath
    scrollable_element = driver.find_element(By.XPATH, xpath)

    #print('Find listen')
    while scrolltimes <10:
        if gotit:
            break
            scrolltimes=10
        else:
            requests = driver.requests

            # Extract request URLs
            request_urls = [request.url for request in requests]

            # Print request URLs
            for url in request_urls:
                if re.search('listen',url):
                    gotit=True
                    goodurl=url
                    print(url)
                    break

            # Scroll down to the specified element
            scrollable_element.send_keys(Keys.PAGE_DOWN)
    #        scrolltimes+=1
    #        print(scrolltimes)
    #time.sleep(5)  # Adjust the sleep duration as needed
    #end=time.time()
    #print(end-start)
    # Capture network traffic

    # Quit the WebDriver
    driver.quit()
    #print('chrome closed')
    #end = time.time()
    #print(end - start)

    #引入函式庫
    import requests
    import json
    import pandas as pd

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


    # 代理伺服器
    proxies = {
        "http": "47.243.17.210:8088"
    }

    good=goodurl.split('2i103e1')
    # 超連結 幾個 url 各代表不同的評論條。
    #url = 'https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758546651144975!2y6093113884180453713!2m1!2i10!3e1!4m5!3b1!4b1!6b1!7b1!20b1!5m2!1sJPLxZPmPEITx-Qa51rWQAg!7e81'
    # 誠品 站前店 共有 4821 則評論
    #prefix = 'https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758546651144975!2y6093113884180453713!2m1!'
    prefix=good[0]
    number = '2i2003e2'
    #suffix = '!3e2!4m5!3b1!4b1!6b1!7b1!20b1!5m2!1sJPLxZPmPEITx-Qa51rWQAg!7e81'
    suffix=good[1]
    #url = 'https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758546651144975!2y6093113884180453713!2m1!2i100!3e1!4m5!3b1!4b1!6b1!7b1!20b1!5m2!1sJPLxZPmPEITx-Qa51rWQAg!7e81'
    url = prefix+number+suffix
    # 發送get請求
    text = requests.get(url,headers=headers,proxies=proxies,verify=False).text

    # 取代掉特殊字元，這個字元是為了資訊安全而設定的喔。
    pretext = ')]}\''
    text = text.replace(pretext,'')
    # 把字串讀取成json
    soup = json.loads(text)

    #讀出soup的結構
    my_list = soup
    enumerate(my_list)
    #for index, item in enumerate(my_list):
    #    print(f"Index {index}: {item}")

    # 取出包含留言的List 。
    conlist = soup[2]

    #print('最多一次能下載',len(conlist), '則評論')
    RES='下載了 '+str(len(conlist))+' 則評論'
    comment=[]
    for i in conlist:
        comment+=[i[3]]

    df=pd.DataFrame(comment,columns=['comment'])
    df.to_csv('store.csv')
    return RES
