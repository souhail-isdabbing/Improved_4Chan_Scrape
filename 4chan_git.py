import requests
import sys
import os
import wget
from bs4 import BeautifulSoup
import pprint
import shutil

res=requests.get(sys.argv[1])
soup=BeautifulSoup(res.text,'html.parser')

class Images():
    def __init__(self):
        self.src=soup.find_all('img',loading='lazy')
    def full_pic(self):
        srcs=[]
        for i in self.src:
            if 'jpg' in i['src']:
                jpg=i['src'].replace('s.jpg','.jpg')
                srcs.append(jpg)
            if 'png' in i['src']:
                png=i['src'].replace('s.png','.png')
                srcs.append(png)
        return srcs
    
    def urling(self):
        urls=[]
        for src in self.full_pic():
            url=src.replace('//','https://')
            urls.append(url)
        return(urls)




class Directory():
    def __init__(self,parent_dir,directory):
        self.parent_dir=parent_dir
        self.directory=directory
        self.path=os.path.join(self.parent_dir,self.directory)
    def create_dir(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)

def get_name():
    link=sys.argv[1]
    return link[24:].replace('/','')

def filing(link):
    nums=[]
    for i in link[20:]:
        if i in '0123456789':
            nums.append(i)
    return f'{"".join(nums)}{link[-4:]}'


images=Images()
directory=Directory('C:\\User Destination',f'{get_name()}')


def main():
    
    def check(link):
        r=requests.get(link)
        if r.status_code==200:
            r.raw.decode_content = True
            return 1
    directory.create_dir()
    for url in images.urling():
        if check(url)==1:
            wget.download(url)
            source=f'C:\\User destination\\{filing(url)}'
            shutil.move(source,directory.path)
    

main()
