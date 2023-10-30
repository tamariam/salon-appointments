# **SALON-APPOINTMENTS**

![responsive-image!](/views/assets/images/responsive.png)

## introduction

salon-appointments is python terminal app,which runs on a mock terminal in Heroku.The program is aimed at helping a salon manage patient appointments.This app provides a user-friendly and convenient way to handle appointment bookings and updates.
Here is live[link](https://salon-appointments-6179b752c1c9.herokuapp.com/?fbclid=IwAR2x-9_64jEAfkuD--ZYmFj9lUsE7TI0OsEsGUH8_Jiw3SymieOm-HKvgko).

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

- If the user accidentally enters an invalid input, the application will display an appropriate error message. The error message will vary depending on whether the user enters a letter or an incorrect number.

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

### Todays appointments

If the user selects the second option from the main menu, they will navigate to the 'Today's Appointments' page. If appointments are booked for today, they will be displayed in the terminal; otherwise, an appropriate message will be shown.

![todays-appointments](/views/assets/images/todays-appointments.png)

![no-appointments-for-today!](/views/assets/images/today-no-appointments.png)

### Search appointments

After choosing the third option, the user can search for appointments by date or by name. Validations are in place for both date and name inputs, so if the user enters an invalid name or date format, they will be notified. If there are no appointments for the specified date, the user will receive a message to that effect. If appointments exist, the user can view their details.

![search-appointment!](/views/assets/images/search-appointment.png)

### cancell appointment

The Salon Appointments app allows users to cancel appointments. To cancel an appointment, the user should enter the name and date. If an appointment is booked for the specified date and name, it will be canceled. If no appointment exists with the provided details, the user will receive a message displayed on the screen.
![cancelled-appointment!](/views/assets/images/cancell-appointment%20.png)

### Quit

The final option is to enter '0,' which simply closes the program and displays the word 'Goodbye' on the screen.

### Back to Menu

Users can return to the main menu at any time by selecting option '1' while in any of the other menu options.

## Testing
I have manualy tested  this project by doing the folowing:

- Entered invalid date, name, time, or menu-option inputs to verify that the application returns appropriate error messages for incorrect data entry.

- Checked if it's possible to book an appointment at a time that is already booked.

- Confirmed that after canceling an appointment, it is no longer present in the appointment JSON file.

- Ensured that the 'Today's Appointments' option only displays appointments for the current day, if there are any.

## Bugs

### Fixed Bugs 

The 'Cancel Appointment' option did not work as expected. It correctly displayed a message indicating that the specified appointment was canceled, but it inadvertently canceled an older appointment with the same date

### Unfixed Bugs

There is no unfixed bugs.

## Validator testing
- Pep8

 - No errors were found when passing through the official ( Pep8) validator.

 ## Deployment
- fork this repository
- create a new Heroku app
- set the buldbacks to Python and Node JS in that order.
- Link the Heroku app in the repository
- Deploy

## Credits
- Code institute for the deployment terminal.
- Relyed on W3school, ChatGPt and MDN for general references throughout the project.



