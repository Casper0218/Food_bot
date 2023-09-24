import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
def numtoint(num):
    if  num< 1.5:
        output=1
    else:
        output=round(num)
    return output
#from collections import Counter

# 讀取CSV文件
def my_wordcloud(df, score, star):
    #df = pd.read_csv('結果.csv', encoding='utf-8')

    # 將'comment'列的內容合併為一個字符串
    comments = df['comment'].str.cat(sep=' ')

    # 使用jieba分詞對文本進行分詞處理
    word_list = jieba.cut(comments)

    # 過濾單一個字的詞語
    filtered_words = [word for word in word_list if len(word) > 1]

    # 將過濾後的分詞結果轉為空格分隔的字符串
    filtered_word_str = ' '.join(filtered_words)

    # 使用正則表達式去除標點符號
    filtered_word_str = re.sub(r'[^\w\s]', '', filtered_word_str)

    # 創建文字雲，不指定字體文件路徑，使用系統默認字體
    wordcloud = WordCloud(
        font_path='C:/Windows/Fonts/msjh.ttc',  # 微軟正黑體的文件路徑
        background_color='white',
        width=800,
        height=400,
    ).generate(filtered_word_str)

    # 顯示文字雲
    #fig.savefig('output.png')
    
    #plt.figure(figsize=(10, 5))
    
    smilescore=numtoint(score*5)
    googlestar=numtoint(star)
    # print(f'g{googlestar}m{smilescore}')

    smilepath='media/g'+str(googlestar)+'m'+str(smilescore)+'.png'
    #smile=plt.imread(smilepath)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, #interpolation='bilinear'
               )
    plt.axis('off')
    #plt.show()
    wordcloudpath='media/wordcloud.png'
    plt.savefig(wordcloudpath)    
    
    #plt.show()
    # Create a new figure
    
    from PIL import Image

    # Open the two input PNG files
    #image1 = Image.open(smilepath)
    #image2 = Image.open(wordcloudpath)
    image1 = Image.open(wordcloudpath)
    image2 = Image.open(smilepath)

    # Get the dimensions of the first image
    width1, height1 = image1.size

    # Get the dimensions of the second image
    width2, height2 = image2.size

    # Calculate the total width and height for the combined image
    #total_width = width1 + width2
    #max_height = max(height1, height2)
    total_width = max(width1, width2)
    max_height = height1 + height2

    # Create a new blank image with the calculated dimensions
    combined_image = Image.new('RGB', (total_width, max_height))

    # Paste the first image onto the combined image at the leftmost position
    combined_image.paste(image1, (0, 0))

    # Paste the second image next to the first image
    #combined_image.paste(image2, (width1, 0))
    combined_image.paste(image2, (0, height1))
    # Save the combined image as a new PNG file
    combined_image.save('media/文字雲.png')

    # Close the input images
    image1.close()
    image2.close()

    #print("Images combined and saved as 'combined_image.png'.")

    print("Images combined and saved as 'media/文字雲.png'.")

# 創建一個字詞計數器
#word_counter = Counter(filtered_word_str)

# 取出出現次數最多的前10個字詞和它們的出現次數
#top_10_words = word_counter.most_common(10)

# 打印結果
#for word, count in top_10_words:
#    print(f'{word}: {count}')
