class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def increase_age(self,a):
        self.age = self.age + a
        return self.age

class student(Person):
    def __init__(self,name,age,school):
        super().__init__(name,age)
        self.school = school
    
    def islegal(self):
        return self.age > 17

    def print_details(self):
        print("The name is ",self.name,", age is ",self.age," and the school is ", self.school)

if __name__ == "__main__":

    print("Enter the name of the person")
    name = input()
    print("Enter the age of the person")
    age = int(input())
    
    if (age < 17):
        print("Is the person a student ? [Y/N]")
        chr = input()
        if(chr == 'Y' or chr =='y'):
            print("Enter the school name")
            sname = input()
            st = student(name,age,sname)
            st.print_details()
        else:
            print("OK!!")
    else:
        p1 = Person(name,age)
        print("The name is ",p1.name," and the age is ",p1.age)



    