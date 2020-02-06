import os
import re

str_pattern = "*.xml"
api_set = set()

with open('sduview.html', 'r') as html_file:
    for line in html_file:
        line = line.strip()
        matchObj = re.search(r"href=(.*)\.xml\">&nbsp", line)
        if matchObj:
            api_str = matchObj.group(1)[1:]
            api_set.add(api_str)
            
with open('api_url.txt', "w") as txt_file:
    for api_name in api_set:
        txt_file.write(api_name + "\n")
    
 
            
        
	    