# Flighty :airplane:

#### DBMS Course Mini-Project

`Flighty` is a Flask-based web-app which allows users to create profiles, book and cancel tickets and print transaction info. The app also offers `admin` support so that the admin may add/ remove new flights, airports, airlines etc. as per requirement. The application stores the `session` data and the user may continue the session later. Accessing application endpoints like payment, bookticket(main app), profile require `authorization` and the user needs to login to gain access to these endpoints. As this is a mini-development project, ticket date feature has not been implemented as it requires continuous/ regular insertion of data. The MySQL queries include usage of clauses like `SELECT, INSERT, DELETE, JOIN` (for views) and the data is stored locally on the development machine. The ddl file describes the structure of the data and the insert file describes the data to be added.

------

### To use the app:
1. Clone the repository
2. Install **Flask** and **flask-mysql**
3. Navigate to the directory and set environment variable using:
```
$env:FLASK_APP = "flighty" (Windows)
```

  or

```
export FLASK_APP=flighty (UNIX bash)
```
4. Run the application using
```
flask run
```

   or

```
python(3) flighty.py (Dev server)
```

#### The application is now running on localhost port 5000.

-----

#### Usage:
- User 
```
Signup using necessary details and a unique username.

Login into your account 

Select a source and destination and check for available flights

Book ticket for a suitable flight

```

- Admin
```
Login using username: `admin` and passoword: `admin`

Add new flights, airports, airlines and check current list of users

```

------

### Technologies Used:
- HTML
- CSS
- JS
- Flask
- flask-mysql

------

### Content
- Home Page

![alt-text](https://github.com/ruheengl/Flighty/blob/master/Screenshots/Screenshot%20from%202020-11-01%2023-28-10.png)

- Login Page

![alt-text](https://github.com/ruheengl/Flighty/blob/master/Screenshots/Screenshot%20from%202020-11-01%2023-28-50.png)

- Sign Up

![alt-text](https://github.com/ruheengl/Flighty/blob/master/Screenshots/Screenshot%20from%202020-11-01%2023-29-09.png)

- Book Ticket

![alt-text](https://github.com/ruheengl/Flighty/blob/master/Screenshots/Screenshot%20from%202020-11-01%2023-30-51.png)

- Available Flights

![alt-text](https://github.com/ruheengl/Flighty/blob/master/Screenshots/Screenshot%20from%202020-11-01%2023-32-02.png)

- User Information (Profile)

![alt-text](https://github.com/ruheengl/Flighty/blob/master/Screenshots/Screenshot%20from%202020-11-01%2023-31-06.png)

- Previous Transactions/ Bookings and cancellation option

![alt-text](https://github.com/ruheengl/Flighty/blob/master/Screenshots/Screenshot%20from%202020-11-01%2023-32-35.png)

- Payment Successful

![alt-text](https://github.com/ruheengl/Flighty/blob/master/Screenshots/Screenshot%20from%202020-11-01%2023-32-10.png)

- Print Payment Info


![alt-text](https://github.com/ruheengl/Flighty/blob/master/Screenshots/Screenshot%20from%202020-11-01%2023-32-17.png)

------

### Group Members:
- [Ruhee Nagulwar](https://github.com/ruheengl)
- [Chinmay Dixit](https://github.com/chinmaydixit20)
