import random
import pandas as pd



def read_file(file):
    with open(f"data/{file}") as f:
        data = f.readlines()
    return pd.DataFrame([x.split() for x in data],
             columns = ["name", "freq", "cum_freq", "rank"]
            )

male_first_names = read_file("dist.male.first.txt")

female_first_names = read_file("dist.female.first.txt")

surnames = read_file("dist.all.last.txt")

class RandomPerson():
    def male_first_name():
        return None
    
    def female_first_name():
        return None
    
    def surname():
        return None
    
    def generate_random_name():
        return None
    
    def random_age(min=1, max=100):
        return None
    
    def random_email_service():
        return None
    
    def random_phone_number():
        return None
    
    def create_occupation():
        return None
    
    def create_person():
        return None