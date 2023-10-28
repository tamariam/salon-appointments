from datetime import datetime
import json
import os
 
def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

FILE_PATH = 'appointments.json'


def time_validator(time_option):
    valid_options= [1,2,3,4,5,6]
    return time_option in valid_options  
def booked_times(appointments,correct_format_date) :
    booked_times=[]
    for appointment in appointments:
        if appointment['date']== correct_format_date:
            booked_times.append(appointment['time'])
    return booked_times       


def name_validator(name) :
    name_word=name.split()
    for word in name_word:
        if not all(char.isalpha() or char == '-' for char in word):
            return False

    return True   
  
def user_choice_validator(user_choice):
    user_options=[1,2,3,4,0]
    return user_choice in user_options  

def show_appointment(appointments) :
    print('\n appointments')
    print('Name\t\tDate\t\tTime')
    print('-' *50)
    for appointment in appointments :
        print(f'{appointment["name"]}\t\t{appointment["date"]}\t\t{appointment["time"]}')
def just_booked(new_appointment):
    if isinstance(new_appointment, dict):
        print(f'Name: {new_appointment.get("name", "N/A")}')
        print(f'Date: {new_appointment.get("date", "N/A")}')
        print(f'Time: {new_appointment.get("time", "N/A")}')
    else:
        print(new_appointment)

def todays_appointments(appointments):
    screen_clear()
    today = datetime.now().date()
    correct_format_today = today.strftime('%d/%m/%Y')
  
    
    todays_bookings= []
    for appointment in appointments:
        if  appointment["date"] == correct_format_today:
            todays_bookings.append(appointment)
    if todays_bookings:
        print('todays appointments: ')
        show_appointment(todays_bookings)
        print(todays_bookings)
    else:
        print('no appointments booked for today')
        

    back_to_menu()    

def handle_to_user_click(appointments):
    while True:   
        try:
            user_click = int(input('click 3 to go back to main menu  or click 4 to stay on this page'))  
                                    
            if user_click == 3:
                screen_clear() 
                return True
            elif user_click == 4:
                screen_clear() 
                return False
            else:
                print(' ivalid option please chosse 3 or 4')
        except ValueError:
            print('please use only numbers')
    return appointments
def search_appointment(appointments):
    screen_clear()
    while True :
        try:
            search_method=int(input('please mark one option below:\n 1)search appointment by date\n 2) search appointment by name\n'))
            screen_clear()
        except ValueError:
            print('please use only numbers ')
            continue
        if search_method == 1:
            date =input('Please enter date(dd/mm/yyyy): ')  
            date_obj=date_validation(date)
            if date_obj:
                screen_clear()
                appointments_date=[]
                for appointment in appointments:
                    if appointment['date']==date_obj.strftime('%d/%m/%Y'):
                        appointments_date.append(appointment)
                if appointments_date:
                    print('appointments for specified date:')  
                    show_appointment(appointments_date)
                    if handle_to_user_click(appointments):
                        return appointments
                       
                else:
                    print('no appointments for specified date')
                    if handle_to_user_click(appointments):
                        return appointments
                    
                    
                   

        elif search_method == 2:
            name_input=input('please enter name \n')
            name=name_validator(name_input)
            if name:
                appointments_name = []
                for appointment in appointments:
                    if appointment['name']== name_input:
                        appointments_name.append(appointment)
                if appointments_name:
                    print('appointments for specified name : \n ')
                    show_appointment(appointments_name)
                    if handle_to_user_click(appointments):
                        return appointments
                       
                else:
                    print('no appointments for specified name')
                    if handle_to_user_click(appointments):
                        return appointments
                   


    return appointments


def cancell_appointment(appointments):
    screen_clear()
    while True:
        name=input('please enter name  \n')
        if not name_validator(name):
            print('please enter valid name')
        else:
            
       
            date=input('enter date you want to cancell \n')
            date_obj=date_validation(date)

            cancelled_appointments=[]
            for appointment in appointments:
                if appointment['date']==date and appointment['name'] == name:
                    cancelled_appointments.append(appointment)
                    show_appointment(cancelled_appointments)
            if cancelled_appointments:
                for appointment in appointments:
                    appointments.remove(appointment)
                with open(FILE_PATH, 'w') as file:
                    json.dump(appointments, file)
                print('your appointment has been cancelled')
                back_to_menu()
                return appointments
                
            else:
                print('no appointment found')
                back_to_menu()
                return appointments
                


def back_to_menu():
     while True:
            user_click=int(input('click 1 to go back to main menu '))
            try:
                if user_click==1:
                   screen_clear()
                   break
            except ValueError:
                print('please enter 1 to  go back to main menu')
def date_validation(date) :
    if not date.count('/') == 2:
            print('invalid date format, please use dd/mm/yyyy format only')
    else:
         # Split the input date string
        day,month,year=map(int,date.split('/'))
        try:
            date_obj = datetime(year,month,day).date()
            return date_obj
        except ValueError:
            print('invalid date input')
            



def book_appointment(appointments): 
    screen_clear()
    while True:       
        date =input('Please let us know when you want an appointment (dd/mm/yyyy): ')  
        date_obj=date_validation(date)
        if date_obj:
            break

    day, month, year = date_obj.day, date_obj.month, date_obj.year
    current_year = datetime.now().year
    today = datetime.now().date()
    if 1 <= day <= 31 and 1 <= month <= 12  and year >= current_year:
        if month == 2 :
            max_day = 29
        elif month in [4,6,9,11] :
            max_day = 30
        else:
            max_day = 31
        if 1 <= day <= max_day :        
            appointment_date = datetime(year, month, day).date()
            correct_format_date = appointment_date.strftime('%d/%m/%Y')
            print(correct_format_date)
            if appointment_date < today:
                screen_clear()
                print('date is in past please enter  future or todays date ')
                back_to_menu()
            elif appointment_date.weekday() in [5,6]:
                screen_clear()
                print('Please choose another option because we are closed on weekends')
                back_to_menu()
                
                
            else:    
                name=input('please enter your name ').strip() 
                if name_validator(name):
                        try:
                            time_options=int(input('plese choose one option below\n1) 09:00\n2) 10:00\n3) 11:00\n4) 12:00\n5) 14:00\n6) 15:00\n'))
                            if time_validator(time_options):
                                
                                time_availibilities = ['09:00', '10:00', '11:00' ,'12:00', '14:00', '15:00']
                                time=time_availibilities[time_options-1]
                                booked_time = booked_times(appointments,correct_format_date)
                                screen_clear()
                                if time in booked_time:
                                    print(f'{time} on {correct_format_date}is already boooked,please try another time')
                                    back_to_menu()
                                else:
                                        new_appointment={'name': name, 'date' :correct_format_date, 'time' : time}
                                        print(f'your appointment has been booked for {correct_format_date} at {time} {name}, see you soon ')
                                        appointments.append(new_appointment)
                                
                                        with open('appointments.json', 'w') as file:
                                            json.dump(appointments, file)    
                                        just_booked(new_appointment)
                                       
                                        back_to_menu()
                                            
                            else:
                                print('invalid time option please choose  a valid one')
                                
                        except ValueError:
                            print('please enter only number for time option')     
                                  
                else:
                    print('invalid name format, name should only include letters')     
                       
            
        else:
            
            print('Invalid date format. Please use valid dd/mm/yyyy format.')   
                
    else:
        
        print('Invalid date format. Please use valid dd/mm/yyyy format.')
        
                    
    return appointments 
    screen_clear()
                       
def main_menu():
    screen_clear()
    try:
        with open(FILE_PATH, 'r') as file:
            appointments = json.load(file)
    except ( FileNotFoundError, json.JSONDecodeError):
        appointments = []     
    while True:
        print('Welcome to the hair-beauty booking app')
        try:
            user_choice = int(input('please select one option below \n1) book an appointment \n2) Todays appointments\n3) search appointment\n4) cancell appointment\n0) Quit \n '))
            if user_choice == 1:
                appointments=book_appointment(appointments)
            elif user_choice == 2:
                todays_appointments(appointments)
            elif user_choice == 3:
                appointments=search_appointment(appointments)
            elif user_choice == 4:
                appointments=cancell_appointment(appointments)
            elif user_choice == 0:
                screen_clear()
                break
            else:
                print('Invalid input. Please select a valid option.') 
        except ValueError:
            print('please use only numbers from 0 to 4')
                
                  
           
                                    
if  __name__=='__main__' :
      main_menu()    