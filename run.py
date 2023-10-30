'''import modules to set up initial enviroment for project '''
# import datetime class from datetime module to work with dates
from datetime import datetime
# import json to read and write data
import json
# import os to interact with operating system
import os
# define file path for json file
FILE_PATH = 'appointments.json'
'''define function which will clear terminal
screen screen for improving console output clarity.'''


def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


'''this function  checks if user pass correct time'''


def time_validator(time_option):
    screen_clear()
    valid_options = [1, 2, 3, 4, 5, 6]
    return time_option in valid_options


'''this  function checks if the name is correctly formatted'''


def name_validator(name):
    screen_clear()
    while True:
        name_word = name.split()
        valid_name = True
        for word in name_word:
            if not all(char.isalpha() or char == '-' for char in word):
                valid_name = False
                break
        if valid_name:
            return True
        else:
            print('invalid name format, name should only include letters')
            name = input('Please enter your name: ').strip()


'''this function checks if user choice is a valid option'''


def user_choice_validator(user_choice):
    user_options = [1, 2, 3, 4, 0]
    return user_choice in user_options


'''this functions validates and parse a date in dd/mm/yyyy format'''


def date_validation(date):
    while True:
        if not date.count('/') == 2:
            screen_clear()
            print('invalid date format, please use dd/mm/yyyy format only \n')
        else:
            # Split the input date string
            day, month, year = map(int, date.split('/'))
            try:
                date_obj = datetime(year, month, day).date()
                return date_obj
            except ValueError:
                screen_clear()
                print('invalid date input')
        date = input('Please enter the date (dd/mm/yyyy): \n ')


'''This function searches through
a list of appointments to find all the booked times
    for a specified date in the correct date format. '''


def booked_times(appointments, correct_format_date):
    booked_times = []
    for appointment in appointments:
        if appointment['date'] == correct_format_date:
            booked_times.append(appointment['time'])
    return booked_times


'''this function prints appointment details '''


def show_appointment(appointments):
    print('\n appointments')
    print('Name\t\tDate\t\tTime')
    print('-' * 50)
    for appointment in appointments:
        print(
            f'{appointment["name"]}\t\t'
            f'{appointment["date"]}\t\t'
            f'{appointment["time"]}'
        )


'''this function  displays latest appointment
information,it checks if new appointment is dictionery or not,
if it is dictionery takes keys and its values
from there if not just prints new_appointment'''


def just_booked(new_appointment):
    if isinstance(new_appointment, dict):
        print(f'Name: {new_appointment.get("name", "N/A")}')
        print(f'Date: {new_appointment.get("date", "N/A")}')
        print(f'Time: {new_appointment.get("time", "N/A")}')
    else:
        print(new_appointment)


'''this function checks if there is or not
appointments booked for today, if there is it displays appointment details,
if not simply says that there is no appointments booked for today '''


def todays_appointments(appointments):
    screen_clear()
    today = datetime.now().date()
    correct_format_today = today.strftime('%d/%m/%Y')
    todays_bookings = []
    for appointment in appointments:
        if appointment["date"] == correct_format_today:
            todays_bookings.append(appointment)
    if todays_bookings:
        print('todays appointments: ')
        show_appointment(todays_bookings)
    else:
        print('no appointments booked for today')
    back_to_menu()


''' this function allow user to return to main menu by clicking 1'''


def back_to_menu():
    while True:
        user_click = int(input('click 1 to go back to main menu '))
        try:
            if user_click == 1:
                screen_clear()
                break
        except ValueError:
            print('please enter 1 to  go back to main menu')


'''define this function to handle user to
navigate between search appointments and main menu'''


def handle_to_user_click(appointments):
    while True:
        try:
            user_click = int(input('Click 1 to go back to the main menu '
                                   'or click 2 to stay on this page: '))
            if user_click == 1:
                screen_clear()
                return True
            elif user_click == 2:
                screen_clear()
                return False
            else:
                print(' ivalid option please chosse 3 or 4')
        except ValueError:
            print('please use only numbers')
    return appointments


''' search appointment function  help user
to search appointments by name or by date,
if specified appointment exists it displays on screen
if not simply says there is no appointments for specified  date(or name)'''


def search_appointment(appointments):
    screen_clear()
    while True:
        try:
            search_method = int(input('Please mark one option below:\n'
                                      '1) Search appointment by date\n'
                                      '2) Search appointment by name\n'))
            screen_clear()
        except ValueError:
            print('please use only numbers ')
            continue
        if search_method == 1:
            date = input('Please enter date(dd/mm/yyyy): ')
            date_obj = date_validation(date)
            if date_obj:
                screen_clear()
                appointments_date = []
                for appointment in appointments:
                    if appointment['date'] == date_obj.strftime('%d/%m/%Y'):
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
            name_input = input('please enter name \n')
            name = name_validator(name_input)
            if name:
                appointments_name = []
                for appointment in appointments:
                    if appointment['name'] == name_input:
                        appointments_name.append(appointment)
                if appointments_name:
                    print('appointments for specified name : \n ')
                    show_appointment(appointments_name)
                    if handle_to_user_click(appointments):
                        return appointments
                else:
                    print('no appointments for specified name \n ')
                    if handle_to_user_click(appointments):
                        return appointments
    return appointments


''' Allow the user to cancel an appointment by providing name and date.'''


def cancell_appointment(appointments):
    screen_clear()
    while True:
        name = input('Please enter your name: ')
        screen_clear()
        if not name_validator(name):
            print('Invalid name format. Please enter a valid name.')
        else:
            date = input('Enter the date of the appointment you want to cancel (dd/mm/yyyy): ')
            screen_clear()
            date_obj = date_validation(date)
            if date_obj:
                appointment_to_cancel = None
                for appointment in appointments:
                    if appointment['date'] == date_obj.strftime('%d/%m/%Y') and appointment['name'] == name:
                        appointment_to_cancel = appointment
                        break  # Found the appointment to cancel, exit the loop
                if appointment_to_cancel:
                    appointments.remove(appointment_to_cancel)
                    with open(FILE_PATH, 'w') as file:
                        json.dump(appointments, file)
                    print('Your appointment has been canceled.')
                    show_appointment([appointment_to_cancel])  # Show the canceled appointment details
                else:
                    print('No appointment found for the specified name and date.')
                back_to_menu()
                return appointments
            else:
                print('Invalid date format. Please use dd/mm/yyyy format.')
                back_to_menu()
                return appointments


''' this function allows user to book
an appointment by specifying name date  and time'''


def book_appointment(appointments):
    screen_clear()
    while True:
        date = input('Please let us know when you want to book an appointment '
                     '(dd/mm/yyyy): \n')
        screen_clear()
        date_obj = date_validation(date)
        if date_obj:
            break
    day, month, year = date_obj.day, date_obj.month, date_obj.year
    current_year = datetime.now().year
    today = datetime.now().date()
    if 1 <= day <= 31 and 1 <= month <= 12 and year >= current_year:
        if month == 2:
            max_day = 29
        elif month in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31
        if 1 <= day <= max_day:
            appointment_date = datetime(year, month, day).date()
            correct_format_date = appointment_date.strftime('%d/%m/%Y')
            if appointment_date < today:
                screen_clear()
                print('date is in past, please enter  future or todays date ')
                back_to_menu()
            elif appointment_date.weekday() in [5, 6]:
                screen_clear()
                print('Please choose another option because we are closed '
                      'on weekends')
                back_to_menu()
            else:
                name = input('please enter your name \n').strip()
                screen_clear()
                if name_validator(name):
                    try:
                        time_options = int(input('Please choose '
                                                 'one option below \n  '
                                                 '1) 09:00\n'
                                                 '2) 10:00\n'
                                                 '3) 11:00\n'
                                                 '4) 12:00\n'
                                                 '5) 14:00\n'
                                                 '6) 15:00\n'))
                        if time_validator(time_options):
                            time_availibilities = [
                                '09:00', '10:00', '11:00',
                                '12:00', '14:00', '15:00'
                                ]
                            time = time_availibilities[time_options-1]
                            booked_time = booked_times(
                             appointments, correct_format_date)
                            screen_clear()
                            if time in booked_time:
                                print(f'{time} on {correct_format_date}'
                                      'is already booked,'
                                      'please try another time')
                                back_to_menu()
                            else:
                                new_appointment = {
                                    'name': name,
                                    'date': correct_format_date,
                                    'time': time
                                }
                                print(f'Your appointment has been booked for '
                                      f'{correct_format_date} at {time} '
                                      f'{name}, see you soon')
                                appointments.append(new_appointment)
                                with open('appointments.json', 'w') as file:
                                    json.dump(appointments, file)
                                just_booked(new_appointment)
                                back_to_menu()
                        else:
                            print('invalid time option'
                                  'please choose  a valid one')
                            back_to_menu()
                    except ValueError:
                        print('please enter only number from '
                              '1 to 6 for time option')
                        back_to_menu()
                else:
                    print('invalid name format,'
                          'name should only include letters')
        else:
            print('Invalid date format. Please use valid dd/mm/yyyy format.')
    else:
        print('Invalid date format. Please use valid dd/mm/yyyy format.')
    return appointments
    screen_clear()


''' this is main menu function which
is responsible to display main menu
and let user to chooose one option '''


def main_menu():
    screen_clear()
    try:
        with open(FILE_PATH, 'r') as file:
            appointments = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        appointments = []
    while True:
        print('Welcome to the hair-beauty booking app \n')
        try:
            user_choice = int(input(
                                'please select one option below \n'
                                '1) book an appointment \n'
                                '2) Todays appointments\n'
                                '3) search appointment\n'
                                '4) cancell appointment\n'
                                '0) Quit \n '
                                ))
            if user_choice == 1:
                appointments = book_appointment(appointments)
            elif user_choice == 2:
                todays_appointments(appointments)
            elif user_choice == 3:
                appointments = search_appointment(appointments)
            elif user_choice == 4:
                appointments = cancell_appointment(appointments)
            elif user_choice == 0:
                screen_clear()
                print('Good Bye')
                break
            else:
                screen_clear()
                print('Invalid input. Please select a valid option.')
        except ValueError:
            screen_clear()
            print('please use only numbers from 0 to 4')


if __name__ == '__main__':
    # call the main menu function to start application
    main_menu()
