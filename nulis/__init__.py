from PIL import Image, ImageDraw, ImageFont
"""
Bot Tulis Sangat cocok Untuk anda Yg Malas Menulis :v
"""
__author__="Krypton-Byte, MhankBarBar, NoneX9, Underfif, Kitsune, ITacHi, GiovalIT"
__title__ ="BotTulis"
license   ="MIT License"
class tulis:
    """
    listOrText : String
    """
    def __init__(self, listOrText):
        self.text = listOrText
        self.output = []
    def tulis(self):
        img, font, kata, tempkata=Image.open("nulis/before.jpg"), ImageFont.truetype("nulis/IndieFlower.ttf",24),'',''
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
        return self.output
    def __repr__(self):
        return "<length: %s char>"%len(self.text)
