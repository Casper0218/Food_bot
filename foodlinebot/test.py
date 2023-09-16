import torch
from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd
#import os

def model(other_data):
    # 指定模型和權重路徑
    model_path = "best_model.pth"

    # 初始化 Bert tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

    # 初始化模型
    model = BertForSequenceClassification.from_pretrained('bert-base-chinese')

    # 載入你的權重
    #print(os.getcwd())
    model.load_state_dict(torch.load(model_path))

    # 將模型移動到 GPU，如果 GPU 可用的話
    if torch.cuda.is_available():
        model.to('cuda')

    # 載入其他 CSV 檔案
    #other_csv_file = '茶六公益店100則評論.csv'
    #other_data = pd.read_csv(other_csv_file, encoding='utf-8-sig', encoding_errors='ignore')
    other_data['comment'].fillna('', inplace=True)

    comments = other_data['comment']
    
    # 將評論轉換為模型輸入格式
    def tokenize_comments(comments, tokenizer, max_length=128):
        input_ids = []
        attention_masks = []
    
        for comment in comments:
            encoded_dict = tokenizer.encode_plus(
                comment,
                add_special_tokens=True,
                max_length=max_length,
                padding='max_length',
                return_attention_mask=True,
                return_tensors='pt',
                truncation=True
            )
    
            input_ids.append(encoded_dict['input_ids'])
            attention_masks.append(encoded_dict['attention_mask'])
    
        return torch.cat(input_ids, dim=0), torch.cat(attention_masks, dim=0)
    
    input_ids, attention_masks = tokenize_comments(comments, tokenizer)
    
    # 將數據移動到 GPU，如果 GPU 可用的話
    if torch.cuda.is_available():
        input_ids, attention_masks = input_ids.to('cuda'), attention_masks.to('cuda')
    
    # 使用模型進行評估
    with torch.no_grad():
        model.eval()
        outputs = model(input_ids, attention_mask=attention_masks)
        predicted_probabilities = torch.softmax(outputs.logits, dim=1)  # 獲取預測概率
    
    # 將預測概率添加到原始 CSV 數據中
    other_data['predicted_prob_negative'] = predicted_probabilities[:, 0].cpu().numpy()
    other_data['predicted_prob_positive'] = predicted_probabilities[:, 1].cpu().numpy()
    
    # 保存結果到 CSV 文件，編碼為 'utf-8-sig'，包含 BOM，並忽略編碼錯誤
    #result_csv_file = '結果.csv'
    #other_data.to_csv(result_csv_file, index=False, encoding='utf-8-sig')
    
    #print(f"結果已保存到 {result_csv_file}，編碼為 'utf-8-sig'")
    return predicted_probabilities[:, 1].cpu().numpy().mean()
