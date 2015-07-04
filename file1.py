from fingered import *
import random
import csv
import sys

def caac():
	records = random.randrange(200,500)
	inst3=Xf("r")
	inst3.setStats(records,2,(2,records/10),[-1,0],[False,False],0,40000)
	inst3.FormData()

	inst4=Xf("s")
	inst4.setStats(100,2,(2,10),[-1,0],[False,True],0,40000)
	inst4.FormData()

	print inst3
	print inst4

	#print "Predicted Cost of Fingered Join from Stats: "
	#print "recorSize of file1=" + str(records)

	pCost = inst3.getSize() + (inst4.getSize() * inst3.getRuns(1) )+ (inst3.getRuns(1) * inst4.getSize())

	#print pCost
	#print inst3.eJoin(inst4,1,1)
	#print "\n Fingered Join:"

	j=JoinReq(inst3,inst4,1,1,True)

	tup=j.pull()
	while tup is not "eoo":
		#print str(tup)

		tup=j.pull()

	#print "Cost : "  + str(j.getCost())



	"""
	print "\nNested Loop Join:\n"

	inst3.reset()
	inst4.reset()

	k=JoinReq(inst3,inst4,1,1,False)


	tup=k.pull()
	while tup is not "eoo":
		print str(tup)

		tup=k.pull()

	print "Cost : "  + str(k.getCost()) 

	"""


	print "Summary:"
	print "selected file1size: " + str(records)
	print "selected number of runs for file1: " + str(inst3.getRuns(1))
	print "Predicted Cost Finger:" + str(pCost)
	print "Actual Cost Finger:" + str(j.getCost())
	#print "Actual Cost NLJ:" + str(k.getCost())

	print "("+ str(records) +","+ str(inst3.getRuns(1)) +","+ str(inst4.getSize()) +","+ str(pCost) +","+ str(j.getCost())+")"

	tup = [ str(records), str(inst3.getRuns(1)),str(inst4.getSize()),str(pCost),str(j.getCost())]
	print tup


	fp = open("toexcel.csv","ab")

	writer = csv.writer(fp)
	data = [tup]
	writer.writerows(data)



for i in range(2):
	caac()
