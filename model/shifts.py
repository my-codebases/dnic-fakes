import datetime
import random
import uuid

def create_fake_shift(shift_type, dnic_id, datetime, office_id, isAvailable, isUrgent):
    shift = {
        'id': str(uuid.uuid4()),
        'dnicID': str(dnic_id),
        'type': shift_type,
        'datetime': datetime.strftime('%Y-%m-%d %H:%M:%S'),
        'isAvailable': isAvailable,
        'isUrgent': isUrgent,
        'office': office_id
    }
    return shift

def create_shifts_for_offices(starting_dnic_id, start_date, number_days, offices_x_shift_types):
    shifts = []
    dnic_id = starting_dnic_id
    for offset_days in range(number_days):
        date = start_date + datetime.timedelta(days=offset_days)
        for shift_type, offices in offices_x_shift_types.items():
            for office_id, office in offices.items():
                for turn in range(12):
                    offset_mins = turn * 30
                    for i in range(office['number_of_booths']):
                        dt = date + datetime.timedelta(minutes=offset_mins)
                        shift = create_fake_shift(shift_type, dnic_id, dt, office_id, office['available_ratio'], office['urgent_ratio'])
                        shifts.append(shift)
                        dnic_id += 1
    return shifts
                    
                
            
        