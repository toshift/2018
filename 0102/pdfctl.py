# -*- coding: utf-8 -*-

# pip install reportlab==3.4.0
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm

# pip install pyPDF2==1.26.0
import PyPDF2

def pdfmake():
    """
    pdfを生成する
    """
    pdffile = canvas.Canvas("test.pdf")
    pdffile.saveState()

    # font 登録
#    try:
#        pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))
#        pdffile.setFont("HeiseiMin-W3",16)
#    except Exception as e:
#        print(e)
    pdffile.drawString(4*cm, 26*cm, 'testtesttest')
    pdffile.showPage()
    pdffile.save()

def pdfload():
    """
    pdfを読み込んで書いてある文字を出力する
    """
    try :
        pdfFile = open("test.pdf", "rb")
    except :
        exit(1)
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfObj = pdfReader.getPage(0)
    msg = pdfObj.extractText()
    print(msg)

if __name__ == '__main__':
    pdfmake()
    pdfload()
