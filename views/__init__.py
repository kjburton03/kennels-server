# from http.server import BaseHTTPRequestHandler, HTTPServer
# from views import get_all_animals
from .animal_requests import get_all_animals, get_single_animal, get_animals_by_location_id
from .animal_requests import create_animal, delete_animal, update_animal

from .locations_requests import get_all_locations, get_single_location
from .locations_requests import create_location, delete_location, update_location

from .employee_requests import get_all_employees, get_single_employee, get_employees_by_location_id
from .employee_requests import create_employee, delete_employee, update_employee

from .customer_request import get_all_customers, get_single_customer, get_customers_by_email
from .customer_request import create_customer, delete_customer, update_customer
