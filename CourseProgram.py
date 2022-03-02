'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''

import CourseClass as c

def main():

   name = 'MIS 4322 - Advanced Python'
   crn = '250309'
   seats = 4
   status = 'open'
   students = ['John','James','Jill','Jack','Joanne']

   advpy = c.Course(name, crn, seats, status)

   for student in students:
      registration = c.Register(student, crn)
      if advpy.get_status() == 'open':
         advpy.update_seat_count()
         print('\nStudent Name:', registration.get_name())
         print('Course Name:', advpy.get_name())
         print('CRN:', advpy.get_crn())
         print('Seats Left:', advpy.get_seats(), '\n')
      else:
         print('Sorry ', registration.get_name(), ', registration is closed for ', advpy.get_name(), '\n', sep = '')

main()
