from utils.custom_logging import set_logging
from data.article_data import get_article_data
from model.recommendation_model import create_recommendation_model, recommend_articles

if __name__ == '__main__':
    set_logging('INFO', 'Application started...')
    uni_sim, data = create_recommendation_model()
    data["Recommended Articles"] = [recommend_articles(x, data) for x in uni_sim]
    print(data)
    set_logging('INFO', 'Application terminated...')





