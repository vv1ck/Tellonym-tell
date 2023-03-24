try:
	from  requests import session,ConnectionError
	from random import choice
	from threading import Lock,Thread
except Exception as Joker:exit(Joker)
def vv1ck(*a, **b):
	with Lock():print(*a, **b)


tokens='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTM0ODQ4NjAsImlhdCI6MTY3OTY4MjE3OX0.WbZYdNqWBuRDOuNSzpDnSkKRDlmGoRUFTs5ELBnmsb0'


class TELLONYM_TELLS:
	def __init__(self):
		self.username=input('[$] Enter username: ')
		self.DONE=0
		self.ERROR=0
		self.PEOXY=0
		self.proxylist = []
		try:self.proxy=open(input('[$] Enter name file (proxy) : '),'r').read().splitlines()
		except FileNotFoundError:input('\n[-] The file name is incorrect !\n');return TELLONYM_TELLS()
		self.Get_ID()
	def SENT_TELLS(self):
		global ID
		while 1:
			for pro in self.proxy:
				self.proxylist.append(pro)
				runs = str(choice(self.proxylist))
			try:
				PROXY = {
					"http": f"http://{runs}",
					"https": f"http://{runs}"}
				run=session().post('https://api.tellonym.me/tells/new',headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Accept':'application/json','Tellonym-Client':'web:3.57.1','Content-Type':'application/json;charset=utf-8','Authorization':'Bearer '+tokens},json={"isInstagramInAppBrowser":False,"isSnapchatInAppBrowser":False,"isSenderRevealed":False,"tell":"Joker Here (insta:@221298)","userId":ID,"limit":10},proxies=PROXY)
				if run.status_code==200:
					self.DONE+=1
					vv1ck(f'\r[$] TELL:{self.DONE} |Error:{self.ERROR}|Proxy:{self.PEOXY}\r',end="")
				elif run.status_code==403:
					self.ERROR+=1
					vv1ck(f'\r[$] TELL:{self.DONE} |Error:{self.ERROR}|Proxy:{self.PEOXY}\r',end="")
				elif run.status_code==429:
					self.PEOXY+=1
					vv1ck(f'\r[$] TELL:{self.DONE} |Error:{self.ERROR}|Proxy:{self.PEOXY}\r',end="")
				elif run.status_code==418:
					self.PEOXY+=1
					vv1ck(f'\r[$] TELL:{self.DONE} |Error:{self.ERROR}|Proxy:{self.PEOXY}\r',end="")
				elif run.status_code==503:
					self.PEOXY+=1
					vv1ck(f'\r[$] TELL:{self.DONE} |Error:{self.ERROR}|Proxy:{self.PEOXY}\r',end="")
				else:
					print(run.text)
					print(run)
			except ConnectionError:
				self.PEOXY+=1
				vv1ck(f'\r[$] TELL:{self.DONE} |Error:{self.ERROR}|Proxy:{self.PEOXY}\r',end="")
			except KeyboardInterrupt:exit()
	
	def Threads(self):
		global ID
		theards = []
		for i in range(200):
			th1 = Thread(target=self.SENT_TELLS)
			th1.start()
			theards.append(th1)	
		for th2 in theards:
			th2.join()
	def Get_ID(self):
		sent = session().get('https://api.tellonym.me/profiles/name/{}?limit=13'.format(self.username),headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Accept':'application/json','Tellonym-Client':'web:3.57.1','Content-Type':	'application/json;charset=utf-8'})
		if 'id' in sent.text:
			global ID
			ID = sent.json()['id']
			self.Threads()
		else:
			print(sent.text)
TELLONYM_TELLS()
