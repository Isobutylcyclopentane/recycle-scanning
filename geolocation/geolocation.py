import requests
import geoip2.database
import os

class Geoloc(object):
    # storage class, read and simplify the output from geoip2 lib;
    # 1 method:
        # __str__, str, return the city location of the device;

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
        return temp

def fetch_ip():
    ## helper function, fetch the external IP address of the device with AWS check_ip service
    ## 0in; 1out: str;

    ip_device = requests.get("https://checkip.amazonaws.com").text.strip()
    return ip_device


def fetch_location(ip_device):
    # helper function, fetch the geological location through the external IP
    # with geoip2 library and its respective library;
    # 1in: str; 1out: class Geoloc
    
    temp_path = os.path.join(os.getcwd(), "GeoLite2-City.mmdb")
    reader = geoip2.database.Reader(temp_path)
    response = reader.city(ip_device)

    result = Geoloc(response)
    
    return result

def get_location():
    # packaged callable, get the location of the device via the external IP mask
    # 0in; 1out: class Geoloc;

    return fetch_location(fetch_ip())
    