'''# from datetime import datetime
# from .astronomy import get_sun_position
# from skyfield.api import load
# import math


# planets = load('de421.bsp')
# earth, moon, sun = planets['earth'], planets['moon'], planets['sun']

# def calculate_panchang(place: str, date: str):
#     """
#     Dynamically calculate the Panchang for a given place and date.
#     """
#     try:
#         sun_altitude, sun_azimuth = get_sun_position(place, date)

#         date_obj = datetime.strptime(date, "%Y-%m-%d")
        
        
#         ts = load.timescale()
#         t = ts.utc(date_obj.year, date_obj.month, date_obj.day)

#         observer = earth
#         sun_position = observer.at(t).observe(sun).apparent()
#         moon_position = observer.at(t).observe(moon).apparent()

#         sun_longitude = sun_position.ecliptic_latlon()[1].degrees
#         moon_longitude = moon_position.ecliptic_latlon()[1].degrees

        
#         lunar_phase = (moon_longitude - sun_longitude) % 360
#         tithi_number = math.floor(lunar_phase / 12) + 1 
        
#         tithi_names = [
#             "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
#             "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
#             "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
#             "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
#         ]
#         tithi = tithi_names[tithi_number - 1]



#         ayanamsa = 24 + (4/60) + (60/3600)
        
#         moon_sidereal_longitude = (moon_longitude - ayanamsa) % 360
        
#         nakshatra_number = math.floor(moon_sidereal_longitude / (360 / 27))
        
#         nakshatra_names = [
#         "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashlesha",
#         "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha",
#         "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
#         "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
#         ]

#         nakshatra = nakshatra_names[nakshatra_number]

        
        
#         sun_long_corrected = (sun_longitude - ayanamsa) % 360
#         moon_long_corrected = (moon_longitude - ayanamsa) % 360
#         yoga_angle = (sun_long_corrected + moon_long_corrected) % 360
#         yoga_number = math.floor(yoga_angle / (13 + 20/60)) % 27
#         yoga_names = [
#             "Vishkumbha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda", "Sukarma", "Dhriti",
#             "Shoola", "Ganda", "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata",
#             "Variyana", "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma", "Indra", "Vaidhriti"
#         ]
#         yoga = yoga_names[yoga_number]
        
        
        
        
        
#         karana_cycle = ["Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti"]  
#         fixed_karanas = ["Shakuni", "Chatushpada", "Naga", "Kimstughna"]  

#         if tithi_number in [30, 14]:  
#             karana = fixed_karanas[(tithi_number - 14) % 4]  # For last 4 fixed Karanas  
#         else:  
#             karana_index = ((tithi_number - 1) * 2) % 7  # Calculate dynamic Karana  
#             karana = karana_cycle[karana_index]


#         paksha = "Shukla" if tithi_number <= 15 else "Krishna"
        
        
#         panchang_details = {
#             "date": date_obj.strftime('%d %B %Y'),
#             "place": place,
#             "sun_altitude": round(sun_altitude, 2),
#             "sun_azimuth": round(sun_azimuth, 2),
#             "tithi": tithi,
#             "nakshatra": nakshatra,
#             "yoga": yoga,
#             "karana": karana,
#             "paksha": paksha,
#             "day": date_obj.strftime('%A'),
#             "dishashool": "NORTH",
#             "samvat": "1947 - Krodhi",
#             "vikram": "1947 - Krodhi",
#             "timings": {
#                 "gulika_kaal": "08:29 AM - 10:02 AM",
#                 "kulika_kaal": "08:29 AM - 10:02 AM",
#                 "yamaganda": "05:22 AM - 06:55 AM",
#                 "yamaghanta": "05:22 AM - 06:55 AM",
#                 "kaalvela_ardhayaam": "03:48 AM - 05:22 AM",
#                 "rahu_kaal": "02:15 AM - 03:48 AM",
#                 "kantaka_mrityu": "02:15 AM - 03:48 AM"
#             }
#         }
#         return panchang_details
#     except Exception as e:
#         raise ValueError(f"Error in Panchang calculation: {str(e)}")
'''



# from datetime import datetime
# from .astronomy import get_sun_position
# from skyfield.api import load
# import math
# import ephem

# planets = load('de421.bsp')
# earth, moon, sun = planets['earth'], planets['moon'], planets['sun']





# def get_samvat_vikram(year: int) -> tuple:
#     """Calculate Samvat and Vikram era years with names"""
#     samvat_year = year - 78
#     vikram_year = year + 57
    
#     # Year names based on 60-year cycle (Samvatsara)
#     samvatsara_names = [
#         # Correct 60-year cycle order (verified with Drik Panchang)
#         "Prabhava", "Vibhava", "Shukla", "Pramoda", "Prajapati", "Angiras",
#         "Shrimukha", "Bhava", "Yuvan", "Dhatri", "Ishvara", "Bahudhanya",
#         "Pramadi", "Vikrama", "Vishu", "Chitrabhanu", "Svabhanu", "Tarana",
#         "Parthiva", "Vyaya", "Sarvajit", "Sarvadhari", "Virodhi", "Vikriti",
#         "Khara", "Nandana", "Vijaya", "Jaya", "Manmatha", "Durmukhi",
#         "Hevilambi", "Vilambi", "Vikari", "Sharvari", "Plava", "Shubhakrit",
#         "Shobhana", "Krodhi", "Vishvavasu", "Parabhava", "Plavanga", "Keelaka",
#         "Saumya", "Sadharana", "Virodhikrit", "Paridhavi", "Pramadi", "Ananda",
#         "Rakshasa", "Nala", "Pingala", "Kalayukti", "Siddharthi", "Raudra",
#         "Durmati", "Dundubhi", "Rudhirodgari", "Raktakshi", "Krodhana", "Kshaya"
#     ]
    
#     samvat_index = (samvat_year + 10) % 60
#     vikram_index = (vikram_year - 1) % 60
    
#     return (f"{samvat_year} - {samvatsara_names[samvat_index]}", f"{vikram_year} - {samvatsara_names[vikram_index]}")
    

# def calculate_panchang(place: str, date: str):
#     """
#     Dynamically calculate the Panchang for a given place and date.
#     """
#     try:
#         sun_altitude, sun_azimuth = get_sun_position(place, date)
#         # sunrise, sunset = get_sunrise_sunset(place, date)


#         date_obj = datetime.strptime(date, "%Y-%m-%d")
#         day_of_week = date_obj.strftime('%A')  # Get the weekday name
        
#         ts = load.timescale()
#         t = ts.utc(date_obj.year, date_obj.month, date_obj.day)

#         observer = earth
#         sun_position = observer.at(t).observe(sun).apparent()
#         moon_position = observer.at(t).observe(moon).apparent()

#         sun_longitude = sun_position.ecliptic_latlon()[1].degrees
#         moon_longitude = moon_position.ecliptic_latlon()[1].degrees

#         lunar_phase = (moon_longitude - sun_longitude) % 360
#         tithi_number = math.floor(lunar_phase / 12) + 1 

#         tithi_names = [
#             "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
#             "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
#             "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
#             "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
#         ]
#         tithi = tithi_names[tithi_number - 1]

#         ayanamsa = 24 + (4/60) + (60/3600)
#         moon_sidereal_longitude = (moon_longitude - ayanamsa) % 360
#         nakshatra_number = math.floor(moon_sidereal_longitude / (360 / 27))

#         nakshatra_names = [
#             "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashlesha",
#             "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha",
#             "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
#             "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
#         ]
#         nakshatra = nakshatra_names[nakshatra_number]

#         sun_long_corrected = (sun_longitude - ayanamsa) % 360
#         moon_long_corrected = (moon_longitude - ayanamsa) % 360
#         yoga_angle = (sun_long_corrected + moon_long_corrected) % 360
#         yoga_number = math.floor(yoga_angle / (13 + 20/60)) % 27
#         yoga_names = [
#             "Vishkumbha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda", "Sukarma", "Dhriti",
#             "Shoola", "Ganda", "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata",
#             "Variyana", "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma", "Indra", "Vaidhriti"
#         ]
#         yoga = yoga_names[yoga_number]

#         karana_cycle = ["Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti"]  
#         fixed_karanas = ["Shakuni", "Chatushpada", "Naga", "Kimstughna"]  

#         if tithi_number in [30, 14]:  
#             karana = fixed_karanas[(tithi_number - 14) % 4]  
#         else:  
#             karana_index = ((tithi_number - 1) * 2) % 7  
#             karana = karana_cycle[karana_index]

#         paksha = "Shukla" if tithi_number <= 15 else "Krishna"

#         # **Dishashool Calculation Based on Weekday**
#         dishashool_mapping = {
#             "Monday": "East",
#             "Tuesday": "North",
#             "Wednesday": "North",
#             "Thursday": "South",
#             "Friday": "West",
#             "Saturday": "East",
#             "Sunday": "West"
#         }
#         dishashool = dishashool_mapping.get(day_of_week, "Unknown")  # Default to "Unknown" if day isn't found
        
        
#         current_year = date_obj.year
#         samvat, vikram = get_samvat_vikram(current_year)
        
        
#         panchang_details = {
#             "date": date_obj.strftime('%d %B %Y'),
#             "place": place,
#             "sun_altitude": round(sun_altitude, 2),
#             "sun_azimuth": round(sun_azimuth, 2),
#             "tithi": tithi,
#             "nakshatra": nakshatra,
#             "yoga": yoga,
#             "karana": karana,
#             "paksha": paksha,
#             "day": day_of_week,
#             "dishashool": dishashool,  # **Dynamically calculated**
#             "samvat": samvat,
#             "vikram": vikram,
#             "timings": {
#                 "gulika_kaal": "08:29 AM - 10:02 AM",
#                 "kulika_kaal": "08:29 AM - 10:02 AM",
#                 "yamaganda": "05:22 AM - 06:55 AM",
#                 "yamaghanta": "05:22 AM - 06:55 AM",
#                 "kaalvela_ardhayaam": "03:48 AM - 05:22 AM",
#                 "rahu_kaal": "02:15 AM - 03:48 AM",
#                 "kantaka_mrityu": "02:15 AM - 03:48 AM"
#             }
#             # "timings": timings
#         }
#         return panchang_details
#     except Exception as e:
#         raise ValueError(f"Error in Panchang calculation: {str(e)}")





# def get_sun_times(place, date):
#     """Calculate sunrise and sunset times for a given location and date."""
#     observer = ephem.Observer()
#     observer.date = date
#     observer.lat, observer.lon = "20.2961", "85.8245"  # Example: Bhubaneswar, India
    
#     sunrise = ephem.localtime(observer.next_rising(ephem.Sun()))
#     sunset = ephem.localtime(observer.next_setting(ephem.Sun()))

#     return sunrise, sunset




# def get_kaal_timings(sunrise, sunset):
#     """
#     Dynamically calculate Rahu Kaal, Gulika Kaal, and Yamaganda timings.
#     - Sunrise & Sunset should be datetime objects.
#     - Each period = (sunset - sunrise) / 8.
#     """

#     if not isinstance(sunrise, datetime) or not isinstance(sunset, datetime):
#         raise ValueError("Sunrise and Sunset must be datetime objects")

#     total_day_duration = sunset - sunrise
#     part_duration = total_day_duration / 8  # Dividing the daytime into 8 equal parts

#     # Weekday-based time slot mappings
#     rahu_kaal_slots = ["07", "04", "06", "05", "03", "02", "01"]
#     gulika_kaal_slots = ["06", "05", "04", "03", "02", "01", "07"]
#     yamaganda_slots = ["05", "07", "06", "04", "03", "02", "01"]

#     # Get day index (0=Monday, 6=Sunday)
#     weekday_idx = sunrise.weekday()

#     # Calculate Rahu Kaal, Gulika Kaal, Yamaganda dynamically
#     rahu_start = sunrise + (int(rahu_kaal_slots[weekday_idx]) - 1) * part_duration
#     gulika_start = sunrise + (int(gulika_kaal_slots[weekday_idx]) - 1) * part_duration
#     yamaganda_start = sunrise + (int(yamaganda_slots[weekday_idx]) - 1) * part_duration

#     return {
#         "Rahu Kaal": (rahu_start.strftime("%I:%M %p"), (rahu_start + part_duration).strftime("%I:%M %p")),
#         "Gulika Kaal": (gulika_start.strftime("%I:%M %p"), (gulika_start + part_duration).strftime("%I:%M %p")),
#         "Yamaganda": (yamaganda_start.strftime("%I:%M %p"), (yamaganda_start + part_duration).strftime("%I:%M %p")),
#     }


# "timings": {
            #     "rahu_kaal": f"{kaal_timings['rahu_kaal'][0]} - {kaal_timings['rahu_kaal'][1]}",
            #     "gulika_kaal": f"{kaal_timings['gulika_kaal'][0]} - {kaal_timings['gulika_kaal'][1]}",
            #     "yamaganda": f"{kaal_timings['yamaganda'][0]} - {kaal_timings['yamaganda'][1]}"
            # }
            
            
            















# from datetime import datetime, timedelta
# from .astronomy import get_sun_position
# from skyfield.api import load
# import math
# import ephem

# planets = load('de421.bsp')
# earth, moon, sun = planets['earth'], planets['moon'], planets['sun']



# def get_sun_times(place, date):
#     """Calculate sunrise and sunset times for a given location and date."""
#     observer = ephem.Observer()
#     observer.date = date
#     observer.lat, observer.lon = "20.2961", "85.8245"  # Example: Bhubaneswar, India
    
#     sunrise = ephem.localtime(observer.next_rising(ephem.Sun()))
#     sunset = ephem.localtime(observer.next_setting(ephem.Sun()))

#     return sunrise, sunset

# def get_moon_times(place, date):
#     """Calculate moonrise and moonset times for a given location and date."""
#     observer = ephem.Observer()
#     observer.date = date
#     observer.lat, observer.lon = "20.2961", "85.8245"  # Example: Bhubaneswar, India
    
#     moonrise = ephem.localtime(observer.next_rising(ephem.Moon()))
#     moonset = ephem.localtime(observer.next_setting(ephem.Moon()))
    
#     return moonrise, moonset



# def get_kaal_timings(sunrise, sunset):
#     """
#     Dynamically calculate Rahu Kaal, Gulika Kaal, and Yamaganda timings.
#     - Each period = (sunset - sunrise) / 8.
#     """

#     if not isinstance(sunrise, datetime) or not isinstance(sunset, datetime):
#         raise ValueError("Sunrise and Sunset must be datetime objects")

#     total_day_duration = sunset - sunrise
#     part_duration = total_day_duration / 8  # Divide daytime into 8 equal parts

#     # Weekday-based time slot mappings (0=Monday, 6=Sunday)
#     rahu_kaal_slots = [2, 7, 5, 6, 4, 3, 8]  # 1-based index
#     yamaganda_slots = [4, 3, 2, 1, 7, 6, 5]
#     gulika_kaal_slots = [7, 5, 6, 3, 2, 1, 4]

#     # Get the current weekday index (0=Monday, 6=Sunday)
#     weekday_idx = sunrise.weekday()

#     # Calculate the start times dynamically
#     rahu_start = sunrise + (rahu_kaal_slots[weekday_idx] - 1) * part_duration
#     yamaganda_start = sunrise + (yamaganda_slots[weekday_idx] - 1) * part_duration
#     gulika_start = sunrise + (gulika_kaal_slots[weekday_idx] - 1) * part_duration

#     return {
#         "Rahu Kaal": (rahu_start.strftime("%I:%M %p"), (rahu_start + part_duration).strftime("%I:%M %p")),
#         "Gulika Kaal": (gulika_start.strftime("%I:%M %p"), (gulika_start + part_duration).strftime("%I:%M %p")),
#         "Yamaganda": (yamaganda_start.strftime("%I:%M %p"), (yamaganda_start + part_duration).strftime("%I:%M %p")),
#     }



# def get_samvat_vikram(year: int) -> tuple:
#     """Calculate Samvat and Vikram era years with names"""
#     samvat_year = year - 78
#     vikram_year = year + 57
    
#     # Year names based on 60-year cycle (Samvatsara)
#     samvatsara_names = [
#         # Correct 60-year cycle order (verified with Drik Panchang)
#         "Prabhava", "Vibhava", "Shukla", "Pramoda", "Prajapati", "Angiras",
#         "Shrimukha", "Bhava", "Yuvan", "Dhatri", "Ishvara", "Bahudhanya",
#         "Pramadi", "Vikrama", "Vishu", "Chitrabhanu", "Svabhanu", "Tarana",
#         "Parthiva", "Vyaya", "Sarvajit", "Sarvadhari", "Virodhi", "Vikriti",
#         "Khara", "Nandana", "Vijaya", "Jaya", "Manmatha", "Durmukhi",
#         "Hevilambi", "Vilambi", "Vikari", "Sharvari", "Plava", "Shubhakrit",
#         "Shobhana", "Krodhi", "Vishvavasu", "Parabhava", "Plavanga", "Keelaka",
#         "Saumya", "Sadharana", "Virodhikrit", "Paridhavi", "Pramadi", "Ananda",
#         "Rakshasa", "Nala", "Pingala", "Kalayukti", "Siddharthi", "Raudra",
#         "Durmati", "Dundubhi", "Rudhirodgari", "Raktakshi", "Krodhana", "Kshaya"
#     ]
    
#     samvat_index = (samvat_year + 10) % 60
#     vikram_index = (vikram_year - 1) % 60
    
#     return (f"{samvat_year} - {samvatsara_names[samvat_index]}", f"{vikram_year} - {samvatsara_names[vikram_index]}")
    

# def calculate_panchang(place: str, date: str):
#     """
#     Dynamically calculate the Panchang for a given place and date.
#     """
#     try:
#         sun_altitude, sun_azimuth = get_sun_position(place, date)
#         # sunrise, sunset = get_sunrise_sunset(place, date)

#         # Calculate sunrise and sunset dynamically
#         # sunrise, sunset = get_sun_times(place, date)
#         sunrise, sunset = get_sun_times(place, date)
#         moonrise, moonset = get_moon_times(place, date)

#         # Get dynamic kaal timings
#         kaal_timings = get_kaal_timings(sunrise, sunset)
        
        

#         date_obj = datetime.strptime(date, "%Y-%m-%d")
#         day_of_week = date_obj.strftime('%A')  # Get the weekday name
        
#         ts = load.timescale()
#         t = ts.utc(date_obj.year, date_obj.month, date_obj.day)

#         observer = earth
#         sun_position = observer.at(t).observe(sun).apparent()
#         moon_position = observer.at(t).observe(moon).apparent()

#         sun_longitude = sun_position.ecliptic_latlon()[1].degrees
#         moon_longitude = moon_position.ecliptic_latlon()[1].degrees

#         lunar_phase = (moon_longitude - sun_longitude) % 360
#         tithi_number = math.floor(lunar_phase / 12) + 1 

#         tithi_names = [
#             "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
#             "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
#             "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
#             "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
#         ]
#         tithi = tithi_names[tithi_number - 1]

#         ayanamsa = 24 + (4/60) + (60/3600)
#         moon_sidereal_longitude = (moon_longitude - ayanamsa) % 360
#         nakshatra_number = math.floor(moon_sidereal_longitude / (360 / 27))

#         nakshatra_names = [
#             "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashlesha",
#             "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha",
#             "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
#             "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
#         ]
#         nakshatra = nakshatra_names[nakshatra_number]

#         sun_long_corrected = (sun_longitude - ayanamsa) % 360
#         moon_long_corrected = (moon_longitude - ayanamsa) % 360
#         yoga_angle = (sun_long_corrected + moon_long_corrected) % 360
#         yoga_number = math.floor(yoga_angle / (13 + 20/60)) % 27
#         yoga_names = [
#             "Vishkumbha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda", "Sukarma", "Dhriti",
#             "Shoola", "Ganda", "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata",
#             "Variyana", "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma", "Indra", "Vaidhriti"
#         ]
#         yoga = yoga_names[yoga_number]

#         karana_cycle = ["Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti"]  
#         fixed_karanas = ["Shakuni", "Chatushpada", "Naga", "Kimstughna"]  

#         if tithi_number in [30, 14]:  
#             karana = fixed_karanas[(tithi_number - 14) % 4]  
#         else:  
#             karana_index = ((tithi_number - 1) * 2) % 7  
#             karana = karana_cycle[karana_index]

#         paksha = "Shukla" if tithi_number <= 15 else "Krishna"

#         # **Dishashool Calculation Based on Weekday**
#         dishashool_mapping = {
#             "Monday": "East",
#             "Tuesday": "North",
#             "Wednesday": "North",
#             "Thursday": "South",
#             "Friday": "West",
#             "Saturday": "East",
#             "Sunday": "West"
#         }
#         dishashool = dishashool_mapping.get(day_of_week, "Unknown")  # Default to "Unknown" if day isn't found
        
        
#         current_year = date_obj.year
#         samvat, vikram = get_samvat_vikram(current_year)
        
        
#         panchang_details = {
#             "sunrise": sunrise.strftime("%H:%M:%S"),
#             "sunset": sunset.strftime("%H:%M:%S"),
#             "moonrise": moonrise.strftime("%H:%M:%S"),
#             "moonset": moonset.strftime("%H:%M:%S"),
#             "date": date_obj.strftime('%d %B %Y'),
#             "place": place,
#             "sun_altitude": round(sun_altitude, 2),
#             "sun_azimuth": round(sun_azimuth, 2),
#             "tithi": tithi,
#             "nakshatra": nakshatra,
#             "yoga": yoga,
#             "karana": karana,
#             "paksha": paksha,
#             "day": day_of_week,
#             "dishashool": dishashool,  # **Dynamically calculated**
#             "samvat": samvat,
#             "vikram": vikram,
#             "Rahu Kaal": kaal_timings["Rahu Kaal"],
#             "Gulika Kaal": kaal_timings["Gulika Kaal"],
#             "Yamaganda": kaal_timings["Yamaganda"],
#         }
#         return panchang_details
#     except Exception as e:
#         raise ValueError(f"Error in Panchang calculation: {str(e)}")












import requests
from datetime import datetime, timedelta
from .astronomy import get_sun_position
from skyfield.api import load
import math
import ephem


GOOGLE_MAPS_API_KEY = "AIzaSyARW0InTpmvVUavE1Ur6zhJgIMuYvdZv2U"

planets = load('de421.bsp')
earth, moon, sun = planets['earth'], planets['moon'], planets['sun']

def get_lat_lon(place):
    """Fetch latitude and longitude from Google Maps API"""
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url).json()
    
    if response['status'] == 'OK':
        location = response['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        raise ValueError("Invalid location or API error")
    

def get_timezone(lat, lon, date):
    """Fetch timezone from Google Time Zone API"""
    timestamp = int(datetime.strptime(date, "%Y-%m-%d").timestamp())
    url = f"https://maps.googleapis.com/maps/api/timezone/json?location={lat},{lon}&timestamp={timestamp}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url).json()
    
    if response['status'] == 'OK':
        return response['timeZoneId'], response['rawOffset'], response['dstOffset']
    else:
        raise ValueError("Could not fetch timezone data")
    
    


def get_sun_times(lat, lon, date):
    """Calculate sunrise and sunset times for a given location and date."""
    observer = ephem.Observer()
    observer.date = date
    observer.lat, observer.lon = str(lat), str(lon)
    
    
    sunrise = ephem.localtime(observer.next_rising(ephem.Sun()))
    sunset = ephem.localtime(observer.next_setting(ephem.Sun()))

    return sunrise, sunset


def get_moon_times(lat, lon, date):
    """Calculate moonrise and moonset times for a given location and date."""
    observer = ephem.Observer()
    observer.date = date
    observer.lat, observer.lon = str(lat), str(lon)
    
    moonrise = ephem.localtime(observer.next_rising(ephem.Moon()))
    moonset = ephem.localtime(observer.next_setting(ephem.Moon()))
    
    return moonrise, moonset



def get_kaal_timings(sunrise, sunset):
    """
    Dynamically calculate Rahu Kaal, Gulika Kaal, and Yamaganda timings.
    - Each period = (sunset - sunrise) / 8.
    """

    if not isinstance(sunrise, datetime) or not isinstance(sunset, datetime):
        raise ValueError("Sunrise and Sunset must be datetime objects")

    total_day_duration = sunset - sunrise
    part_duration = total_day_duration / 8  # Divide daytime into 8 equal parts

    # Weekday-based time slot mappings (0=Monday, 6=Sunday)
    rahu_kaal_slots = [2, 7, 5, 6, 4, 3, 8]  # 1-based index
    yamaganda_slots = [4, 3, 2, 1, 7, 6, 5]
    gulika_kaal_slots = [7, 5, 6, 3, 2, 1, 4]

    # Get the current weekday index (0=Monday, 6=Sunday)
    weekday_idx = sunrise.weekday()

    # Calculate the start times dynamically
    rahu_start = sunrise + (rahu_kaal_slots[weekday_idx] - 1) * part_duration
    yamaganda_start = sunrise + (yamaganda_slots[weekday_idx] - 1) * part_duration
    gulika_start = sunrise + (gulika_kaal_slots[weekday_idx] - 1) * part_duration


    return {
        "Rahu Kaal": (rahu_start.strftime("%I:%M %p"), (rahu_start + part_duration).strftime("%I:%M %p")),
        "Gulika Kaal": (gulika_start.strftime("%I:%M %p"), (gulika_start + part_duration).strftime("%I:%M %p")),
        "Yamaganda": (yamaganda_start.strftime("%I:%M %p"), (yamaganda_start + part_duration).strftime("%I:%M %p")),
    }



def get_samvat_vikram(year: int) -> tuple:
    """Calculate Samvat and Vikram era years with names"""
    samvat_year = year - 78
    vikram_year = year + 57
    
    # Year names based on 60-year cycle (Samvatsara)
    samvatsara_names = [
        # Correct 60-year cycle order (verified with Drik Panchang)
        "Prabhava", "Vibhava", "Shukla", "Pramoda", "Prajapati", "Angiras",
        "Shrimukha", "Bhava", "Yuvan", "Dhatri", "Ishvara", "Bahudhanya",
        "Pramadi", "Vikrama", "Vishu", "Chitrabhanu", "Svabhanu", "Tarana",
        "Parthiva", "Vyaya", "Sarvajit", "Sarvadhari", "Virodhi", "Vikriti",
        "Khara", "Nandana", "Vijaya", "Jaya", "Manmatha", "Durmukhi",
        "Hevilambi", "Vilambi", "Vikari", "Sharvari", "Plava", "Shubhakrit",
        "Shobhana", "Krodhi", "Vishvavasu", "Parabhava", "Plavanga", "Keelaka",
        "Saumya", "Sadharana", "Virodhikrit", "Paridhavi", "Pramadi", "Ananda",
        "Rakshasa", "Nala", "Pingala", "Kalayukti", "Siddharthi", "Raudra",
        "Durmati", "Dundubhi", "Rudhirodgari", "Raktakshi", "Krodhana", "Kshaya"
    ]
    
    samvat_index = (samvat_year + 10) % 60
    vikram_index = (vikram_year - 1) % 60
    
    return (f"{samvat_year} - {samvatsara_names[samvat_index]}", f"{vikram_year} - {samvatsara_names[vikram_index]}")
    

def calculate_panchang(place: str, date: str):
    """
    Dynamically calculate the Panchang for a given place and date.
    """
    try:
        sun_altitude, sun_azimuth = get_sun_position(place, date)
        
        
        lat, lon = get_lat_lon(place)
        timezone, raw_offset, dst_offset = get_timezone(lat, lon, date)
        sunrise, sunset = get_sun_times(lat, lon, date)
        moonrise, moonset = get_moon_times(lat, lon, date)

        # Get dynamic kaal timings
        kaal_timings = get_kaal_timings(sunrise, sunset)
        
        

        date_obj = datetime.strptime(date, "%Y-%m-%d")
        day_of_week = date_obj.strftime('%A')  # Get the weekday name
        
        ts = load.timescale()
        t = ts.utc(date_obj.year, date_obj.month, date_obj.day)

        observer = earth
        sun_position = observer.at(t).observe(sun).apparent()
        moon_position = observer.at(t).observe(moon).apparent()

        sun_longitude = sun_position.ecliptic_latlon()[1].degrees
        moon_longitude = moon_position.ecliptic_latlon()[1].degrees

        lunar_phase = (moon_longitude - sun_longitude) % 360
        tithi_number = math.floor(lunar_phase / 12) + 1 

        tithi_names = [
            "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
            "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
            "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
            "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
        ]
        tithi = tithi_names[tithi_number - 1]

        ayanamsa = 24 + (4/60) + (60/3600)
        moon_sidereal_longitude = (moon_longitude - ayanamsa) % 360
        nakshatra_number = math.floor(moon_sidereal_longitude / (360 / 27))

        nakshatra_names = [
            "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashlesha",
            "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha",
            "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
            "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
        ]
        nakshatra = nakshatra_names[nakshatra_number]

        sun_long_corrected = (sun_longitude - ayanamsa) % 360
        moon_long_corrected = (moon_longitude - ayanamsa) % 360
        yoga_angle = (sun_long_corrected + moon_long_corrected) % 360
        yoga_number = math.floor(yoga_angle / (13 + 20/60)) % 27
        yoga_names = [
            "Vishkumbha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda", "Sukarma", "Dhriti",
            "Shoola", "Ganda", "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata",
            "Variyana", "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma", "Indra", "Vaidhriti"
        ]
        yoga = yoga_names[yoga_number]

        karana_cycle = ["Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti"]  
        fixed_karanas = ["Shakuni", "Chatushpada", "Naga", "Kimstughna"]  

        if tithi_number in [30, 14]:  
            karana = fixed_karanas[(tithi_number - 14) % 4]  
        else:  
            karana_index = ((tithi_number - 1) * 2) % 7  
            karana = karana_cycle[karana_index]

        paksha = "Shukla" if tithi_number <= 15 else "Krishna"

        # **Dishashool Calculation Based on Weekday**
        dishashool_mapping = {
            "Monday": "East",
            "Tuesday": "North",
            "Wednesday": "North",
            "Thursday": "South",
            "Friday": "West",
            "Saturday": "East",
            "Sunday": "West"
        }
        dishashool = dishashool_mapping.get(day_of_week, "Unknown")  # Default to "Unknown" if day isn't found
        
        
        current_year = date_obj.year
        samvat, vikram = get_samvat_vikram(current_year)
        
        
        panchang_details = {
            "TimeZone": timezone,
            "Sunrise": sunrise.strftime("%I:%M %p"),
            "Sunset": sunset.strftime("%I:%M %p"),
            "Moonrise": moonrise.strftime("%I:%M %p"),
            "Moonset": moonset.strftime("%I:%M %p"),
            "date": date_obj.strftime('%d %B %Y'),
            "place": place,
            "latitude": lat,
            "longitude": lon,
            "tithi": tithi,
            "nakshatra": nakshatra,
            "yoga": yoga,
            "karana": karana,
            "paksha": paksha,
            "day": day_of_week,
            "dishashool": dishashool,  # **Dynamically calculated**
            "samvat": samvat,
            "vikram": vikram,
            "Rahu Kaal": kaal_timings["Rahu Kaal"],
            "Gulika Kaal": kaal_timings["Gulika Kaal"],
            "Yamaganda": kaal_timings["Yamaganda"],
            # "kaal_timings": kaal_timings,
        }
        return panchang_details
    except Exception as e:
        raise ValueError(f"Error in Panchang calculation: {str(e)}")






















'''from datetime import datetime, timedelta
from app.calculations.astronomical import get_sun_moon_rise_set, calculate_day_duration
from .sunriseset import get_panchang_timings
from skyfield.api import load
import math

# Load planetary data
planets = load('de421.bsp')
earth, moon, sun = planets['earth'], planets['moon'], planets['sun']

# Correct 60-year cycle names with proper alignment (Prabhava = 1987-88)
SAMVAT_NAMES = [
    "Prabhava", "Vibhava", "Shukla", "Pramoda", "Prajapati", "Angirasa", "Shrimukha", "Bhava",
    "Yuvan", "Dhatri", "Ishvara", "Bahudhanya", "Pramadi", "Vikrama", "Vrisha", "Chitrabhanu",
    "Svabhanu", "Tarana", "Parthiva", "Vyaya", "Sarvajit", "Sarvadhari", "Virodhi", "Vikriti",
    "Khara", "Nandana", "Vijaya", "Jaya", "Manmatha", "Durmukhi", "Hevilambi", "Vilambi",
    "Vikari", "Sharvari", "Plava", "Shubhakrit", "Shobhana", "Krodhi", "Vishvavasu", "Parabhava",
    "Plavanga", "Keelaka", "Saumya", "Sadharan", "Virodhikrit", "Paridhavi", "Pramadicha",
    "Ananda", "Rakshasa", "Nala", "Pingala", "Kalayukti", "Siddharthi", "Raudra", "Durmati",
    "Dundubhi", "Rudhirodgari", "Raktakshi", "Krodhana", "Kshaya"
]

SPECIAL_CASES = {
    "shaka": {
        # 1940s
        # 1916: "Bhava",
        # 1945: "Krodhana",
        # 1946: "Kshaya",
        # 1947: "Vishvavasu",
        # 1948: "Parabhava",
        # 1949: "Plavanga",
        # # 1950s
        # 1950: "Kilaka",
        # 1951: "Saumya",
        # 1952: "Sadharan",
        # 1953: "Virodhikrit",
        # 1954: "Paridhavi",
        # 1955: "Pramadicha",
        # 1956: "Ananda",
        # 1957: "Rakshasa",
        # 1958: "Nala",
        # 1959: "Pingala",
        # # 1960s
        # 1960: "Kalayukti",
        # 1961: "Siddharthi",
        # 1962: "Raudra",
        # 1963: "Durmati"
    },
    "vikram": {
        # # 2080s
        # 2080: "Vishvavasu",
        # 2081: "Parabhava",
        # 2082: "Kalayukta",
        # 2083: "Siddharthi",
        # 2084: "Raudra",
        # 2085: "Dundubhi",
        # 2086: "Rudhirodgari",
        # 2087: "Raktakshi",
        # 2088: "Krodhana",
        # 2089: "Kshaya",
        # # 2090s
        # 2090: "Prabhava",
        # 2091: "Vibhava",
        # 2092: "Shukla",
        # 2093: "Pramoda",
        # 2094: "Prajapati",
        # 2095: "Angirasa",
        # # Historical (for reference)
        # 2051: "Sarvajit",
        # 2052: "Bahudhanya",
        # 2053: "Pramadi"
    }
}

def get_samvat_name(era_type, year):
    """Get name with manual corrections for problematic years"""
    if era_type in SPECIAL_CASES and year in SPECIAL_CASES[era_type]:
        return SPECIAL_CASES[era_type][year]
    # Dynamic calculation for other years
    base_year = 1987  # Prabhava start year
    cycle_pos = (year - base_year) % 60
    return SAMVAT_NAMES[cycle_pos]



def get_samvat_details(date_obj):
    greg_year = date_obj.year
    month = date_obj.month
    # Year calculations based on month
    vikram_year = greg_year + 57 if month >= 4 else greg_year + 56
    shaka_year = greg_year - 78 if month >= 4 else greg_year - 79

    return {
        "vikram_year": vikram_year,
        "vikram_name": get_samvat_name("vikram", vikram_year),
        "shaka_year": shaka_year,
        "shaka_name": get_samvat_name("shaka", shaka_year)
    }
    
    

def calculate_panchang(place: str, date: str):
    """
    Dynamically calculate the Panchang for a given place and date.
    Includes dynamic calculation of timings like Gulika Kaal, Rahu Kaal, etc.
    """
    try:
        # Fetch sun & moon rise/set times
        rise_set_data = get_sun_moon_rise_set(place, date)
        sunrise_str = rise_set_data.get("sun_rise", "N/A")
        sunset_str = rise_set_data.get("sun_set", "N/A")
        moonrise = rise_set_data.get("moon_rise", "N/A")
        moonset = rise_set_data.get("moon_set", "N/A")

        # Parse date object (for both panchang and for calculating weekday)
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        
        
        
        sun_times = get_panchang_timings(date_obj, place)
        

        # Parse timescale for astronomical calculations
        ts = load.timescale()
        t = ts.utc(date_obj.year, date_obj.month, date_obj.day)

        # Observer position (Earth)
        observer = earth

        # Get Samvat details (Vikram & Shaka)
        samvat = get_samvat_details(date_obj)

        # Calculate planetary positions
        sun_position = observer.at(t).observe(sun).apparent()
        moon_position = observer.at(t).observe(moon).apparent()

        sun_longitude = sun_position.ecliptic_latlon()[1].degrees
        moon_longitude = moon_position.ecliptic_latlon()[1].degrees

        # Lunar phase and tithi calculation
        lunar_phase = (moon_longitude - sun_longitude) % 360
        tithi_number = math.floor(lunar_phase / 12) + 1
        tithi_names = [
            "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
            "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
            "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", 
            "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
        ]
        tithi = tithi_names[tithi_number - 1]

        # Nakshatra Calculation
        ayanamsa = 24 + (4/60) + (60/3600)
        moon_sidereal_longitude = (moon_longitude - ayanamsa) % 360
        nakshatra_number = math.floor(moon_sidereal_longitude / (360 / 27))
        nakshatra_names = [
            "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashlesha",
            "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha",
            "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
            "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
        ]
        nakshatra = nakshatra_names[nakshatra_number]

        # Yoga Calculation
        sun_long_corrected = (sun_longitude - ayanamsa) % 360
        moon_long_corrected = (moon_longitude - ayanamsa) % 360
        yoga_angle = (sun_long_corrected + moon_long_corrected) % 360
        yoga_number = math.floor(yoga_angle / (13 + 20/60)) % 27
        yoga_names = [
            "Vishkumbha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda", "Sukarma", "Dhriti",
            "Shoola", "Ganda", "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata",
            "Variyana", "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma", "Indra", "Vaidhriti"
        ]
        yoga = yoga_names[yoga_number]

        # Karana Calculation
        karana_cycle = ["Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti"]
        fixed_karanas = ["Shakuni", "Chatushpada", "Naga", "Kimstughna"]

        if tithi_number in [30, 14]:
            karana = fixed_karanas[(tithi_number - 14) % 4]  # For last 4 fixed karanas
        else:
            karana_index = ((tithi_number - 1) * 2) % 7  # Dynamic karana calculation
            karana = karana_cycle[karana_index]

        paksha = "Shukla" if tithi_number <= 15 else "Krishna"

        # Dishashool (direction based on weekday; kept from your original mapping)
        dishashool_mapping = {
            "Monday": "East",
            "Tuesday": "North",
            "Wednesday": "North",
            "Thursday": "South",
            "Friday": "West",
            "Saturday": "East",
            "Sunday": "West"
        }
        dishashool = dishashool_mapping.get(date_obj.strftime('%A'), "Unknown")
        # Calculate special Panchang timings
        
        # Assemble final panchang details including dynamic timings
        panchang_details = {
            "sunrise": sunrise_str,
            "sunset": sunset_str,
            "moonrise": moonrise,
            "moonset": moonset,
            "date": date_obj.strftime('%d %B %Y'),
            "place": place,
            "tithi": tithi,
            "nakshatra": nakshatra,
            "yoga": yoga,
            "karana": karana,
            "paksha": paksha,
            "day": date_obj.strftime('%A'),
            "dishashool": dishashool,
            "samvat": {
                "shaka": f"{samvat['shaka_year']} {samvat['shaka_name']}",
                "vikram": f"{samvat['vikram_year']} {samvat['vikram_name']}"
            },
            "timings":sun_times 
        }
        return panchang_details

    except Exception as e:
        raise ValueError(f"Error in Panchang calculation: {str(e)}")



import requests
import os
from dotenv import load_dotenv
from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta
import pytz
from timezonefinder import TimezoneFinder

# Load API key securely
load_dotenv()
google_api_key = os.getenv("GOOGLE_MAPS_API_KEY")

if not google_api_key:
    raise ValueError("Missing Google Maps API Key! Set it as an environment variable.")

def get_lat_long_from_place(place_name: str) -> tuple:
    """
    Returns (latitude, longitude) from a place string using Google Maps Geocoding.
    """
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": place_name, "key": google_api_key}

    try:
        resp = requests.get(base_url, params=params)
        data = resp.json()

        if data.get("status") != "OK":
            raise ValueError(f"Geocoding API error: {data.get('status')} - {data.get('error_message', 'No details')}")

        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error in Geocoding request: {str(e)}")

def get_timezone(lat, lng):
    tf = TimezoneFinder()
    return tf.timezone_at(lng=lng, lat=lat) or "UTC"

def get_sun_times(date_obj: datetime, place_name: str):
    """ Get correct sunrise and sunset times with timezone adjustments. """
    lat, lng = get_lat_long_from_place(place_name)
    timezone = get_timezone(lat, lng)
    
    location = LocationInfo(name=place_name, region="", timezone=timezone, latitude=lat, longitude=lng)
    s = sun(location.observer, date=date_obj.date(), tzinfo=location.timezone)

    return s["sunrise"], s["sunset"]

def get_panchang_timings(date_obj: datetime, place_name: str) -> dict:
    """ Fixes Gulika Kalam being one segment ahead. """
    sunrise, sunset = get_sun_times(date_obj, place_name)

    day_duration = (sunset - sunrise) / 8

    time_segment_map = {
        "Monday":  [2, 7, 5],  # [Rahu, Gulika, Yamaganda]
        "Tuesday": [7, 6, 6],
        "Wednesday": [5, 5, 4],
        "Thursday": [6, 4, 3],
        "Friday": [4, 3, 2],
        "Saturday": [3, 2, 7],
        "Sunday": [8, 1, 8],
    }

    weekday = date_obj.strftime("%A")
    rahu_segment, gulika_segment, yamaganda_segment = time_segment_map[weekday]

    # Compute each period
    rahu_start = sunrise + (rahu_segment - 1) * day_duration
    rahu_end = rahu_start + day_duration

    # 🛠 FIX: Shift Gulika Kalam one segment back
    gulika_start = sunrise + (gulika_segment - 2) * day_duration  # -1 correction
    gulika_end = gulika_start + day_duration

    yamaganda_start = sunrise + (yamaganda_segment - 3) * day_duration
    yamaganda_end = yamaganda_start + day_duration

    return {
        "Rahu Kalam": f"{rahu_start.strftime('%I:%M %p')} to {rahu_end.strftime('%I:%M %p')}",
        "Gulika Kalam": f"{gulika_start.strftime('%I:%M %p')} to {gulika_end.strftime('%I:%M %p')}",  # ✅ FIXED!
        "Yamaganda": f"{yamaganda_start.strftime('%I:%M %p')} to {yamaganda_end.strftime('%I:%M %p')}"
    }










GOOGLE_MAPS_API_KEY="AIzaSyARW0InTpmvVUavE1Ur6zhJgIMuYvdZv2U"
'''