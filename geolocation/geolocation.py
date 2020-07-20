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
    # storage class, read and simplify the response from the geoip2
    # library. It keeps the city, state, country, and postal code
    # from the device
    # =========================
    # This class contains 1 method:
    #   __str__(self): standard method for str output: 0in; 1out: str;

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
    # helper function, fetch the external ip of the product with 
    # AWS check ip services, return the external ip address in a
    # string
    # 0in; 1out: str;

    ip_device = requests.get("https://checkip.amazonaws.com").text.strip()
    return ip_device


def fetch_location(ip_device):
    # helper function, fetch the geolocation of the device with 
    # the given external IP, return the geolocation with a Geoloc
    # class
    # 1in: str; 1out: class Geoloc;
    
    reader = geoip2.database.Reader(os.getcwd())
    response = reader.city(ip_device)

    result = Geoloc(response)
    
    return result

def get_location():
    # packaged function for import, return the geolocation
    # of the device in a Geoloc class
    # 0in; 1out: class Geoloc
    return fetch_location(fetch_ip())


if __name__ == "__main__":
    
    # for testing ONLY, do NOT run __main__ while imported
    ip_h = fetch_ip()
    print(ip_h)
    print("DONE")
    