# from os import remove
#
# student = []
#
# while True:
#     print('\n--- Student Score Tracker ---')
#     print('1 : To add a student')
#     print('2 : To view all student')
#     print('3 : Remove a student')
#     print('4 : Sort by score')
#     print('5 : To Reverse the list')
#     print('6 : Check if a student exist')
#     print('7 : Exist')
#
#     choice = int(input('Choose an option '))
#
#     if choice == 1:
#         name = input('Enter a student name ')
#         score = int(input('Enter the student score '))
#         student.append([name, score])
#         print('Student Added!')
#         print(student)
#
#     elif choice == 2:
#         for s in student:
#             print(f'{s[0]} - {s[1]}')
#
#
#     elif choice == 3:
#         remove_name = input('Enter name you want to remove ')
#         for s in student:
#             if s[0] == remove_name:
#                 student.remove(s)
#                 print(f'Student {remove_name} removed successfully')
#                 break
#             else:
#                 print('Student not found')
#
#     elif choice == 4:
#         student.sort(key=lambda  x: x[1])
#         print(f'List sorted by score \n {student}')
#         print(student)
#
#     elif choice == 5:
#         student.reverse()
#         print('List reversed')
#         print(student)
#
#     elif choice ==6:
#         name_exist = input('Enter name to check wether it exists')
#         found = False
#         for s in student:
#             if s[0] == name_exist:
#                 print(f'{name_exist} is in the list')
#                 found = True
#                 print(s)
#                 break
#         if not found:
#             print('Name does not exist')
#
#     elif choice == 7:
#         print('Exiting program')
#         break
#
#     else:
#         print('Invalid option. \nTry again')