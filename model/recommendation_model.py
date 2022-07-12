import pandas as pd
import numpy as np
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
from utils.custom_logging import set_logging
from data.article_data import get_article_data

def create_recommendation_model():
    data = get_article_data()
    articles = data["Article"].tolist()
    uni_tfidf = text.TfidfVectorizer(input=articles, stop_words="english")
    uni_matrix = uni_tfidf.fit_transform(articles)
    uni_sim = cosine_similarity(uni_matrix)
    return uni_sim, data

def recommend_articles(x, data):
    return ", ".join(data["Title"].loc[x.argsort()])

