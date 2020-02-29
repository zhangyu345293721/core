# -*- coding:utf-8 -*-
'''
在图片上加文字
author:zhangyu
date:2020/2/14
'''

from PIL import Image, ImageDraw, ImageFont


def draw_picture(pic_path: str, output_path: str, text_str='张秋月，超级漂亮 ', font_size=10):
    '''
        在图片上进行加字
    Args:
        pic_path:输入路径
        output_path:输出路径
        text_str:文档字符
        font_size: 字体大小，默认10
    '''
    img_raw = Image.open(pic_path)
    img_array = img_raw.load()
    img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size)
    text_generator = generator_fun(text_str)
    for y in range(0, img_raw.size[1], font_size):
        for x in range(0, img_raw.size[0], font_size):
            draw.text((x, y), next(text_generator), font=font, fill=img_array[x, y])
    img_new.convert('RGB').save(output_path)


def generator_fun(text_str: str):
    while True:
        for i in range(len(text_str)):
            yield text_str[i]


if __name__ == '__main__':
    input_pic_path = "d://zy.jpg"
    output_pic_path = 'd://save2.jpg'
    draw_picture(input_pic_path, output_pic_path)
