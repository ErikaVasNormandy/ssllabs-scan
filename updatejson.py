#!/usr/bin/python
import json
import md5
import sys
import time

from pprint import pprint
import datetime

import json


site_host = ""
site_ipaddress = ""
site_grade = ""
site_httpstatuscode = 0
site_serversignature = ""
site_rawdate = 0
site_expirationdate = ""
#file_timestamp = 'results/ssl_scan_{:%d-%b-%Y_%H:%M}.json'.format(datetime.datetime.now())
file_timestamp = 'results/ssl_scan.json'
site_scantimestamp = '{:%d-%b-%Y_%H:%M}'.format(datetime.datetime.now())
		
data = {
	"site" : {
		"hostname": site_host,
		"ip_address": site_ipaddress,
		"scan_date": site_scantimestamp,
		"grade": site_grade,
		"status_code": site_httpstatuscode,
		"serversignature": site_serversignature,
		"rawdate": site_rawdate,
		"expires": site_expirationdate
				
	}
}

with open(file_timestamp, "a+") as f:
	f.write(",")
	print("\nbreak")
	f.write(json.dumps(data))
		
#			json.dump(original_data, f)

	f.close()
