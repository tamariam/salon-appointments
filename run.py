# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from datetime import datetime

print('Welcome to the hair-beauty booking app')
user_choice = int(input('please select one option below \n 1) book an appointment \n 2) view availibilitys for today\n 3)cacell appointment\n 4)search appointment\n '))
if user_choice == 1:
    while True:    
        date = input('Please let us know when you want an appointment (dd/mm/yyyy): ').lower()

        # Split the input date string
        date_obj = date.split('/')

        if len(date_obj) == 3:
            day, month, year = map(int, date_obj)
            current_year = datetime.now().year
            today = datetime.now().date()
            print(today)
            if 1 <= day <= 31 and 1 <= month <= 12 and year <=current_year :
                if month==2 :
                    max_day=29
                elif month in[4,6,9,11] :
                    max_day=30
                else:
                    max_day=31
                if 1<=day<=max_day:        
                    appointment_date = datetime(year, month, day).date()
                    print(appointment_date)
                    if appointment_date >= today:
                        if appointment_date.weekday() < 5:
                            print('Good job')
                            break
                        else:
                            print('Please choose another option because we are closed on weekends')
                    else:
                        print('date is in past please enter  future or todays date ')
                else:
                    print('Invalid date format. Please use valid dd/mm/yy format.')       
            else:
                print('Invalid date format. Please use valid dd/mm/yy format.')



    
