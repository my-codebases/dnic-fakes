from datetime import datetime, date, time, timedelta
import random
import uuid

amounts = {
    'ID_CARD': {
        False: 402,
        True: 804
    },
    'PASSPORT': {
        False: 3266,
        True: 6356
    }
}
offset_days = {
    'ID_CARD': {
        False: (80, 30),
        True: (40, 5)
    },
    'PASSPORT': {
        False: (120, 30),
        True: (60, 10)
    },
}
        

def create_fake_payment(username, shift_type, timestamp, isUrgent):
    payment_offset = offset_days[shift_type][isUrgent]
    creation_start = timestamp - timedelta(days=payment_offset[0])
    creation_end = timestamp - timedelta(days=payment_offset[1])
    
    creation_date = random_date_between(creation_start, creation_end)
    expiration_date = creation_date + timedelta(days=3)
    payment_date = random_payment_date(creation_date)
    amount = amounts[shift_type][isUrgent]
    
    payment = {
        'id': str(uuid.uuid4()),
        'username': username,
        'status': True,
        'amount': amount,
        'creationDate': creation_date.strftime('%Y-%m-%d %H:%M:%S'),
        'paymentDate': payment_date.strftime('%Y-%m-%d %H:%M:%S'),
        'expirationDate': expiration_date.strftime('%Y-%m-%d %H:%M:%S'),
    }
    
    return payment


def random_date_between(start_date, end_date):
    timestamp_start = datetime.timestamp(start_date)
    timestamp_end = datetime.timestamp(end_date)
    random_timestamp = random.uniform(timestamp_start, timestamp_end)
    random_date = datetime.fromtimestamp(random_timestamp)
    return add_random_hour(random_date)

def random_payment_date(creation_date):
    timestamp = date(creation_date.year, creation_date.month, creation_date.day)
    payment_delay = random.choice([0, 0, 0, 1, 1, 2])
    if payment_delay == 0:
        return creation_date
    timestamp += timedelta(hours=24*payment_delay)
    return add_random_hour(timestamp)

def add_random_hour(date):
    return date + timedelta(hours=9, seconds=random.randint(0, 12*60*60))