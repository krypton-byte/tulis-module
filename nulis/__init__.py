from concurrent.futures import ThreadPoolExecutor
import os
from typing import Literal, Union
from PIL import Image, ImageDraw, ImageFont
"""
Bot Tulis Sangat cocok Untuk anda Yg Malas Menulis :v
"""

__author__="Krypton-Byte, MhankBarBar, NoneX9, Underfif, Kitsune, ITacHi, GiovalIT"
__title__ ="BotTulis"
license   ="MIT License"
__all__ = ['tulis']
myasset = lambda x:os.path.dirname(__file__)+"/"+x
class _tulis:
    """
    listOrText : String
    """
    def __init__(self):
        pass
        #self.text = listOrText
        #self.output = []
        #self.text_perlembar = []
    def parser(self, text):
        img, font, kata, tempkata=Image.open(myasset("before.jpg")), ImageFont.truetype(myasset("IndieFlower.ttf"),24),'',''
        draw=ImageDraw.Draw(img)
        if type(text) is not list:
            for i in text:
                if draw.textsize(tempkata, font)[0] < 734:
                    tempkata+=i
                else:
                    kata, tempkata=kata+'%s\n'%tempkata, i
            if tempkata:
                kata+="%s"%tempkata
            spliter=kata.split("\n")
        else:
            spliter=text
        return spliter
    def _write(self, spliter):
        img, font=Image.open(myasset("before.jpg")), ImageFont.truetype(myasset("IndieFlower.ttf"),24)
        draw=ImageDraw.Draw(img)
        line=190
        for i in spliter[:25]:
            draw.text((170, int(line)), i, font=font, fill=(0, 0, 0)) #selisih = Line
            line+=37 + 2.2
        return img
    def write(self, text: str, worker: Union[int, Literal['auto']]):
        sheets = self.sheets(self.parser(text))
        return ThreadPoolExecutor(max_workers=sheets.__len__() if worker == 'auto' else worker).map(self._write, sheets)
    def sheets(self, l:list):
        if l:
            return [l[:25]]+self.sheets(l[25:])
        else:
            return []
    def nulis(self):
        pass
    """@property
    def tulis(self):
        img, font, kata, tempkata=Image.open(myasset("before.jpg")), ImageFont.truetype(myasset("IndieFlower.ttf"),24),'',''
        draw=ImageDraw.Draw(img)
        if type(self.text) is not list:
            self.output=[]
            for i in self.text:
                if draw.textsize(tempkata, font)[0] < 734:
                    tempkata+=i
                else:
                    kata, tempkata=kata+'%s\n'%tempkata, i
            if tempkata:
                kata+="%s"%tempkata
            spliter=kata.split("\n")
        else:
            spliter=self.text
        line=190
        for i in spliter[:25]:
            draw.text((170, int(line)), i, font=font, fill=(0, 0, 0)) #selisih = Line
            line+=37 + 2.2
        self.output.append(img)
        if len(spliter) > 25:
            self.output+=tulis(spliter[25:]).tulis()
        return self.output"""

class tulis:
    def __init__(self, text: str, worker: Union[int, Literal['auto']] = 'auto') -> None:
        self.text: str = text
        self.worker: Union[int, Literal['auto']] = worker
    def __iter__(self):
        yield from _tulis().write(self.text, self.worker)
    def __enter__(self):
        return self.__iter__()
    def __exit__(self, *args):
        pass
    def __repr__(self):
        return "<length: %s char>"%len(self.text)