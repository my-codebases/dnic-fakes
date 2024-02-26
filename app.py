from dnic_data_generator import generate_data
from output import generate_json_data, generate_sql_scripts

from datetime import datetime

starting_dnic_id = 1
start_date = datetime(2024, 12, 3, 9, 0, 0)
number_days = 5
offices = {
    'ID_CARD': {
        'ee7e5318-35d8-4287-93cd-11b6b510dd2d': {
            'number_of_booths': 3,
            'available_ratio': 0.40,
            'urgent_ratio': 0.40
        },
        '990d8640-be51-40fd-b036-2bd6aece2322': {
            'number_of_booths': 2,
            'available_ratio': 0.50,
            'urgent_ratio': 0.25
        },
        'd55a046e-2579-47f0-b031-52a27b4a7a49': {
            'number_of_booths': 1,
            'available_ratio': 0.00,
            'urgent_ratio': 0.60
        }
    },
    'PASSPORT': {
        '31db63d2-7502-4cf2-87f8-5059548d8466': {
            'number_of_booths': 2,
            'available_ratio': 0.25,
            'urgent_ratio': 0.50
        },
        '990d8640-be51-40fd-b036-2bd6aece2322': {
            'number_of_booths': 1,
            'available_ratio': 0.80,
            'urgent_ratio': 0.00
        },
        'd55a046e-2579-47f0-b031-52a27b4a7a49': {
            'number_of_booths': 1,
            'available_ratio': 1.00,
            'urgent_ratio': 0.00
        }
    }
}

data = generate_data(starting_dnic_id, start_date, number_days, offices)
generate_json_data(data)
generate_sql_scripts(data)