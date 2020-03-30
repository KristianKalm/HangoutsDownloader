import time
import re
import urllib.request
import json
import os

try:

  print ("Start");
  
  if(os.path.isdir("files") is False):
    os.mkdir("files");
  count = 0;

  folderLine = '';
  folderName = '';
  
  groupNameLine = '';
  fallbackNameLine = '';
  
  
  folderNameLine = ''
  
  with open("Hangouts.json", encoding='utf8') as infile:
    for line in infile:
        if('"name"' in line):
            folderNameLine = line;
            print ("Folder name found "+line);
            
        if('"fallback_name"' in line and folderNameLine == ''):
            folderNameLine = line;
            print ("Fallback found "+line);
            
        if('"events"' in line):
            print ("Using line "+folderNameLine);
            folderParts = folderNameLine.split('"');
            folderName = "files/"+folderParts[3];
            if(os.path.isdir(folderName) is False):
                 os.mkdir(folderName);
            folderNameLine = '';
                
        if('"url"' in line and 'googleusercontent' in line):
            
            urlParts = line.split('"');
            url = urlParts[3];
                   
            urlParts = url.split("/");
            name = urlParts[len(urlParts) - 1];
            
            if(name.endswith("=m37") or name.endswith("=m18")):
                name = name + ".mp4"; 
            if("." not in name):
                name = name + ".jpg";
                
            name = str(count) + "-" + name; 
            
            path = folderName+"/"+name;
            print ("Saving " + path);
            #print (url);
            
            try:
              image = open(path,'wb');
              image.write(urllib.request.urlopen(url).read());
              image.close;
            except Exception as inst:
              continue
              
            count = count + 1;
except Exception as inst:
  print("Error " + inst)
  
print("done")
time.sleep(5)