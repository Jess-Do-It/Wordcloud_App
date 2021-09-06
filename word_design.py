from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image


def create_word_cloud(name):
    string = open("text/temp_words.txt", "r").read().lower()
    cloud = WordCloud(background_color = "white", max_words = 200, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("images/wordCloud.png")
