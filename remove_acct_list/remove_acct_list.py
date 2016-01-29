# coding: utf-8
import os,sys
import pycpanel

#=============================================================
server_name="your_server"
admin_login="your_login"
admin_password="your_password"
#=============================================================

temp_flag=0
os.system("uniq -c input_acct_list_for_remove > remove_acct_tempfile")
for temp_line in open('remove_acct_tempfile','r'):
    temp_line_list=temp_line.strip().split(" ")
    if int(temp_line_list[0])>1:
        print temp_line_list[1]+" encountered "+temp_line_list[0]+ " times"
        temp_flag+=1
if temp_flag>0:
    os.remove('remove_acct_tempfile')
    sys.exit(0)
os.remove('remove_acct_tempfile')

account_list=[]
input_accts=open('input_acct_list_for_remove','r')
for line in input_accts:
    account_list.append(line.strip())
if "List of accounts has been successfully deleted" in account_list[-1]:
    print "List of accounts has already been successfully deleted - make changes to the list"
    sys.exit(0)
input_accts.close()

server = pycpanel.conn(hostname=server_name,
                       username=admin_login, 
                       password=admin_password) #Basic user/password authentication
for index,account_name in enumerate(account_list):
    out_info_dict=server.api('removeacct', params={'api.version':1,'user':account_name})
    if int(out_info_dict["metadata"]["result"])==1:
        print account_name+" successfully deleted"
    else:
        print "ERROR "+account_name+"  "+out_info_dict["metadata"]["reason"]
        sys.exit(0)
    print "processed line № ", index+1
    print "----------------------"
open('input_acct_list_for_remove','a').write("List of accounts has been successfully deleted")