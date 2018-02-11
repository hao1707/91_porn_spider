import requests
import os,re,time
b=1
flag=1
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
def format_str(content):
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str = content_str+i
    return content_str
def download_mp4(url,dir):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com'}
    req=requests.get(url=url)
    if req.status_code==200:
        b=1
        with open(str(dir)+'.mp4','wb') as f:
            f.write(req.content)
    else:
        if b<3:
            time.sleep(2)
            download_mp4(url,dir)
            b+=1
headers={'Accept-Language':'zh-CN,zh;q=0.9','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com','Content-Type': 'multipart/form-data; session_language=cn_CN'}
while flag<=100:
    tittle=[]
    base_url='http://91porn.com/view_video.php?viewkey='
    page_url='http://91porn.com/v.php?next=watch&page='+str(flag)
    get_page=requests.get(url=page_url,headers=headers)
    viewkey=re.findall(r'<a target=blank href="http://91porn.com/view_video.php\?viewkey=(.*)&page=.*&viewtype=basic&category=mr">\n                    <img ',str(get_page.content,'utf-8',errors='ignore'))
    for key in viewkey:
        get=requests.get('http://www.jiexiba.tech/api/pron?url='+base_url+key)
        get_tittle=requests.get(base_url+key,headers=headers)
        tittle=re.findall(r'<div id="viewvideo-title">(.*?)</div>',str(get_tittle.content,'utf-8',errors='ignore'),re.S)
        t=tittle[0]
        tittle[0]=format_str(t)
        t=tittle[0]
        if not os.path.isfile(str(t)+'.mp4'):
            print('开始下载：'+str(t))
            download_mp4(str(get.text),str(t))
            print('下载完成')
        else:
            print('文件已存在')
    flag=flag+1
    print('此页已下载完成，下一页是'+str(flag))
    

