import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from collections import Counter

# 讀取CSV文件
df = pd.read_csv('茶六公益店100則評論.csv', encoding='utf-8')

# 將'comment'列的內容合併為一個字符串
comments = df['comment'].str.cat(sep=' ')

# 使用jieba分詞對文本進行分詞處理
word_list = jieba.cut(comments)

# 過濾停用詞
stop_words = ['的', '了', '是', '在', '我', '你', '也', '都', '或', '跟', '所以', '但', '而且','有','很','吃','人','不']  # 請替換成您的停用詞列表
filtered_words = [word for word in word_list if word not in stop_words]

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
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# 創建一個字詞計數器
word_counter = Counter(filtered_word_str)

# 取出出現次數最多的前10個字詞和它們的出現次數
top_10_words = word_counter.most_common(10)

# 打印結果
for word, count in top_10_words:
    print(f'{word}: {count}')
