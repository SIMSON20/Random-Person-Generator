import unittest
import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Random Person Generator'))
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from random_person_generator import *

class Test_Random_Person_Generator(unittest.TestCase):
    def test_male_first_name(self):
        self.p = RandomPerson()
        self.assertIn(self.p.male_first_name(), male_first_names.name.values.tolist())

    def test_female_first_name(self):
        self.p = RandomPerson()
        self.assertIn(self.p.female_first_name(), female_first_names.name.values.tolist())

    def test_surname(self):
        self.p = RandomPerson()
        self.assertIn(self.p.surname(), surnames.name.values.tolist())

    def test_generate_random_name(self):
        self.p = RandomPerson()
        name = self.p.generate_random_name()
        first, last = name.split()
        self.assertIn(first, female_first_names.name.values.tolist()+male_first_names.name.values.tolist())
        self.assertIn(last, surnames.name.values.tolist())

    def test_random_age(self):
        self.p = RandomPerson()
        age = self.p.random_age()
        self.assertGreaterEqual(age, 1)
        self.assertLessEqual(age, 100)

    def test_random_email_service(self):
        self.p = RandomPerson()
        self.assertRegex(self.p.random_email_service(),
         r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[aol|gmail|outlook|yahoo|icloud|yandex]+(\.[A-Z|a-z]{2,})+')

    def test_random_phone_number(self):
        self.p = RandomPerson()
        self.assertRegex(self.p.random_phone_number(),
         r'\d\d\d-\d\d\d-\d\d\d\d')
        

    def test_create_occupation(self):
        self.p = RandomPerson().create_person()
        age = self.p["age"]
        occupation = self.p["job"]
        if age < 4:
            self.assertEqual(occupation, "NA")
        elif age < 18:
            self.assertEqual(occupation, "Student")
        else:
            self.assertIn(occupation, ["cook", "actor", "programmer", "doctor", "dentist", "uber driver", "photographer", "astronaut"])

    def test_create_person(self):
        self.p = RandomPerson()
        person = self.p.create_person()
        self.assertEqual(len(person), 7)
        self.assertEqual(list(person.keys()), ['first_name', 'last_name', 'email', 'sex', 'age', 'job', 'phone'])
        


if __name__ == '__main__':
    unittest.main()