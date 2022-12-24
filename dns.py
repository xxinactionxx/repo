#!/usr/bin/pyhton3
import argparse, sys,subprocess,os
parser = argparse.ArgumentParser(description="This tool is for dns enumeration")
parser.add_argument("-d",type=str,help="Type DNS",required=True)
parser.add_argument("-reconall",action="store_true")
a=parser.parse_args()
def arec():
	print("---------------------------------------------------------")
	cmdrun1=subprocess.getoutput("host -t A {}".format(a.d))
	print(cmdrun1)
	cmdrun3=cmdrun1.split()
	ipadd=cmdrun3[3]
	print("----------------------------------------------------------")
	ptri=subprocess.getoutput("host -t ptr {}".format(ipadd))
	print(ptri)
def recall():
	print("---------------------------------------------------------")
	ns=subprocess.getoutput("host -t ns {}".format(a.d))
	print(ns)
	print("----------------------------------------------------------")
	mx=subprocess.getoutput("host -t mx {}".format(a.d))
	print(mx)
	print("----------------------------------------------------------")
	soa=subprocess.getoutput("host -t soa {}".format(a.d))
	print(soa)
	print("-----------------------------------------------------------")
	xm=subprocess.getoutput("host -t mx {}".format(a.d))
	xm2 = xm.split()
	k=6
	for i in xm2:
		#	print(xm2)
		if k < len(xm2):
		
			txt=subprocess.getoutput("host -t txt {}".format(xm2[k]))
			print(txt)
			k=k+7
#	print(xm[29::])
#	txt=subprocess.getoutput("host -t txt {}".format(xm[29::]))
#	txt=subproess.run("host -t ")
arec()
if a.reconall is True:
	recall()
#print(a.reconall)
