students_1 = int( input ("Введи количество учеников в 1-м классе: ") )
students_2 = int( input ("Введи количество учеников в 2-м классе: ") )
students_3 = int( input ("Введи количество учеников в 3-м классе: ") )

ostatok_1 = students_1 % 2
ostatok_2 = students_2 % 2
ostatok_3 = students_3 % 2

tables_1 = students_1 // 2 + ostatok_1
tables_2 = students_2 // 2 + ostatok_2
tables_3 = students_3 // 2 + ostatok_3

print('Количество парт в 1-м классе:' ,tables_1,
      '\nКоличество парт в 2-м классе:',tables_2,
      '\nКоличество парт в 3-м классе:',tables_3,
      '\nОбщее количество парт: ',tables_1 + tables_2 + tables_3,)