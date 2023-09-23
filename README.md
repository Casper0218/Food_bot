# Food_bot

This manual is for [我們的專題] version [我不知道第幾版].

   Copyright © 2023 AI人工智慧與數據分析班 第二組

     Permission is granted to copy, distribute and/or modify this
     document under the terms of the GNU Free Documentation License,
     Version 1.3 or any later version published by the Free Software
     Foundation; with no Invariant Sections, with the Front-Cover Texts
     being “A GNU Manual,” and with the Back-Cover Texts as in (a)
     below.  A copy of the license is included in the section entitled
     “GNU Free Documentation License.”

     (a) The FSF’s Back-Cover Text is: “You have the freedom to copy and
     modify this GNU manual.”

## Introduction

### Summary
### Installation
#### Prepared
1. Anaconda or miniconda evironment
   ```bash
   conda create -n [your_env_name] python==3.8
   ```
2. Create a [LINE Developers](https://developers.line.biz/zh-hant/) Messaging API:
   1. LINE Channel seret (You can find it on 'Basic settings' in your
      LINE Developers console.)
   2. LINE Channel access token (You can find it on 'Messaging API
      settings' in your LINE Developers console.)
   3. Setting Webhook URL on your 'Messaging API settings' page.
      Webhook URL: `https://[Your.Server.Link]/foodlinebot/callback`
   4. Create a file `line_bot_config.py` which contains:
       ```python
       # Put this file in 'mylinebot' project folder
       from .settings import ALLOWED_HOSTS
       LINE_CHANNEL_ACCESS_TOKEN="[Copy your 'channel access token' here]"
       LINE_CHANNEL_SECRET="[Copy your 'channel secret' here]"
       domainname='Your.Server.Link'
       ALLOWED_HOSTS += [domainname]
	    ```
      Please confirm the link of server is within single quotes.
3. A specifc version of chromedriver.exe was needed to match the
   version of Google Chrome on your system.
4. After clone this project, you need download the model file
   `best_model.pth` from this link:
   https://drive.google.com/file/d/1CI8k02VDCZHxhzl74kT4-sF9Tj2PIg9R/view?usp=sharing
   , and save this file in `Food_bot` folder.
5. Using command line prompt to install dependencies.
   ```bash
   conda activate [your_env_name]
   pip install -r "requirements.txt"
   ```
6. Save `line_bot_config.py` (step 2.4) in subfolder `mylinebot`.
7. Make sure your server domain name is in `ALLOWED_HOSTS` list in
   `line_bot_config.py`.
## Related Works

## Proposed Design

## Experiment

## Conclusion

# Food_bot

This manual is for [我們的專題] version [我不知道第幾版].

   Copyright © 2023 AI人工智慧與數據分析班 第二組

     Permission is granted to copy, distribute and/or modify this
     document under the terms of the GNU Free Documentation License,
     Version 1.3 or any later version published by the Free Software
     Foundation; with no Invariant Sections, with the Front-Cover Texts
     being “A GNU Manual,” and with the Back-Cover Texts as in (a)
     below.  A copy of the license is included in the section entitled
     “GNU Free Documentation License.”

     (a) The FSF’s Back-Cover Text is: “You have the freedom to copy and
     modify this GNU manual.”

## 前言

### 簡介
### 安裝指引
#### 事先準備
1. 請準備 Anaconda 或 miniconda 開發環境，可輸入下列指令新增新環境：
   ```bash
   conda create -n [your_env_name] python==3.8
   ```
2. 申請 [LINE Developers](https://developers.line.biz/zh-hant/) 的 Messaging API 頻道並且:
   1. 取得 LINE Channel seret (你可以在你的 LINE Developers console 中
      的 'Basic settings' 頁面裡找到)
   2. LINE Channel access token (你可以在你的 LINE Developers console
      中的 'Messaging API settings' 頁面裡找到)
   3. 在 'Messaging API settings' 頁面中設定 Webhook URL:
      Webhook URL: `https://[Your.Server.Link]/foodlinebot/callback`
   4. 新增檔名為 `line_bot_config.py` 的檔案，檔案裡寫入下列內容:
       ```python
	    # Put this file in 'mylinebot' project folder
	    from .settings import ALLOWED_HOSTS
	    LINE_CHANNEL_ACCESS_TOKEN="[Copy your 'channel access token' here]"
	    LINE_CHANNEL_SECRET="[Copy your 'channel secret' here]"
	    domainname='Your.Server.Link'
       ALLOWED_HOSTS += [domainname]
	    ```
	  請確認主機連結位址在單引號內。
3. 需要有與主機裡 Google Chrome 版本相應的 chromedriver.exe。
4. After clone this project, you need download the model file 從 Git
   下載此專案後，你還需要從這個 Googlr drive 連結
   https://drive.google.com/file/d/1CI8k02VDCZHxhzl74kT4-sF9Tj2PIg9R/view?usp=sharing
   額外下載`best_model.pth`，並儲存在專案資料夾 `Food_bot` 中。
5. 使用命令提示字元或其它指令式的 shell 中，移動工作目錄到 `Food_bot` 下，並輸入下面的指令來下載相依套件:
   ```bash
   pip install -r "requirements.txt"
   ```
6. 將在步驟 2.4 建立的 `line_bot_config.py` 檔案複製到專案子目錄 `mylinebot` 下。
7. 確認主機所使用的域名紀錄在步驟 2.4 建立的 `line_bot_config.py`中。
## Related Works

## Proposed Design

## Experiment

## Conclusion
