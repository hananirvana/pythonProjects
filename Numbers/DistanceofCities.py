"""
Distance Between Two Cities - Calculates the distance between two cities and allows
the user to specify a unit of distance. This program may require finding coordinates
for the cities like latitude and longitude.

This code only works in replit, and not in other python consoles (SSL certificate's not found).
NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with
'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
NOTE: This code will return a length that is approximately the distance.
(may not be as accurate as the actual distance)
P.S. This code is not optimized for speed.
"""

from math import radians, cos, sin, asin, sqrt  # asin is basically inverse sine
from geopy.geocoders import Nominatim

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 3956  # Radius of earth in kilometers. Use 3956 for miles.
    return c * r


def get_lat_long(cy):
    geolocator = Nominatim(user_agent="my_app")  # setting the geolocator
    location = geolocator.geocode(cy)  # grabbing location
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


if __name__ == '__main__':
    city1 = input("City1 Name: ")
    city2 = input("City2 Name: ")
    latitude1, longitude1 = get_lat_long(city1)
    latitude2, longitude2 = get_lat_long(city2)
    if latitude1 is not None and longitude1 is not None and latitude2 is not None and longitude2 is not None:
        distance = haversine(longitude1, latitude1, longitude2, latitude2)
        print(f"The distance between {city1} and {city2} is {distance} kilometers.")
    else:
        print(f"Could not find coordinates for {city1}")
        print(f"Could not find coordinates for {city2}")


