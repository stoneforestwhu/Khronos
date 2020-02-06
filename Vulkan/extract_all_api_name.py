import os
import re

str_pattern = "*.xml"
api_set = set()

with open('vulkan_api.html', 'r') as html_file:
    for line in html_file:
        line = line.strip()
        matchObj = re.search(r"href=\"https://www.khronos.org/registry/vulkan/specs/1.2-extensions/man/html/(.*)\.html\">&nbsp", line)
        if matchObj:
            api_str = matchObj.group(1)
            print(api_str)
            api_set.add(api_str)
            
with open('api_name_list.txt', "w") as txt_file:
    for api_name in api_set:
        txt_file.write(api_name + "\n")
    
 
            
        
	    