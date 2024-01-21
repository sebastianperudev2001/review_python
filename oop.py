class Employee:

    company = "Belcorp"
    technologies = ["Python", "C++"]

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    
    def speak(self, sound = "default"):
        print("{} says {}".format(self.name, sound))
    

    def __str__(self) -> str:
        return "Name: {} - Age: {}".format(self.name, self.age)

class Intern(Employee):

    company = "Yanbal"

    def __init__(self, name, age, university) -> None:
        super().__init__(name, age)
        self.university = university
        self.technologies.append("Java")

def main():
    emp1 = Employee("John", 25)
    emp2 = Employee("Mary", 30)
    print(emp1.description())
    emp2.speak("Hello")
    emp2.speak()

    print(emp1)

    print(emp1.technologies)
    sebastian = Intern("Sebastian", 22, "Unilima")
    print(emp1.technologies)




main()




