import sys
def exit():
    sys.exit()

name = "Ali Gel"
check = False
for x in range(3):
  your_name = (input("Please enter your name and surname: "))
  
  if your_name == name:
    print("Wellcome")
    check = True
    break
  else:
    print("Try again!")
if not check:
  print("Please try again later!!!")
  exit()
selected_courses =[]
def selection():
    err_message= "You failed in class"

    course = input("You can choose a minimum of 3 and a maximum of 5 courses, Please enter the name of the courses you want to choose  : ")

    global selected_courses 
    selected_courses = course.replace(","," ").split()

    
    if 3<=(len(selected_courses))<=5:
      return selected_courses
        
    elif 5<(len(selected_courses)):
      print("You can choose a minimum of 3 and a maximum of 5 courses,Please try again later!!!")
      return exit()
      
    
    elif len(selected_courses)<3 :
      print(err_message)
      return exit()
      
     
    
selection()
print (selected_courses)

lesson = (input("Choose the course you want to take the exam: "))
print (selected_courses)


while lesson not in selected_courses:
  lesson = (input("please select a course from the list "))
if lesson in selected_courses:
  print("you chose \"{}\"course to take the exam".format(lesson))

  
midtermp = int(input("enter midterm point: "))  
finalp = int(input("enter final point: "))
projectp =int(input("enter prjoect point: "))

exams= ["midterm", "final","project"]
points= [midtermp,finalp, projectp]

res={}
for key in exams:
  for value in points:
    res[key]= value
    points.remove(value)
    break
print(res)

mg = res["midterm"]
fg = res["final"] 
pg = res["project"]
grades = mg*0.30 +fg*0.50 + pg*0.20
your_grade = "Your grade is "
x=""
if grades> 90:
  x="AA"
  print(your_grade, x)
elif 70 <= grades <= 90:
  x="BB"
  print(your_grade, x)
elif 50 <= grades < 70:
  x="CC"
  print(your_grade, x)
elif 30 <= grades <50:
  x="DD"
  print(your_grade, x)
elif grades<30:
  x="FF"
  print(your_grade, x,", you failed this course")

    

    





  
  



  
   

    