# coding: utf-8
import os
import sys
import pycpanel

#=============================================================
server_name="your_server"
admin_login="your_login"
admin_password="your_password"
search_ip="ip_for_search"
#=============================================================

if os.path.exists('out'):
    os.remove('out')

server = pycpanel.conn(hostname=server_name,
                       username=admin_login, 
                       password=admin_password) #Basic user/password authentication

acc_list=[]
for acct in server.api('listaccts')['acct']:
    if acct['ip']=='search_ip':
        out=open('out','a')
        out.write( '%s\t%s\n' % (acct['ip'],acct['user']) )
        out.close()
        acc_list.append(acct['user'])
        print acct['ip'],acct['user']

out=open('out','a')
out.write('\n')
out.close()

for out_acc in acc_list:
        out=open('out','a')
        out.write( '%s\n' % out_acc)
        out.close()