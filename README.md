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
2. Create a LINE developer Messaging API:
   1. LINE Channel seret (You can find it on 'Basic settings' in your
      LINE developer console.)
   2. LINE Channel access token (You can find it on 'Messaging API
      settings' in your LINE developer console.)
   3. Setting Webhook URL on your 'Messaging API settings' page.
      Webhook URL: `https://[Your.Server.Link]/foodlinebot/callback`
   4. Create a file `line_bot_config.py` which contains:
      ```python
        # Put this file in 'mylinebot' project folder
        LINE_CHANNEL_ACCESS_TOKEN="[Copy your 'channel access token' here]"
        LINE_CHANNEL_SECRET="[Copy your 'channel secret' here]"
      ```
3. A specifc version of chromedriver.exe was needed to match the
   version of Google Chrome on your system.
4. After clone this project, you need download the model file
   `best_model.pth` from this link:
   https://drive.google.com/file/d/1CI8k02VDCZHxhzl74kT4-sF9Tj2PIg9R/view?usp=sharing
   , and put this file in `Food_bot` folder.
5. Using command line prompt to install dependencies.
   ```bash
   pip install -r "requirements.txt"
   ```
## Related Works

## Proposed Design

## Experiment

## Conclusion

# Food_bot

## Introduction
### Summary
### Installation

## Related Works

## Proposed Design

## Experiment

## Conclusion
