import random
from models import User
from storage import read_storage,write_storage

class UserManagement(User):
    MAX_BOOKS_ISSUED = 5

    def __init__(self):
        super().__init__(user_id=None, name=None, pin=None)
        self.user_id_generator = self.generate_user_id()

    def generate_user_id(self):
        try:
            data = read_storage("utils.json")
            counter = data.get('user_counter', 0)

            while True:
                counter += 1
                data['user_counter'] = counter
                write_storage(data, 'utils.json')
                yield f"U_{counter}"
        except Exception as e:
            print(f"Error in generating user id: {str(e)}")

    def add_user(self, name):
        user_id = next(self.user_id_generator)
        pin = ''.join(map(lambda x: str(random.randint(0, 9)), range(4)))
        
        new_user = User(user_id, name, pin).to_json()

        try:
            data = read_storage("users.json")
            data[user_id] = new_user
            write_storage(data,"users.json")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    def authenticate_user(self, func):
        def wrapper(*args, **kwargs):
            user_id = kwargs.get('user_id')
            pincode = kwargs.get('pincode')
            if self.authenticate(user_id, pincode):
                return func(*args, **kwargs)
            else:
                print("Authentication failed. Access denied.")
        return wrapper
    
    def authenticate(self,user_id,pincode):
        try:
            data = read_storage('users.json')  # Read user data
            if user_id in data and data[user_id]['pin'] == pincode:
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False
        
    def is_valid(user_id):
        try:
            data = read_storage("users.json")
            if user_id in data:
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occured:{str(e)}")
            return False