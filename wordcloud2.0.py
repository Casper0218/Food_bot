import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from collections import Counter

# 讀取CSV文件
df = pd.read_csv('紅茶巴士 台中重慶站-結果.csv', encoding='utf-8')

# 根据predicted_prob_positive的值分成两组评论
positive_comments = df[df['predicted_prob_positive'] > 0.5]['comment'].str.cat(sep=' ')
negative_comments = df[df['predicted_prob_positive'] < 0.5]['comment'].str.cat(sep=' ')

# 使用jieba分詞對文本進行分詞處理
positive_word_list = jieba.cut(positive_comments)
negative_word_list = jieba.cut(negative_comments)

# 過濾單一個字的詞語
filtered_positive_words = [word for word in positive_word_list if len(word) > 1]
filtered_negative_words = [word for word in negative_word_list if len(word) > 1]

# 將過濾後的分詞結果轉為空格分隔的字符串
filtered_positive_word_str = ' '.join(filtered_positive_words)
filtered_negative_word_str = ' '.join(filtered_negative_words)

# 使用正則表達式去除標點符號
filtered_positive_word_str = re.sub(r'[^\w\s]', '', filtered_positive_word_str)
filtered_negative_word_str = re.sub(r'[^\w\s]', '', filtered_negative_word_str)

# 創建文字雲，不指定字體文件路徑，使用系統默認字體
positive_wordcloud = WordCloud(
    font_path='C:/Windows/Fonts/msjh.ttc',  # 微軟正黑體的文件路徑
    background_color='white',
    width=800,
    height=400,
).generate(filtered_positive_word_str)

negative_wordcloud = WordCloud(
    font_path='C:/Windows/Fonts/msjh.ttc',  # 微軟正黑體的文件路徑
    background_color='white',
    width=800,
    height=400,
).generate(filtered_negative_word_str)

# 顯示文字雲
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.title('+')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.title('-')
plt.axis('off')
# plt.show()
plt.savefig('文字雲.png')
