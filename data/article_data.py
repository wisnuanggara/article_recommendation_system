import pandas as pd
from utils.custom_logging import set_logging

DATA_SOURCE = "https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv"

def get_article_data():
    data = pd.read_csv(DATA_SOURCE,encoding='latin1')
    set_logging("INFO","Get Article Data Success !")
    return data