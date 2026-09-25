from .users import create_user
from werkzeug.security import generate_password_hash

create_user(
    'gustavo@email.com', 
    generate_password_hash('1234'), 
    'Gustavo'
)
