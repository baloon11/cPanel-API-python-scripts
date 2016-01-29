# coding: utf-8
import sys
import pycpanel

#=============================================================
server_name="your_server"
admin_login="your_login"
admin_password="your_password"
#=============================================================

server = pycpanel.conn(hostname=server_name,
                       username=admin_login, 
                       password=admin_password) #Basic user/password authentication
account_list=server.api('listaccts')['acct']
for index,account_name in enumerate(account_list):
    out_info_dict=server.api('removeacct', params={'api.version':1,'user':account_name['user']})
    if int(out_info_dict["metadata"]["result"])==1:
        print account_name['user']+" successfully deleted"
    else:
        print "ERROR "+account_name['user']+"  "+out_info_dict["metadata"]["reason"]
        sys.exit(0)
    print "processed line № ", index+1
    print "----------------------"
