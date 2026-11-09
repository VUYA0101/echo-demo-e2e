# Synthetic demonstration only, NOT Echo source code.
def get_customer_by_id(customer_id, rows, tenant_id):
    if tenant_id is None:
        return None
    return next((row for row in rows
                 if row['id'] == customer_id and row.get('tenant') == tenant_id), None)
