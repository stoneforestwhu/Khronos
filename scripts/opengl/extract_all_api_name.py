import os
import re

str_pattern = "*.xml"
api_set = set()

with open('indexflat.html', 'r') as html_file:
    for line in html_file:
        line = line.strip()
        matchObj = re.search(r"https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/(.*)\.xhtml", line)
        if matchObj:
            api_str = matchObj.group(1)
            print(api_str)
            api_set.add(api_str)
            
with open('api_name_list.txt', "w") as txt_file:
    for api_name in api_set:
        txt_file.write(api_name + "\n")
    
 
            
        
	    