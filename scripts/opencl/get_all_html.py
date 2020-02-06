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
 
 
with open("api_url.txt", 'r') as rdFile:
    for line in rdFile:
        line = line.strip()
        a_url = "https://www.khronos.org/registry/OpenCL/sdk/1.2/docs/man/xhtml/" + line + ".html"
        saved_path = os.path.join('opencl', line) 
        try:
            html_file = getHtml(a_url)
        except Exception:
            print(line + "doesn't exist")
            html_file = None
        if html_file:
            saveHtml(saved_path, html_file)
 
print("下载成功")