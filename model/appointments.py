import uuid

def create_fake_appointment(username, shift_id, payment_id):
    appointment = {
        'id': str(uuid.uuid4()),
        'username': username,
        'shift_id': shift_id,
        'payment_id': payment_id,
        'status': 'CONFIRMED'
    }
    
    return appointment