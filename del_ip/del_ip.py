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
os.system("uniq -c input_ips_for_del > del_ip_tempfile")
for temp_line in open('del_ip_tempfile','r'):
    temp_line_list=temp_line.strip().split(" ")
    if int(temp_line_list[0])>1:
        print temp_line_list[1]+" encountered "+temp_line_list[0]+ " times"
        temp_flag+=1
if temp_flag>0:
    os.remove('del_ip_tempfile')
    sys.exit(0)
os.remove('del_ip_tempfile')

ip_list=[]
input_ips=open('input_ips_for_del','r')
for line in input_ips:
    ip_list.append(line.strip())
if "List of ip address has been successfully deleted" in ip_list[-1]:
    print "List of ip address has already been successfully deleted - make changes to the list"
    sys.exit(0)
input_ips.close()

server = pycpanel.conn(hostname=server_name,
                       username=admin_login,
                       password=admin_password) #Basic user/password authentication
for index,curr_ip in enumerate(ip_list):
    params = {'api.version':1,'ip':curr_ip, 'netmask':netmask,'skipifshutdown':0}#skipifshutdown:0 — Remove the IP address
    out_info_dict=server.api('delip', params=params)
    if int(out_info_dict["metadata"]["result"])==1:
        print curr_ip+" successfully deleted"
    else:
        print "ERROR "+curr_ip+"  "+out_info_dict["metadata"]["reason"]
        sys.exit(0)
    print "processed line № ", index+1
    print "----------------------"
open('input_ips_for_del','a').write("List of ip address has been successfully deleted")