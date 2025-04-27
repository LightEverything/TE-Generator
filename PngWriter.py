# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import io
import win32clipboard as wcb
import win32con

COLOR_BLACK = (0, 0, 0)
COLOR_WHITTE = (255, 255, 255)
DEFAULT_FONT_SIZE = 100
DEFAULT_FONT = "simhei.ttf"
DEFAULT_FILENAME = "new.png"

class PngWriter:
    text = ""
    color = COLOR_BLACK
    bgColor = COLOR_WHITTE
    fontSize = DEFAULT_FONT_SIZE
    font = "simhei.ttf"
    blankBorderSize = 10
    filename = DEFAULT_FILENAME
    
    def CreateImage(self):
        igFont = None
        
        try:
            igFont = ImageFont.truetype(self.font, self.fontSize)
        except:
            print("找不到字体")
            return None
            
        fontBox = igFont.getbbox(self.text)
        
        if fontBox :
            width = fontBox[2] - fontBox[0]
            height = fontBox[3] - fontBox[1]
        else:
            width = 300
            height = 300
            
        width = width + self.blankBorderSize * 2
        height = height + self.blankBorderSize * 2
        
        # 塞到图片里
        image = Image.new(mode="RGB", size=(width, height), color=self.bgColor)
        draw = ImageDraw.Draw(image)
        draw.text(xy = (self.blankBorderSize - fontBox[0], self.blankBorderSize - fontBox[1]), text = self.text, fill = self.color, font = igFont)
        
        return image
    
    def CopyToClipboard(self):
        # 把图片写入数据流
        byte_stream = io.BytesIO()
        # 将图片转换为位图格式（BMP）并保存到字节流中
        image = self.CreateImage()
        
        if image:
            image.convert("RGB").save(byte_stream, format="BMP")
        else:
            return

        # 获取位图数据
        bitmap_data = byte_stream.getvalue()[14:]

        try:
            # 打开剪贴板
            wcb.OpenClipboard()
            wcb.EmptyClipboard()

            # 将位图数据写入剪贴板
            wcb.SetClipboardData(wcb.CF_DIB, bitmap_data)
            wcb.CloseClipboard()
            print("成功复制到剪贴板")
        except:
            print("无法打开剪贴板")

    def SaveImage(self):
        # 直接保存到本地
        image = self.CreateImage()
        if image:
            image.save(DEFAULT_FILENAME)
        else:
            return 