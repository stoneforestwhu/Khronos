# -*- coding: utf-8 -*-  
import os
import urllib.request
 
def getHtml(url):
 html = urllib.request.urlopen(url).read()
 return html
 
def saveHtml(file_name, file_content):
  # 注意windows文件命名的禁用符，比如 /
 with open(file_name.replace('/', '_') + ".html", "wb") as f:
  # 写文件用bytes而不是str，所以要转码
  f.write(file_content)
 
aurl = "https://www.khronos.org/registry/OpenGL-Refpages/gl4/"
html = getHtml(aurl)
saveHtml("api_list", html)
 
print("下载成功")