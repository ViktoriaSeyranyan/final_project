import requests
import random
from faker import Faker

fake = Faker('ru_RU')  
API_URL = "http://127.0.0.1:8000/students/"

def create_student():
    return {
        "fio": fake.name(),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=25).strftime("%Y-%m-%d"),
        "city": fake.city(),
        "enrollment_year": random.randint(2018, 2023)
    }

def add_students(count):
    for _ in range(count):
        student = create_student()
        response = requests.post(API_URL, json=student)
        if response.status_code == 200:
            print(f"Добавлен студент: {student['fio']}")
        else:
            print(f"Ошибка при добавлении {student['fio']}: {response.text}")

if __name__ == "__main__":
    num_students = int(input("Сколько студентов добавить? "))
    add_students(num_students)
