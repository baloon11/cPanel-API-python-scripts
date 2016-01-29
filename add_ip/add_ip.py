# coding: utf-8
import os,sys
import pycpanel

#=============================================================
server_name="your_server"
admin_login="your_login"
admin_password="your_password"
netmask="255.255.255.255"
#=============================================================

temp_flag=0
os.system("uniq -c input_ips > add_ip_tempfile")
for temp_line in open('add_ip_tempfile','r'):
    temp_line_list=temp_line.strip().split(" ")
    if int(temp_line_list[0])>1:
        print temp_line_list[1]+" encountered "+temp_line_list[0]+ " times"
        temp_flag+=1
if temp_flag>0:
    os.remove('add_ip_tempfile')
    sys.exit(0)
os.remove('add_ip_tempfile')

ip_list=[]
input_ips=open('input_ips','r')
for line in input_ips:
    ip_list.append(line.strip())
if "List of ip address has been successfully added" in ip_list[-1]:
    print "List of ip address has already been successfully added - make changes to the list"
    sys.exit(0)
input_ips.close()

server = pycpanel.conn(hostname=server_name,
                       username=admin_login,
                       password=admin_password) #Basic user/password authentication
for index,curr_ip in enumerate(ip_list):
    params = {'api.version':1,'ips':curr_ip, 'netmask':netmask}
    out_info_dict=server.api('addips', params=params)
    if int(out_info_dict["metadata"]["result"])==1:
        print curr_ip +" successfully added"
    else:
        print "ERROR "+curr_ip+"  "+out_info_dict["metadata"]["reason"]
        sys.exit(0)
    print "processed line № ", index+1
    print "----------------------"

open('input_ips','a').write("List of ip address has been successfully added")