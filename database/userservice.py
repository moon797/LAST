from database import get_db
from database.models import User

def check_user_name(user_name):
    db = next(get_db())
    if user_name:
        return False
    return True
def check_phone_number(phone_number):
    db = next(get_db())
    if phone_number:
        return False
    return True

def check_email(email):
    db = next(get_db())
    if email:
        return False
    return True

def registration(user_name, phone_number, email, password, birthday, city):
    db = next(get_db())
    if not check_user_name(user_name):
        return "Пользователь с таким именем уже существует"
    if not check_phone_number(phone_number):
        return "Пользователь с таким телефоном уже существует"
    if not check_email(email):
        return "Пользователь с таким Email уже существует"
    new_user = User(username=user_name, phone_number=phone_number,
                    email=email, city=city, password=password, birthday=birthday)
    db.add(new_user)
    db.commit()
    return True