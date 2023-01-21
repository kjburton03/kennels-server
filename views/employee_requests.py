EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Timbre Bur"
    },
    {
        "id": 3,
        "name": "Lacey Wade"
    }
]

def get_all_employees():
    """_summary_

    Returns:
        _type_: _description_
    """
    return EMPLOYEES

def get_single_employee(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    """_summary_

    Args:
        employee (_type_): _description_

    Returns:
        _type_: _description_
    """
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    """_summary_

    Args:
        id (_type_): _description_
    """
    # Initial -1 value for animal index, in case one isn't found
    employee_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Store the current index.
            employee_index = index

    # If the animal was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """_summary_

    Args:
        id (_type_): _description_
        new_animal (_type_): _description_
    """
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = new_employee
            break
