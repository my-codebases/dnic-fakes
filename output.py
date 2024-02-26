import json

def generate_json_data(data):
    with open('./json_files/users.json', 'w') as file:
        json.dump(data['users'], file, ensure_ascii=False, indent=4)
        
    with open('./json_files/shifts.json', 'w') as file:
        json.dump(data['shifts'], file, ensure_ascii=False, indent=4)
        
    with open('./json_files/payments.json', 'w') as file:
        json.dump(data['payments'], file, ensure_ascii=False, indent=4)
        
    with open('./json_files/appointments.json', 'w') as file:
        json.dump(data['appointments'], file, ensure_ascii=False, indent=4)
        
def generate_sql_scripts(data):
    generate_sql_scripts_for(data['users'], 'user', ['username', 'email', 'first_name', 'last_name', 'phone', 'created_date', 'last_updated_date', 'status', 'password', 'material_number', 'id_card_expiration_date', 'passport_expiration_date'])
    generate_sql_scripts_for(data['shifts'], 'shift', ['id', 'dnic_id', 'type', 'datetime', 'is_available', 'urgent', 'office_id'])
    generate_sql_scripts_for(data['payments'], 'payment', ['id', 'username', 'status', 'amount', 'creation_date', 'payment_date', 'expiration_date'])
    generate_sql_scripts_for(data['appointments'], 'appointment', ['id', 'username', 'shift_id', 'payment_id', 'status'])
    
def generate_sql_scripts_for(records, table_name, table_columns):
    values_list = []
    for record in records:
        values = [f"'{val}'" if isinstance(val, str) else str(val).lower() for val in record.values()]
        values_list.append(f"({', '.join(values)})")
    joined_values = ',\n\t'.join(values_list)
    stmt = f"""INSERT INTO `{table_name}` (`{'`, `'.join(table_columns)}`)
VALUES {joined_values};"""
    with open(f"./sql_scripts/sql_{table_name}.txt", 'w') as file:
        file.write(stmt)
    