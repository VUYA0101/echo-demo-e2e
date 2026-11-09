# Synthetic demonstration only, NOT Echo source code.
def get_customer_by_id(customer_id, rows):
    return next((row for row in rows if row['id'] == customer_id), None)
