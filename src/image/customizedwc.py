#!/usr/bin/env python
#coding=utf-8

import matplotlib.pyplot as plt
from wordcloud.wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import numpy as np
from PIL import Image
import jieba
import codecs
from scipy.misc import imread

def generate_word_cloud(world_file):
    font = r'C:\Windows\Fonts\Microsoft YaHei UI\MSYHBD.TTC' #os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")
    text = codecs.open(world_file,encoding = 'utf-8').read()
    wordlist_after_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    backgroup_mask = np.array(Image.open("love.jpg"))
    my_wordcloud = WordCloud(font_path =font, mask = backgroup_mask, background_color ="black",max_font_size=100,random_state=42)
    my_wordcloud.generate(wl_space_split)

    image_colors = ImageColorGenerator(backgroup_mask)
    my_wordcloud.recolor(color_func=image_colors)

    #plt.imshow(my_wordcloud)
    #plt.axis("off")
    #plt.show()
    my_wordcloud.to_file("love.png")

if __name__=="__main__":
    generate_word_cloud('loveme.txt')