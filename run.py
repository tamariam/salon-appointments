# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from datetime import datetime

def time_validator(time_option):
    valid_options=[1,2,3,4,5,6,]
    return time_option in valid_options    

def name_validator(name) :
    name_word=name.split()
    for word in name_word:
        if not word.isalpha():
            return False

    return True   
  
def show_appointment(appointments) :
    print('\n appointments')
    print('Name\t\tDate\t\tTime')
    print('-' *50)
    for appointment in appointments :
        print(f'{appointment["name"]}\t\t{appointment["date"]}\t\t{appointment["time"]}')

print('Welcome to the hair-beauty booking app')
user_choice = int(input('please select one option below \n1) book an appointment\n2) view availibilitys for today\n3) cacell appointment\n4) search appointment\n '))
appointments=[]
if user_choice == 1:
    
     date =input('Please let us know when you want an appointment (dd/mm/yyyy): ')  
          # Split the input date string
     date_obj = date.split('/')

while True: 
        if len(date_obj) == 3:
            day, month, year = map(int, date_obj)
            current_year = datetime.now().year
            today = datetime.now().date()
            print(today)
            if 1 <= day <= 31 and 1 <= month <= 12  and year >=current_year:
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
                            name=input('please enter your name ').strip() 
                            if name_validator(name):
                                time_options=int(input('plese choose one option below\n1) 09:00\n2) 10:00\n3) 11:00\n4) 12:00\n4) 14:00\n5) 15:00\n'))
                                if time_validator(time_options):
                                    time_availibilities=['09:00', '10:00', '11:00' ,'12:00', '14:00', '15:00']
                                    time=time_availibilities[time_options-1]
                                    print(f'your appointment has been booked for {appointment_date} at {time} {name}, see you soon ')
                                    appointments.append({'name': name, 'date': appointment_date, 'time': time})
                                    show_appointment(appointments)
                                    break
                                else:
                                    print('invalid time option please choose  a valid one')
                            else:
                                print('invalid name format, name should only include letters')        
                        else:
                            print('Please choose another option because we are closed on weekends')
                            break
                    else:
                        print('date is in past please enter  future or todays date ')
                        break
                else:
                    print('Invalid date format. Please use valid dd/mm/yyyy format.')       
            else:
                print('Invalid date format. Please use valid dd/mm/yyyy format.')