#### cPanel API python scripts for create/delete accounts and ip addresses.

This repository is a set of python scripts (that using cPanel API and
`pycpanel` Рython library) that allows to manipulate accounts and ip addresses.

---------------

directory `add_ip`  contains 2 files.

`add_ip.py` is a script that add ip addresses from file `input_ips` to your cPanel.

---------------

directory `del_ip`  contains 2 files.

`del_ip.py` is a script that delete list of ip addresses from your cPanel.
  
List for delete -- in `input_ips_for_del` file.

---------------

directory `remove_acct_list`  contains 2 files.

`remove_acct_list.py` is a script that delete list of accounts from  your cPanel.

List for delete -- in `input_acct_list_for_remove` file.

---------------

`remove_all_acct.py` is a script that delete all accounts from your cPanel.

--------------

In the head of each script you need to change this data:
	#=============================================================
	server_name="your_server"
	admin_login="your_login"
	admin_password="your_password"
	#=============================================================

**Note**: in files with data (lists of ip addresses or accounts) should not be empty lines.

If the data file has been successfully processed by the script,
in the end of the data file will be automatically 
recorded information that the file has been processed.

Before starting of work, script checks if line with this information exists in the data file.

If this line is in the file -   it is mean the file has been processed
and the script not start its work.


-----------------------------------

Before working each script checks the data file.
If the data file contains several identical lines,
console displays additional information and the script does not begin its work.

-----------------------------------

#### Requirements
 
	Python 2.7.10
	pip install pycpanel==0.1.5













