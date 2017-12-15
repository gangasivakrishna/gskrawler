from bs4 import BeautifulSoup
import re
import requests
import random
import urllib.request

#HTML Head
def head(urlstr):
	url=urlstr
	if(url.startswith("http://") or url.startswith("https://")):
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			return (soup.head)
		except Exception as e:
			return(e)
	else:
		return("Incorrect URL !! ")

#HTML title
def title(urlstr):
	url=urlstr
	if(url.startswith("http://") or url.startswith("https://")):
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			return (soup.title.string)
		except Exception as e:
			return(e)
	else:
		return("Incorrect URL !! ")

#HTML Body
def body(urlstr):
	url=urlstr
	if(url.startswith("http://") or url.startswith("https://")):
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			return (soup.body)
		except Exception as e:
			return(e)
	else:
		return("Incorrect URL !! ")

#HTML page
def html(urlstr):
	url=urlstr
	if(url.startswith("http://") or url.startswith("https://")):
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			return (soup.prettify())
		except Exception as e:
			return(e)
	else:
		return("Incorrect URL !! ")

#Website Links
def links(urlstr):
	url=urlstr
	if(url.startswith("http://") or url.startswith("https://")):
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			for link in soup.find_all('a'):
				print(link.text,"\n"+"URL : "+link.get('href'))
				print("\n")
		except Exception as e:
			return(e)
	else:
		return("Incorrect URL !! ")


#Tag Name and Class name

def tagclass(urlstr,tagname,cls):
	url=urlstr
	if(url.startswith("http://") or url.startswith("https://")):
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			for data in soup.find_all(tagname, { "class" : cls }):
				text=data.text
				if(text is not None):
					print(text)
		except Exception as e:
			return(e)
	else:
		return("Incorrect URL !! ")

#Tag Name and Id name

def tagid(urlstr,tagname,idname):
	url=urlstr
	if(url.startswith("http://") or url.startswith("https://")):
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			for data in soup.find_all(tagname, { "id" : idname }):
				text=data.text
				if(text is not None):
					print(text)
		except Exception as e:
			return(e)
	else:
		return("Incorrect URL !! ")




#Emails

def emails(urlstr):
	url=urlstr
	if(url.startswith("http://") or url.startswith("https://")):
		proc=[]
		mail=[]
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			links = [a.attrs.get('href') for a in soup.select('a[href]') ]
			for i in links:
				if(("contact" in i or "Contact")or("Career" in i or "career" in i))or('about' in i or "About" in i)or('Services' in i or 'services' in i):
					proc.append(i)
			proc=set(proc)
			for j in proc:
				if(j.startswith("http") or j.startswith("www")):
					r=requests.get(j)
					data=r.text
					soup=BeautifulSoup(data,'html.parser')
					for name in soup.find_all('a'):
						k=name.text
						a=bool(re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',k))
						if('dot' in k and 'at' in k)or ('@' in k and a==True):
							k=k.replace(" ",'').replace('\r','')
							k=k.replace('\n','').replace('\t','')
							if(len(mail)==0)or(k not in mail):
								print(k)
							mail.append(k)
				else:
					newurl=url+j
					r=requests.get(newurl)
					data=r.text
					soup=BeautifulSoup(data,'html.parser')
					for name in soup.find_all('a'):
						k=name.text
						a=bool(re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',k))
						if('dot' in k and 'at' in k)or ('@' in k and a==True):
							k=k.replace(" ",'').replace('\r','')
							k=k.replace('\n','').replace('\t','')
							if(len(mail)==0)or(k not in mail):
								print(k)
							mail.append(k)
			mail=set(mail)
			if(len(mail)==0):
				print("NO MAILS FOUND")
		except Exception as e:
			return(e)
	else:
		return("Incorrect URL !! ")

#Images

def images(urlstr):
	url=urlstr
	if(url.startswith("http://") or url.startswith("https://")):
		try:
			response=requests.get(url)
			soup=BeautifulSoup(response.text,'html.parser')
			for img in soup.find_all('img'):
				src=img.get('src')
				print(src)
				name=random.randrange(1,1000)
				imgname=str(name)
				lk=url+"/"+src
				urllib.request.urlretrieve(lk,imgname)
		except Exception as e:
			return(e)
	else:
		return("Incorrect URL !! ")

