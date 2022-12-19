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
    def male_first_name(self):
        return random.choices(male_first_names.name.values, k=1)[0]
    
    def female_first_name(self):
        return random.choices(female_first_names.name.values, k=1)[0]

    def surname(self):
        return random.choices(surnames.name.values, k=1)[0]
    
    def generate_random_name(self):
        first = random.choice([self.female_first_name(), self.male_first_name()])
        return " ".join([first, self.surname()])
    
    def random_age(self, min=1, max=100):
        try:
            if min > 0 and max <101:
                return random.randint(min, max)
            else:
                raise ValueError
        except ValueError:
            raise ValueError("Enter in min greater than 0 and a max less than one")
    
    def random_email_service(self):
        first = random.choice([self.female_first_name(), self.male_first_name()])
        return "".join([first, self.surname(),
                        "@", random.choice(["aol", "gmail", "outlook", "yahoo", "icloud", "yandex"]), 
                        ".", random.choice(["co", "com", "ru", "fr"])])

    def random_phone_number(self):
        return "-".join([str(random.randint(100, 1000)), str(random.randint(100,1000)), str(random.randint(1000, 10000))])
    
    def create_occupation(self):
        occupation = random.choice(["cook", "actor", "programmer", "doctor", "dentist", "uber driver", "photographer", "astronaut"])
        return occupation
    
    def create_person(self):
        names = [self.female_first_name(), self.male_first_name()]
        first = random.choice(names)
        last = self.surname()
        email = self.random_email_service()
        sex = "female" if first==names[0] else "male"
        age = self.random_age()
        if age < 4:
            job = "NA"
        elif age < 18:
            job = "student"
        else:
            job = self.create_occupation()
        phone = self.random_phone_number()

        return {'first_name': first, 
                'last_name': last, 
                'email': email, 
                'sex': sex, 
                'age': age, 
                'job': job, 
                'phone': phone}