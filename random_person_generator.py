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
    def __init__(self, sex="female"):
        self.sex = sex
        self.age = self.random_age()

    def male_first_name(self):
        return random.choices(male_first_names.name.values, k=1)[0]
    
    def female_first_name(self):
        return random.choices(female_first_names.name.values, k=1)[0]

    def surname(self):
        return random.choices(surnames.name.values, k=1)[0]
    
    def generate_random_name(self):
        return " ".join([self.female_first_name(), self.surname()]) if self.sex=="female" else " ".join([self.male_first_name(), self.surname()])
    
    def random_age(self, min=1, max=100):
        return random.randint(min, max)
    
    def random_email_service(self):
        return "".join([self.female_first_name(), self.surname(),
         "@", random.choice(["aol", "gmail", "outlook", "yahoo", "icloud", "yandex"]), ".", random.choice(["co", "com", "ru", "fr"])]) if self.sex=="female" else "".join([self.female_first_name(), self.surname(),
         "@", random.choice(["aol", "gmail", "outlook", "yahoo", "icloud", "yandex"]), ".", random.choice(["co", "com", "ru", "fr"])])
    
    def random_phone_number(self):
        return "-".join([str(random.randint(100, 1000)), str(random.randint(100,1000)), str(random.randint(1000, 10000))])
    
    def create_occupation(self):
        if  self.age < 4:
            occupation = "NA"
        elif self.age < 18:
            occupation = "student"
        else:
            occupation = random.choice(["cook", "actor", "programmer", "doctor", "dentist", "uber driver", "photographer", "astronaut"])
        return occupation
    
    def create_person(self):
        return {'first_name': self.female_first_name() if self.sex=="female" else self.male_first_name(), 
                'last_name': self.surname(), 
                'email': self.random_email_service(), 
                'sex': self.sex, 
                'age': self.age, 
                'job': self.create_occupation(), 
                'phone': self.random_phone_number()}