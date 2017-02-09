import subprocess
import re


hosts =[
["23.23.255.255","us-east-1",-1],
["52.14.64.0","us-east-2",-1],
["52.60.50.0","ca-central-1",-1],
["52.222.9.163","us-gov-west-1",-1],
["35.160.63.253","us-west-2",-1],
["50.18.56.1","us-west-1",-1],
["34.248.60.213","eu-west-1",-1],
["35.156.63.252","eu-central-1",-1],
["52.56.34.0","eu-west-2",-1],
["13.112.63.251","ap-northeast-1",-1],
["52.78.63.252","ap-northeast-2",-1],
["46.51.216.14","ap-southeast-1",-1],
["13.54.63.252","ap-southeast-2",-1],
["35.154.63.252","ap-south-1",-1],
["52.67.255.254","sa-east-1",-1]
]

for host in hosts:
	ping = subprocess.Popen(
    	["ping", "-n", "3", host[0]],
    	stdout = subprocess.PIPE,
    	stderr = subprocess.PIPE
	)

	out, error = ping.communicate()

	out = out.split('\n')[-3:]
	times =  re.findall(r'[0-9]+',out[1])	
	host[2] = int(times[1])

def getKey(item):
	return item[2]

hosts = sorted(hosts, key=getKey)

for host in hosts:
	print '{1:<30}\t [{0:<20}]\t\t = {2} ms'.format(host[0],host[1], host[2])