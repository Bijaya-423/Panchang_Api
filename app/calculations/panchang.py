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












# import requests
# from datetime import datetime, timedelta
# from .astronomy import get_sun_position
# from skyfield.api import load
# import math
# import ephem


# GOOGLE_MAPS_API_KEY = "AIzaSyARW0InTpmvVUavE1Ur6zhJgIMuYvdZv2U"

# planets = load('de421.bsp')
# earth, moon, sun = planets['earth'], planets['moon'], planets['sun']

# def get_lat_lon(place):
#     """Fetch latitude and longitude from Google Maps API"""
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={GOOGLE_MAPS_API_KEY}"
#     response = requests.get(url).json()
    
#     if response['status'] == 'OK':
#         location = response['results'][0]['geometry']['location']
#         return location['lat'], location['lng']
#     else:
#         raise ValueError("Invalid location or API error")
    

# def get_timezone(lat, lon, date):
#     """Fetch timezone from Google Time Zone API"""
#     timestamp = int(datetime.strptime(date, "%Y-%m-%d").timestamp())
#     url = f"https://maps.googleapis.com/maps/api/timezone/json?location={lat},{lon}&timestamp={timestamp}&key={GOOGLE_MAPS_API_KEY}"
#     response = requests.get(url).json()
    
#     if response['status'] == 'OK':
#         return response['timeZoneId'], response['rawOffset'], response['dstOffset']
#     else:
#         raise ValueError("Could not fetch timezone data")
    
    


# def get_sun_times(lat, lon, date):
#     """Calculate sunrise and sunset times for a given location and date."""
#     observer = ephem.Observer()
#     observer.date = date
#     observer.lat, observer.lon = str(lat), str(lon)
    
    
#     sunrise = ephem.localtime(observer.next_rising(ephem.Sun()))
#     sunset = ephem.localtime(observer.next_setting(ephem.Sun()))

#     return sunrise, sunset


# def get_moon_times(lat, lon, date):
#     """Calculate moonrise and moonset times for a given location and date."""
#     observer = ephem.Observer()
#     observer.date = date
#     observer.lat, observer.lon = str(lat), str(lon)
    
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
        
        
#         lat, lon = get_lat_lon(place)
#         timezone, raw_offset, dst_offset = get_timezone(lat, lon, date)
#         sunrise, sunset = get_sun_times(lat, lon, date)
#         moonrise, moonset = get_moon_times(lat, lon, date)

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
#             "TimeZone": timezone,
#             "Sunrise": sunrise.strftime("%I:%M %p"),
#             "Sunset": sunset.strftime("%I:%M %p"),
#             "Moonrise": moonrise.strftime("%I:%M %p"),
#             "Moonset": moonset.strftime("%I:%M %p"),
#             "date": date_obj.strftime('%d %B %Y'),
#             "place": place,
#             "latitude": lat,
#             "longitude": lon,
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
#             # "kaal_timings": kaal_timings,
#         }
#         return panchang_details
#     except Exception as e:
#         raise ValueError(f"Error in Panchang calculation: {str(e)}")





















# import requests
# from datetime import datetime, timedelta
# from .astronomy import get_sun_position
# from skyfield.api import load
# import math
# import ephem


# GOOGLE_MAPS_API_KEY = "AIzaSyARW0InTpmvVUavE1Ur6zhJgIMuYvdZv2U"

# planets = load('de421.bsp')
# earth, moon, sun = planets['earth'], planets['moon'], planets['sun']

# def get_lat_lon(place):
#     """Fetch latitude and longitude from Google Maps API"""
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={GOOGLE_MAPS_API_KEY}"
#     response = requests.get(url).json()
    
#     if response['status'] == 'OK':
#         location = response['results'][0]['geometry']['location']
#         return location['lat'], location['lng']
#     else:
#         raise ValueError("Invalid location or API error")
    

# def get_timezone(lat, lon, date):
#     """Fetch timezone from Google Time Zone API"""
#     timestamp = int(datetime.strptime(date, "%Y-%m-%d").timestamp())
#     url = f"https://maps.googleapis.com/maps/api/timezone/json?location={lat},{lon}&timestamp={timestamp}&key={GOOGLE_MAPS_API_KEY}"
#     response = requests.get(url).json()
    
#     if response['status'] == 'OK':
#         return response['timeZoneId'], response['rawOffset'], response['dstOffset']
#     else:
#         raise ValueError("Could not fetch timezone data")
    
    


# def get_sun_times(lat, lon, date):
#     """Calculate sunrise and sunset times for a given location and date."""
#     observer = ephem.Observer()
#     observer.date = date
#     observer.lat, observer.lon = str(lat), str(lon)
    
    
#     sunrise = ephem.localtime(observer.next_rising(ephem.Sun()))
#     sunset = ephem.localtime(observer.next_setting(ephem.Sun()))

#     return sunrise, sunset


# def get_moon_times(lat, lon, date):
#     """Calculate moonrise and moonset times for a given location and date."""
#     observer = ephem.Observer()
#     observer.date = date
#     observer.lat, observer.lon = str(lat), str(lon)
    
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
        
        
#         lat, lon = get_lat_lon(place)
#         timezone, raw_offset, dst_offset = get_timezone(lat, lon, date)
#         sunrise, sunset = get_sun_times(lat, lon, date)
#         moonrise, moonset = get_moon_times(lat, lon, date)

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
#             "TimeZone": timezone,
#             "Sunrise": sunrise.strftime("%I:%M %p"),
#             "Sunset": sunset.strftime("%I:%M %p"),
#             "Moonrise": moonrise.strftime("%I:%M %p"),
#             "Moonset": moonset.strftime("%I:%M %p"),
#             "date": date_obj.strftime('%d %B %Y'),
#             "place": place,
#             "latitude": lat,
#             "longitude": lon,
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
#             # "kaal_timings": kaal_timings,
#         }
#         return panchang_details
#     except Exception as e:
#         raise ValueError(f"Error in Panchang calculation: {str(e)}")













import requests
from datetime import datetime
from astral import LocationInfo
from astral.sun import sun
import pytz
from timezonefinder import TimezoneFinder
from skyfield.api import load
import math
import ephem

# Constants
GOOGLE_MAPS_API_KEY = "AIzaSyARW0InTpmvVUavE1Ur6zhJgIMuYvdZv2U"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%I:%M %p"

# Load planetary data
planets = load('de421.bsp')
earth, moon, sun_planet = planets['earth'], planets['moon'], planets['sun']

def get_lat_lon(place):
    """Get coordinates using Google Geocoding API with error handling"""
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={GOOGLE_MAPS_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'OK':
            loc = data['results'][0]['geometry']['location']
            return loc['lat'], loc['lng']
        raise ValueError(f"Geocoding API error: {data.get('error_message', 'Unknown error')}")
    except Exception as e:
        raise ValueError(f"Geocoding failed: {str(e)}")

def get_timezone(lat, lng):
    """Get timezone using coordinates"""
    tf = TimezoneFinder()
    return tf.timezone_at(lng=lng, lat=lat) or "UTC"

def get_sun_times(place, date):
    """Get accurate sunrise/sunset times using Astral"""
    lat, lng = get_lat_lon(place)
    tz = pytz.timezone(get_timezone(lat, lng))
    
    location = LocationInfo(
        name=place,
        region="IN",
        timezone=tz.zone,
        latitude=lat,
        longitude=lng
    )
    
    date_obj = datetime.strptime(date, DATE_FORMAT).date()
    s = sun(location.observer, date=date_obj, tzinfo=tz)
    return (
        s['sunrise'].strftime(TIME_FORMAT),
        s['sunset'].strftime(TIME_FORMAT),
        s['sunrise'].astimezone(tz),  # Convert to aware datetime
        s['sunset'].astimezone(tz)
    )

def get_moon_times(lat, lon, date):
    """Calculate accurate moonrise/moonset with proper date handling"""
    tz = pytz.timezone(get_timezone(lat, lon))
    observer = ephem.Observer()
    observer.lat = str(lat)
    observer.lon = str(lon)
    
    # Set to UTC midnight of target date
    utc_date = datetime.strptime(date, DATE_FORMAT).replace(tzinfo=pytz.utc)
    observer.date = utc_date
    
    try:
        moonrise = observer.next_rising(ephem.Moon())
        moonset = observer.next_setting(ephem.Moon())
        
        # Convert to local timezone
        moonrise_local = ephem.localtime(moonrise).astimezone(tz)
        moonset_local = ephem.localtime(moonset).astimezone(tz)
        
        # Format times with proper AM/PM handling
        return (
            moonrise_local.strftime(TIME_FORMAT),
            moonset_local.strftime(TIME_FORMAT)
        )
    except ephem.AlwaysUpError:
        return ("Always Up", "Always Down")
    except ephem.NeverUpError:
        return ("Never Rises", "Never Sets")

# Add this timezone conversion helper
def ensure_timezone(dt, tz):
    """Convert naive datetime to timezone-aware"""
    if dt.tzinfo is None:
        return tz.localize(dt)
    return dt.astimezone(tz)

def format_time(start_time, duration):
    """Helper function to format time range as string"""
    end_time = start_time + duration
    return f"{start_time.strftime(TIME_FORMAT)} to {end_time.strftime(TIME_FORMAT)}"

def get_kaal_timings(sunrise, sunset):
    """Calculate kaal periods with snake_case keys and string format"""
    if not isinstance(sunrise, datetime) or not isinstance(sunset, datetime):
        raise ValueError("Invalid datetime inputs")

    day_duration = sunset - sunrise
    part_duration = day_duration / 8

    weekday_map = {
        0: (2, 4, 7),   # Monday
        1: (7, 3, 6),   # Tuesday
        2: (5, 2, 8),   # Wednesday
        3: (6, 1, 4),   # Thursday
        4: (4, 7, 2),   # Friday
        5: (3, 6, 1),   # Saturday
        6: (8, 5, 7)    # Sunday
    }

    weekday_idx = sunrise.weekday()
    rahu_slot, yama_slot, gulika_slot = weekday_map[weekday_idx]

    return {
        "rahu_kaal": format_time(sunrise + (rahu_slot-1)*part_duration, part_duration),
        "yamaganda": format_time(sunrise + (yama_slot-1)*part_duration, part_duration),
        "gulika_kaal": format_time(sunrise + (gulika_slot-1)*part_duration, part_duration)
    }
def get_samvat_details(date_obj):
    """Calculate Samvat and Vikram eras with month adjustment"""
    greg_year = date_obj.year
    month = date_obj.month
    
    # Hindu calendar year starts in Chaitra (March-April)
    vikram_year = greg_year + 57 if month >= 4 else greg_year + 56
    shaka_year = greg_year - 78 if month >= 4 else greg_year - 79
    
    samvatsara_names = [
        "Prabhava", "Vibhava", "Shukla", "Pramoda", "Prajapati", "Angirasa",
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
    
    return {
        "shaka": f"{shaka_year} - {samvatsara_names[(shaka_year + 10) % 60]}",
        "vikram": f"{vikram_year} - {samvatsara_names[(vikram_year - 1) % 60]}"
    }

def calculate_panchang(place, date):
    """Main function to calculate complete Panchang"""
    try:
        # Get date object
        date_obj = datetime.strptime(date, DATE_FORMAT)
        
        # Get location data
        lat, lon = get_lat_lon(place)
        timezone = get_timezone(lat, lon)
        
        # Get sun times
        sunrise_str, sunset_str, sunrise_dt, sunset_dt = get_sun_times(place, date)
        
        # Get moon times
        moonrise_str, moonset_str = get_moon_times(lat, lon, date)
        
        # Calculate kaal timings
        kaal_timings = get_kaal_timings(sunrise_dt, sunset_dt)
        
        # Astronomical calculations
        ts = load.timescale()
        t = ts.utc(date_obj.year, date_obj.month, date_obj.day)
        
        sun_pos = earth.at(t).observe(sun_planet).apparent()
        moon_pos = earth.at(t).observe(moon).apparent()
        sun_lon = sun_pos.ecliptic_latlon()[1].degrees
        moon_lon = moon_pos.ecliptic_latlon()[1].degrees
        
        # Tithi calculation
        lunar_phase = (moon_lon - sun_lon) % 360
        tithi_num = math.floor(lunar_phase / 12) + 1

# Complete list of 30 tithis
        tithi_names = [
            "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", 
            "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami", 
            "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
            "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
            "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
            "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
        ]

        tithi = tithi_names[tithi_num - 1]  # Now properly initialized
        
        # Nakshatra calculation
        ayanamsa = 24 + (4/60) + (60/3600)
        moon_sidereal = (moon_lon - ayanamsa) % 360
        nakshatra_num = math.floor(moon_sidereal / (360 / 27))
        nakshatra_names = [
            "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", 
            "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha", 
            "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", 
            "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", 
            "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", 
            "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
        ]
        nakshatra = nakshatra_names[nakshatra_num]
        
        # Yoga calculation
        yoga_angle = ((sun_lon - ayanamsa) + (moon_lon - ayanamsa)) % 360
        yoga_num = math.floor(yoga_angle / (13 + 20/60)) % 27
        yoga_names = [
            "Vishkumbha", "Priti", "Ayushman", "Saubhagya", "Shobhana", 
            "Atiganda", "Sukarma", "Dhriti", "Shoola", "Ganda", 
            "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra", 
            "Siddhi", "Vyatipata", "Variyana", "Parigha", "Shiva", 
            "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma", "Indra", "Vaidhriti"
        ]
        yoga = yoga_names[yoga_num]
        
        # Paksha and Karana
        paksha = "Shukla" if tithi_num <= 15 else "Krishna"
        if tithi_num in [30, 14]:
            karana = ["Shakuni", "Chatushpada", "Naga", "Kimstughna"][(tithi_num - 14) % 4]
        else:
            karana = ["Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti"][((tithi_num - 1) * 2) % 7]
        
        # Dishashool
        dishashool_mapping = {
            0: "East",   # Monday
            1: "North",  # Tuesday
            2: "North",  # Wednesday
            3: "South",  # Thursday
            4: "West",   # Friday
            5: "East",   # Saturday
            6: "West"    # Sunday
        }
        
        return {
            "Date": date_obj.strftime('%d %B %Y'),
            "Place": place,
            "Timezone": timezone,
            "Sunrise": sunrise_str,
            "Sunset": sunset_str,
            "Moonrise": moonrise_str,
            "Moonset": moonset_str,
            "Tithi": tithi,
            "Nakshatra": nakshatra,
            "Yoga": yoga,
            "Karana": karana,
            "Paksha": paksha,
            "Day": date_obj.strftime('%A'),
            "Dishashool": dishashool_mapping[date_obj.weekday()],
            **get_samvat_details(date_obj),
            **kaal_timings
        }
        
    except Exception as e:
        return {"error": str(e)}








