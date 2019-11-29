cd /root/Desktop/ssllabs-scan/

current_time=$(date +"%Y-%m-%d_%H:%M:%S")
file_name=results-ssl-scan.out

new_fileName=$current_time-$file_name


./ssllabs-scan-v3 --hostfile="sites.txt" > raw_results/$new_fileName

cat raw_results/$new_fileName | python parse-ssl-scan.py

#./ssllabs-scan-v3 --hostfile="sites.txt" > /var/log/splunk-monitoring/$new_fileName
