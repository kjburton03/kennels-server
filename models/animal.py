class Animal():
    """_summary_
    """

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, breed, status, location_id, customer_id):
        """_summary_

        Args:
            id (_type_): _description_
            name (_type_): _description_
            breed (_type_): _description_
            status (_type_): _description_
            location_id (_type_): _description_
            customer_id (_type_): _description_
        """
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id
