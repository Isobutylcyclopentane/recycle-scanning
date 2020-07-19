"""
# This is a simple program that serves the function for locating 
# the device geologically with the external IP address of the device.
# The external IP is fetched by the AWS check ip service, and the 
# geolocation is obtained by geoip2 library. 
# 
# This program requires the GeoLite2-City.mmdb database in the same 
# directory to run. This database is from GeoLite.
# 
# ----------------------------------------
# Author: Jerry Cheng;
# ENGR-2050, Section 4, Team A, Summer 2020;
# Last Update: 2020.07.19

"""
import requests
import geoip2.database
import os

class Geoloc(object):
    def __init__(self, resp):
        self.city = resp.city.name
        self.state = resp.subdivisions.most_specific.iso_code
        self.country = resp.country.iso_code
        self.postal = resp.postal.code
        self.latitude = resp.location.latitude
        self.longitude = resp.location.longitude
        return
    
    def __str__(self):
        temp = ",".join((self.city, self.state, self.country, self.postal))
        return 

def fetch_ip():
    ip_device = requests.get("https://checkip.amazonaws.com").text.strip()
    return ip_device


def fetch_location(ip_device):
    
    reader = geoip2.database.Reader(os.getcwd())
    response = reader.city(ip_device)

    result = Geoloc(response)
    
    return result

if __name__ == "__main__":
    ip = fetch_ip()
    a = fetch_location
    print(a)
    
    