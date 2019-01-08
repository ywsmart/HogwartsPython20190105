#!/usr/bin/env python
#coding=utf-8

from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
from PIL import Image
import jieba

# Read the whole text.
font = r'C:\Windows\Fonts\Microsoft YaHei UI\MSYHBD.TTC'
text = open("loveme.txt").read()
wordlist_after_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)
# 设置背景图片
RGB_coloring = np.array(Image.open("love.jpg"))
# 设置参数：背景颜色,词云显示的最大词数，设置背景图片，字体最大值
wc = WordCloud(font_path =font,background_color="white",max_words=2000,mask=RGB_coloring,max_font_size=100, random_state=42)
#generate word cloud
wc.generate(wl_space_split)
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(RGB_coloring)
wc.recolor(color_func=image_colors)
wc.to_file("mylove.png")