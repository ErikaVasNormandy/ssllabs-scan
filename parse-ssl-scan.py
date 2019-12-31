#!/usr/bin/python
import json
import md5
import sys
import time

from pprint import pprint
import datetime

import json


### Variables

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

with sys.stdin as json_data:
        try:
                data = json.load(json_data)
        except:
                print "Error: no JSON data received!"
                exit(1)
for site in data:
	###Main bit of information
        endpoints = site['endpoints']

        protocol = site['protocol']
        criteriaVersion = site['criteriaVersion']
        isPublic = site['isPublic']
        endpoints = site['endpoints']
	certs = site['certs']

	print("\nNow Scanning %s ---------------\n---------------" % site['host'])
	
	for i in endpoints:
		print("Host: %s" % site['host'])
		site_host = site['host']
		
		print("IP Address: %s " % i['ipAddress'])	
		site_ipaddress = i['ipAddress']
		
		try: 
			print("Grade: %s " % i['grade'])
			site_grade = i['grade']

			print("HTTP Status Code: %s " % i['details']['httpStatusCode'])
			site_httpstatuscode = i['details']['httpStatusCode']

			print("serverSignature: %s" % i['details']['serverSignature'])
			site_serversignature = i['details']['serverSignature']

			timenotAfter = time.gmtime(site['certs'][0]['notAfter']/1000.0)
			print("Time Millisecond Value: %s " % site['certs'][0]['notAfter'])
			site_rawdate = site['certs'][0]['notAfter']

			print("Expires: %s" % time.strftime('%Y-%m-%dT%H:%M:%SZ', timenotAfter))
			site_expirationdate = time.strftime('%Y-%m-%dT%H:%M:%SZ', timenotAfter)	
		except:
			print("scan could not complete successfully")	
		

		
		
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

		print(data)

		with open(file_timestamp, "a+") as f:
			f.write(",")
			print("\nbreak")
			f.write(json.dumps(data))
		
#			json.dump(original_data, f)

			f.close()
