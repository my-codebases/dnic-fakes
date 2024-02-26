from faker import Faker
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import hashlib
import random
import math


id_card_expiration_start = datetime(2023, 9, 10)
id_card_expiration_end = datetime(2024, 5, 30)
passport_expiration_start = datetime(2020, 1, 15)
passport_expiration_end = datetime(2024, 10, 31)

id_number_start = 1200000
id_number_end = 5400000

fake = Faker('es_AR')

def create_fake_user(shift_type):
    age_value = random.random()
    age_deviation = (random.random() - 0.5) * 0.1

    id_number = add_check_digit(get_random_id(id_number_start, id_number_end, age_value + age_deviation))
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = first_name.lower()[:1] + last_name.lower() + '@gmail.com'
    phone = generate_fake_phone_number()
    created_date = fake.date_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
    password = hashlib.sha256('Pass1234'.encode('utf-8')).hexdigest()
    material_number = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    id_card_expiration_date = get_random_date(id_card_expiration_start, id_card_expiration_end, random.random())
    passport_expiration_date = get_random_date(passport_expiration_start, passport_expiration_end, random.random())
    if shift_type == 'PASSPORT':
        id_card_expiration_date += relativedelta(years = random.randint(2, 9))

    user = {
        'username': str(id_number),
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'created_date': created_date,
        'last_updated_date': created_date,
        'status': 'ACTIVE',
        'password': password,
        'material_number': material_number,
        'id_card_expiration_date': id_card_expiration_date.strftime('%Y-%m-%d %H:%M:%S'),
        'passport_expiration_date': '' if shift_type == 'PASSPORT' else passport_expiration_date.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return user

def generate_fake_phone_number():
    country_code = '+598'
    company_code = '9' + str(random.randint(1,9))
    digits = random.choices('0123456789', k=6)
    return f"{country_code} {company_code} {''.join(digits[:3])} {''.join(digits[3:])}"


def get_random_date(start, end, value):
    offset = math.floor(value * (end - start).total_seconds())
    return start + timedelta(seconds=offset)

def get_random_id(start, end, value):
    offset = math.floor(value * (end - start))
    return start + offset

def add_check_digit(document_number):
    factors = [2, 9, 8, 7, 6, 3, 4]
    check_digit = 0
    for i in range(7):
        check_digit += (document_number // 10 ** (6-i)) % 10
    check_digit = 10 - check_digit % 10
    return document_number * 10 + check_digit