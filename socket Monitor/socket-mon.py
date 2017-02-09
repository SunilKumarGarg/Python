import psutil
import re

outPuts = psutil.net_connections("tcp")

#print outPuts


outPutList = []
pidList = {}
for outPut in outPuts:
	phonePattern = re.compile(r'[^^]*\'(\d+.\d+.\d+.\d+)\D*(\d+)[^^]*\'(\d+.\d+.\d+.\d+)\D*(\d+)\D*\'(\D+)\'\D*(\d+)')
	if(phonePattern.search(str(outPut)) != None):
		pidDetail = phonePattern.search(str(outPut)).groups();
		outPutList.append(pidDetail)
		(l, lp, r, rp, c, pid) = pidDetail
		if pid in pidList.keys():
			pidList[pid] += 1;
		else:
			pidList[pid] = 1


outPutList = sorted(outPutList, key=lambda t: int(t[5]))
outPutList = sorted(outPutList, key=lambda t: pidList[t[5]], reverse=True)

print "%5s\t%30s\t%35s\t%20s" %("pid", "laddr", "raddr", "status")
for output in outPutList:
	(l, lp, r, rp, c, pid) = output
	print "%5s\t%30s:%s\t%30s:%s\t%20s" % (pid,l,lp,r,rp,c)