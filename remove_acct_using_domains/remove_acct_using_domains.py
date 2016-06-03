# coding: utf-8
import os
import sys
import pycpanel

#=============================================================
server_name="your_server"
admin_login="your_login"
admin_password="your_password"
#=============================================================

temp_flag=0
os.system("uniq -c domains > remove_domains_tempfile")
for temp_line in open('remove_domains_tempfile','r'):
    temp_line_list=temp_line.strip().split(" ")
    if int(temp_line_list[0])>1:
        print temp_line_list[1]+" encountered "+temp_line_list[0]+ " times"
        temp_flag+=1
if temp_flag>0:
    os.remove('remove_domains_tempfile')
    sys.exit(0)
os.remove('remove_domains_tempfile')

domains_list=[domain.strip().lower() for domain in open('domains','r')]
if "List of accounts has been successfully deleted" in domains_list[-1]:
    print "List of accounts (using list of domains from file 'domains')\
        has already been successfully deleted - make changes to the list"
    sys.exit(0)

server = pycpanel.conn(hostname=server_name,
                       username=admin_login, 
                       password=admin_password) #Basic user/password authentication
account_list=[]
for domain in domains_list:
    for acct in server.api('listaccts')['acct']:
        if acct['domain']==domain:
            account_list.append(acct['user'])
            print '%s account matches %s domain'%(acct['user'],acct['domain'])
            print '========================================'

print"Start removing accounts"
print '========================================'

for index,account_name in enumerate(account_list,start=1):
    out_info_dict=server.api('removeacct', params={'api.version':1,'user':account_name})
    if int(out_info_dict["metadata"]["result"])==1:
        print account_name+" successfully deleted"
    else:
        print '========================================'
        print 'ERROR %s ---> %s'%(account_name,out_info_dict["metadata"]["reason"])
        print '========================================'
        sys.exit(0)
    print "processed line № ", index
    print '========================================'
open('domains','a').write("List of accounts has been successfully deleted")