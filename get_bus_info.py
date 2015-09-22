### Jingqin Gao, jg3146 ###
### Urban Informatics 2015 Homework 2 ###

import json
import sys
import urllib2
import csv

if __name__=='__main__':
 url= 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
#input KEY & Bus line number
 request = urllib2.urlopen(url) 
 BusFile = json.load(request)
 VehActivity = BusFile['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'] #use Json viewer to see the structure

with open(sys.argv[3],'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Latitude', 'Longitude','Stop Name', 'Stop Status']) #write the csv header

	for bus in VehActivity:
                Lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		Long = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']             
		if len(bus['MonitoredVehicleJourney']['OnwardCalls']) == 0:
			StopName = 'N/A'
			StopStatus = 'N/A' 
		else:
			StopName = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
			StopStatus = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'] 
		row = [Lat, Long, StopName, StopStatus]
        	writer.writerow(row)
		# print "%s,%s,StopName:%s,Status:%s" % (Lat,Long,StopName,StopStatus)

print "Finish writing bus %s infomation into %s." % (sys.argv[2],sys.argv[3])

