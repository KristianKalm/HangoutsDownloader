import time
import re
import urllib.request
import json
import os

try:

  print ("Start");
  
  if(os.path.isdir("files") is False):
    os.mkdir("files");
    
  print ("Files folder created");
  
  count = 0;
  folderName = 'noChat';
  with open("Hangouts.json", encoding='utf8') as infile:
    for line in infile:
        if('"fallback_name"' in line):
            folderParts = line.split('"');
            folderName = "files/"+folderParts[3];
            if(os.path.isdir(folderName) is False):
                os.mkdir(folderName);
        if('"url"' in line and 'googleusercontent' in line):
            urlParts = line.split('"');
            url = urlParts[3];
                   
            urlParts = url.split("/");
            name = urlParts[len(urlParts) - 1];
            
            if(name.endswith("=m37") or name.endswith("=m18")):
                name = name + ".mp4"; 
            if("." not in name):
                name = name + ".jpg";
                
            nameParts = name.split(".");
            name = nameParts[0] + "-" + str(count) + "." + nameParts[1]; 
            
            path = folderName+"/"+name;
            print (path);
            print (url);
            
            try:
              image = open(path,'wb');
              image.write(urllib.request.urlopen(url).read());
              image.close;
            except Exception as inst:
              continue
              
            count = count + 1;
            
            #print(url)
            
    
except Exception as inst:
  print("Error " + inst)
  
print("done")
time.sleep(5)