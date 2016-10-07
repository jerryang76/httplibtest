import httplib, ssl, sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sub = '/LoginForm.asp'
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
count = 0

def help():
	print 'httplibtest <Destination IP> <port> <http,https>'
	print 'example:'
	print 'httplibtest 61.218.72.107 443 https'
	print 'httplibtest 61.218.72.109 80 http'
	sys.exit()

if len(sys.argv) < 4:
	help()
host = sys.argv[1]
port = sys.argv[2]
prot = sys.argv[3]

def sendhttp(count,prot_type):
	try:
		prot_type.request('GET', sub, '', headers)  
		httpres = prot_type.getresponse() 

		if (httpres.read().find("username") is None):
			print "NOK __> ", count	
		else:
			count = count + 1
			print "OK --> ", count  			
		return count
	
	except (KeyboardInterrupt,SystemExit):
		print '\nRun', count ,'times'
		sys.exit()
		
while True: 	
	if prot == 'http':
		prot_type = httplib.HTTPConnection(host, port, timeout=1)	
	elif prot == 'https':
		prot_type = httplib.HTTPSConnection(host, port, timeout=1, context=ctx)	 	
	else:
		help()
	count = sendhttp(count,prot_type) 
