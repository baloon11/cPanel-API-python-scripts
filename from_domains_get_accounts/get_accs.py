# coding: utf-8
import os,sys
import pycpanel

#=============================================================
server_name="your_server"
admin_login="your_login"
admin_password="your_password"
#=============================================================

if os.path.exists('out'):
    os.remove('out')

server = pycpanel.conn(hostname=server_name,
                       username=admin_login, 
                       password=admin_password) #Basic user/password authentication

domains_list=[domain.strip().lower() for domain in open('domains','r')]
acc_list=[]
for domain in domains_list:
    for acct in server.api('listaccts')['acct']:
        if acct['domain']==domain:
            out=open('out','a')
            out.write( '%s\t%s\n' % (domain,acct['user']) )
            out.close()
            acc_list.append(acct['user'])

out=open('out','a')
out.write('\n')
out.close()

for out_acc in acc_list:
        out=open('out','a')
        out.write( '%s\n' % out_acc)
        out.close()