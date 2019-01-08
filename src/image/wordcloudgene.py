#!/usr/bin/env python
#coding=utf-8

from wordcloud.wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from PIL import Image
import jieba
import codecs
import numpy as np
from collections import Counter

def generate_word_cloud(world_file):
    text = codecs.open(world_file,encoding = 'utf-8').read()
    wordlist_after_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    data = dict(Counter(wordlist_after_jieba))
    background = np.array(Image.open("love.jpg"))
    my_wordcloud = WordCloud(mask= background,background_color="black")
    my_wordcloud.generate(wl_space_split)

    image_colors = ImageColorGenerator(background)
    my_wordcloud.recolor(color_func=image_colors)


    my_wordcloud.to_file(world_file.split(".")[0]+".png")

if __name__=="__main__":
    generate_word_cloud('auto.txt')
    #generate_word_cloud('girl.txt')
