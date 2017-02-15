import psutil
import re

outPuts = psutil.net_connections("tcp")

outPutList = []
pidList = {}
for outPut in outPuts:
	outputPattern = re.compile(r'[^^]*\'(\d+.\d+.\d+.\d+)\D*(\d+)[^^]*\'(\d+.\d+.\d+.\d+)\D*(\d+)\D*\'(\D+)\'\D*(\d+)')
	if(outputPattern.search(str(outPut)) != None):
		pidDetail = outputPattern.search(str(outPut)).groups();
		outPutList.append(pidDetail)
		(l, lp, r, rp, c, pid) = pidDetail
		if pid in pidList.keys():
			pidList[pid] += 1;
		else:
			pidList[pid] = 1


outPutList = sorted(outPutList, key=lambda t: int(t[5]))
outPutList = sorted(outPutList, key=lambda t: pidList[t[5]], reverse=True)

print "%s,%s,%s,%s" %("pid", "laddr", "raddr", "status")
for output in outPutList:
	(l, lp, r, rp, c, pid) = output
	print "%s,%s:%s,%s:%s,%s" % (pid,l,lp,r,rp,c)