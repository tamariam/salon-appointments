# **SALON-APPOINTMENTS**

![responsive-image!](/views/assets/images/responsive.png)


## introduction
salon-appointments is python terminal app,which runs on a mock terminal in Heroku.The program is aimed at helping a salon manage patient appointments.This app provides a user-friendly and convenient way to handle appointment bookings and updates.
here is link of live[link](https://salon-appointments-6179b752c1c9.herokuapp.com/?fbclid=IwAR2x-9_64jEAfkuD--ZYmFj9lUsE7TI0OsEsGUH8_Jiw3SymieOm-HKvgko).


## Purpose
The purpose of this program is to make appointment booking and record tracking easier and faster for the user.
## Target Audience
- Salon owners
- stylists
- Freelance stylists
- People who prefer to book appointments online rather than by phone.

## Features

### Main Menu
The main menu offers users easy navigation and presents five key options, which are visible in the image below. Each feature will be explained in detail.

![main-menu!](/views/assets/images/main%20-menu.png)

If the user accidentally enters an invalid input, the application will display an appropriate error message. The error message will vary depending on whether the user enters a letter or an incorrect number.
![invalid-input!](/views/assets/images/main-menu%20if%20enter%20invalid%20input.png)
![invalid-input!](/views/assets/images/main-menu-letters.png)


### book appintment
As shown in the image above, the first option is 'Book Appointment.' When the user selects option 1, an empty page opens, prompting the user to enter the appointment date.
[!make-ppointment!](/views/assets/images/booking-date.png)

- This app allows users to input and retrieve validated data. If a user accidentally enters an invalid date format, the app will provide a notification.
![invalid-date!](/views/assets/images/booking-nvalid-date.png)
- If user correctly enters date, then will be asked to enter name.
![name!](/views/assets/images/cancell-appointment-name.png)
- If a user enters an invalid name format, they will be informed with an appropriate error message
![invalid-name-format!](/views/assets/images/invalid-name.png)
- if name is entered correctly, then user should be able to select appropriate time.
![booking-time!](/views/assets/images/booking-select-time.png)
-If user accidently press incorrect key, will be informed about it.
![nonvalid-time!](/views/assets/images/booking-%20if-nonvalid-time.png)
- if time on  date entered is not available , user will be informed.
![no-available!](/views/assets/images/no-avability.png)
- After successfully booking an appointment, the user will see the message displayed in the image below.
![appointment-booked!](/views/assets/images/appointment%20booked.png)
