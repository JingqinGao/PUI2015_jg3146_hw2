### Jingqin Gao, jg3146 ###
### Urban Informatics 2015 Homework 2 ###

import json
import sys
import urllib2

if __name__=='__main__':
 url= 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
#input KEY & Bus line number
 request = urllib2.urlopen(url) 
 BusFile = json.load(request)
 VehActivity = BusFile['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'] #use Json viewer to see the structure

print "The information below shows the locations of active MTA buses."
print "Bus Line: %s" % sys.argv[2]

i = 0 #initialize the counter for number of active buses

for bus in VehActivity:
                Lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		Long = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']                
		print "Bus %s is at latitude %s and longitude %s" % (i,Lat, Long)
		i = i+1

print "Number of Active Buses:%s" % i
