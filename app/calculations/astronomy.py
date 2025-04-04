

from skyfield.api import load, wgs84
import pytz
from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

# Load planetary ephemeris data
planets = load('de421.bsp')
earth = planets['earth']
tf = TimezoneFinder()

def get_sun_position(place: str, date: str):
    """
    Calculate the Sun's position for a given place and date.
    """
    geolocator = Nominatim(user_agent="panchang")
    location = geolocator.geocode(place)
    
    if not location:
        raise ValueError(f"Location {place} not found.")
    
    lat, lon = location.latitude, location.longitude
    
    # Get timezone using timezonefinder
    tz_name = tf.timezone_at(lng=lon, lat=lat)
    
    if not tz_name:
        raise ValueError(f"Could not determine timezone for {place}. Using UTC.")
    
    time_zone = pytz.timezone(tz_name)

    # Convert date string to localized datetime
    local_time = datetime.strptime(date, "%Y-%m-%d")
    local_time = time_zone.localize(local_time)

    # Get Skyfield time
    ts = load.timescale()
    t = ts.utc(local_time.year, local_time.month, local_time.day)

    observer = earth + wgs84.latlon(lat, lon)
    sun = planets['sun']
    astrometric = observer.at(t).observe(sun)

    # Get Sun's altitude and azimuth
    altitude, azimuth, _ = astrometric.apparent().altaz()

    return round(altitude.degrees, 2), round(azimuth.degrees, 2)











# from skyfield.api import load, wgs84
# import pytz
# from datetime import datetime, timedelta
# from geopy.geocoders import Nominatim
# from timezonefinder import TimezoneFinder

# # Load planetary ephemeris data
# planets = load('de421.bsp')
# earth = planets['earth']
# tf = TimezoneFinder()

# def get_sun_position(place: str, date: str):
#     """
#     Calculate the Sun's position for a given place and date.
#     """
#     geolocator = Nominatim(user_agent="panchang")
#     location = geolocator.geocode(place)
    
#     if not location:
#         raise ValueError(f"Location {place} not found.")
    
#     lat, lon = location.latitude, location.longitude
    
#     # Get timezone using timezonefinder
#     tz_name = tf.timezone_at(lng=lon, lat=lat)
    
#     if not tz_name:
#         raise ValueError(f"Could not determine timezone for {place}. Using UTC.")
    
#     time_zone = pytz.timezone(tz_name)

#     # Convert date string to localized datetime
#     local_time = datetime.strptime(date, "%Y-%m-%d")
#     local_time = time_zone.localize(local_time)

#     # Get Skyfield time
#     ts = load.timescale()
#     t = ts.utc(local_time.year, local_time.month, local_time.day)

#     observer = earth + wgs84.latlon(lat, lon)
#     sun = planets['sun']
#     astrometric = observer.at(t).observe(sun)

#     # Get Sun's altitude and azimuth
#     altitude, azimuth, _ = astrometric.apparent().altaz()

#     return round(altitude.degrees, 2), round(azimuth.degrees, 2)

# def get_sunrise_sunset(place: str, date: str):
#     """
#     Calculate the sunrise and sunset times for a given place and date.
#     """
#     geolocator = Nominatim(user_agent="panchang")
#     location = geolocator.geocode(place)
    
#     if not location:
#         raise ValueError(f"Location {place} not found.")
    
#     lat, lon = location.latitude, location.longitude
    
#     # Get timezone using timezonefinder
#     tz_name = tf.timezone_at(lng=lon, lat=lat)
    
#     if not tz_name:
#         raise ValueError(f"Could not determine timezone for {place}. Using UTC.")
    
#     time_zone = pytz.timezone(tz_name)

#     # Convert date string to localized datetime
#     local_time = datetime.strptime(date, "%Y-%m-%d")
#     local_time = time_zone.localize(local_time)

#     # Load timescale and observer location
#     ts = load.timescale()
#     observer = earth + wgs84.latlon(lat, lon)
#     sun = planets['sun']
    
#     # Define time range for searching sunrise and sunset
#     t0 = ts.utc(local_time.year, local_time.month, local_time.day, 0)
#     t1 = ts.utc(local_time.year, local_time.month, local_time.day, 23, 59, 59)
    
#     # Find sunrise and sunset times
#     eph = (earth, sun)
#     f = lambda t: observer.at(t).observe(sun).apparent().altaz()[0].degrees
#     t_sunrise, t_sunset = ts.find_discrete(t0, t1, f)
    
#     # Convert times to local timezone
#     sunrise_utc = t_sunrise.utc_datetime().replace(tzinfo=pytz.utc)
#     sunset_utc = t_sunset.utc_datetime().replace(tzinfo=pytz.utc)
    
#     sunrise_local = sunrise_utc.astimezone(time_zone)
#     sunset_local = sunset_utc.astimezone(time_zone)
    
#     return sunrise_local, sunset_local
