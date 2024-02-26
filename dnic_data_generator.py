from model.shifts import create_fake_shift
from model.users import create_fake_user
from model.payments import create_fake_payment
from model.appointments import create_fake_appointment

from datetime import timedelta
from random import random

def generate_data(starting_dnic_id, start_date, number_days, offices_x_shift_types):
    data = {
        'users': [],
        'shifts': [],
        'payments': [],
        'appointments': []
    }
    dnic_id = starting_dnic_id
    for offset_days in range(number_days):
        date = start_date + timedelta(days=offset_days)
        for shift_type, offices in offices_x_shift_types.items():
            for office_id, office in offices.items():
                for turn in range(12):
                    offset_mins = turn * 30
                    for i in range(office['number_of_booths']):
                        timestamp = date + timedelta(minutes=offset_mins)
                        isAvailable = random() < office['available_ratio']
                        isUrgent = random() < office['urgent_ratio']
                        
                        shift = create_fake_shift(shift_type, dnic_id, timestamp, office_id, isAvailable, isUrgent)
                        data['shifts'].append(shift)
                        
                        if not isAvailable:
                            shift_id = shift['id']
                            user = create_fake_user(shift_type)
                            data['users'].append(user)
                            username = user['username']
                            payment = create_fake_payment(username, shift_type, timestamp, isUrgent)
                            data['payments'].append(payment)
                            payment_id = payment['id']
                            appointment = create_fake_appointment(username, shift_id, payment_id)
                            data['appointments'].append(appointment)
                        
                        dnic_id += 1
    return data
                    
                
            
        