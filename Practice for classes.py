class dogs:
     def __init__(self,
                  name: str,
                  age: int,
                  breed: str):
         self.name = name
         self.age = age
         self.breed = breed


         if age <= 2:
             print(f'the age of the dog is {age} hence it will have a higher price')
         else:
             print('dog will pe cheaper')


     def get_name(self):
         return self.name

     def get_age(self):
         return self.age

     def get_breed(self):
         return self.breed

     # def price_of_dogs(get_age):


d1=dogs("Jackey", 1, 7)
print(d1.get_age())
print(d1.get_name())
print(d1.get_breed())