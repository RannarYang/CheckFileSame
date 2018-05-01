#coding=utf-8  
  
from PIL import Image,ImageEnhance,ImageFilter  
import os  
import fnmatch  
import re,time  
  
import urllib, random  
  
  
#import hashlib    
   
def getGray(image_file):  
   tmpls=[]  
   for h in range(0,  image_file.size[1]):#h  
      for w in range(0, image_file.size[0]):#w  
         tmpls.append( image_file.getpixel((w,h))  )  
            
   return tmpls  
   
def getAvg(ls):#获取平均灰度值  
   return sum(ls)/len(ls)  
   
def getMH(a,b):#比较100个字符有几个字符相同  
   dist = 0;  
   for i in range(0,len(a)):  
      if a[i]==b[i]:  
         dist=dist+1  
   return dist  
   
def getImgHash(fne):  
   image_file = Image.open(fne) # 打开  
   image_file=image_file.resize((12, 12))#重置图片大小我12px X 12px  
   image_file=image_file.convert("L")#转256灰度图  
   Grayls=getGray(image_file)#灰度集合  
   avg=getAvg(Grayls)#灰度平均值  
   bitls=''#接收获取0或1  
   #除去变宽1px遍历像素  
   for h in range(1,  image_file.size[1]-1):#h  
      for w in range(1, image_file.size[0]-1):#w  
         if image_file.getpixel((w,h))>=avg:#像素的值比较平均值 大于记为1 小于记为0  
            bitls=bitls+'1'  
         else:  
            bitls=bitls+'0'  
   return bitls  
'''''          
   m2 = hashlib.md5()    
   m2.update(bitls) 
   print m2.hexdigest(),bitls 
   return m2.hexdigest() 
'''  

def is_img(ext):
    ext = ext.lower()
    if ext == '.jpg':
        return True
    elif ext == '.png':
        return True
    elif ext == '.jpeg':
        return True
    elif ext == '.bmp':
        return True
    else:
        return False


imgPaths = []

for parent,dirnames,filenames in os.walk('.'):
    for i in filenames:
        path = os.path.join(parent, i)
        ext = (os.path.splitext(path)[1])
        if(is_img(ext)):
            imgPaths.append(path)
# print(imgPaths)

for imgPath in imgPaths:
    a=getImgHash(imgPath)#图片地址自行替换
    aimg = Image.open(imgPath)
    aWidth = aimg.size[0]
    aHeight = aimg.size[1]
    aFormat = aimg.format
    
    for parent,dirnames,filenames in os.walk('.'):
        for i in filenames:
            path = os.path.join(parent, i)
            ext = (os.path.splitext(path)[1])
            if(is_img(ext)):
                bimg = Image.open(path)
                bWidth = bimg.size[0]
                bHeight = bimg.size[1]
                bFormat = bimg.format
                if(aWidth == bWidth and aHeight == bHeight and aFormat == bFormat and imgPath != path):
                    b=getImgHash(path)  
                    compare=getMH(a,b)  
                    if(compare >= 99 ):
                        print (imgPath, path,u'相似度',str(compare)+'%') 

print('end')