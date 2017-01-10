import httplib, ssl, sys

# Ignore certicate-validation-urllib2
#SRC : http://stackoverflow.com/questions/19268548/python-ignore-certicate-validation-urllib2
#Context creation
#https://docs.python.org/2/library/ssl.html#ssl.wrap_socket
ctx = ssl.create_default_context()
# Disable check hostname
#https://docs.python.org/2/library/ssl.html#ssl.SSLContext.check_hostname
ctx.check_hostname = False
# No certificates will be required from the other side of the socket connection.
# If a certificate is received from the other end, no attempt to validate it is made.
#https://docs.python.org/2/library/ssl.html#ssl.SSLContext.verify_mode
#https://docs.python.org/2/library/ssl.html#ssl.CERT_NONE
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
