# from ..calculations.panchang import calculate_panchang

# def get_panchang_for_date(place: str, date: str):
#     """
#     Service function to get Panchang based on place and date.
#     """
#     return calculate_panchang(place, date)



from ..calculations.panchang import calculate_panchang

def get_panchang_for_date(place: str, date: str):
    """
    Service function to get Panchang based on place and date.
    """
    return calculate_panchang(place, date)
