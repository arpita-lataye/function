def greet(*names):
    for name in names:
        print("Welcome", name)
greet("Rinki", "Vishal", "Kartik", "Bijender")




def info(name, age='19'):
    print(name + " is " + age + " years old")

info("Sonu")
info("Sana", "17")
info("Umesh", "18")
info('raghav')





def studentDetails(name,currentMilestone,mentorName):
    print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


studentDetails("Nilam","loop",'yoongi')