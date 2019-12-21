current_time=$(date +"%Y-%m-%d_%H:%M:%S")
file_name=results-ssl-scan.out

new_fileName=$current_time-$file_name

./ssllabs-scan-v3 --hostfile="sites.txt" > results/$new_fileName
