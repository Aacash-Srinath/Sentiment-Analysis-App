from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import torch

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def sentimentRating(review):
    tokens = tokenizer.encode(review, return_tensors='pt', truncation=True, max_length=512)
    result = model(tokens)
    rating = int(torch.argmax(result.logits)) + 1
    return (rating)
