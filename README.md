# Base

### Hotel website and hotel management app

A two-sided hotel app, with one side focused on future and current guests, and a second side built for hotel employees. The public-facing side shows off the hotel and its amenities. It also allows users to create an account, make reservations, and update guest details. The employee-only side, which takes advantage of Django's built-in admin features, allows specific users to manage all of the hotel’s reservations, as well as the accounts of guests. It even includes a simple housekeeping system that tracks which rooms have been cleaned.

---

## Planning

Initial planning for the app consisted of three elements: wireframes, user stories and an entity relationship diagram (ERD) for mapping out the structure of the database.

### Wireframes

<!-- prettier-ignore -->
URL: /
![Home page wireframe](planning/wireframes/guest-home.png)
URL: /booking/step1
![Booking step 1 page wireframe](planning/wireframes/guest-booking-step1.png)
URL: /booking/step2
![Booking step 2 page wireframe](planning/wireframes/guest-booking-step2.png)
URL: /booking/:id/confirmation
![Booking confirmation page wireframe](planning/wireframes/guest-booking-confirmation.png)
URL: /create-account
![Create account page wireframe](planning/wireframes/guest-create-account.png)
URL: /guest/:id/profile
![Profile page wireframe](planning/wireframes/guest-profile.png)

### Database ERD

![Database ERD](planning/erd/base-erd.png)

### User Stories

Given that there are two different interfaces, two categories of user stories are required: guests and employees.

<!-- prettier-ignore -->
| Story | Type |
| - | - |
| As a potential guest, I want to see lots of photos of the hotel's rooms and common areas, so I can get a sense of the hotel's style and decide whether it's someplace I want to stay. | Guest |
| As a potential guest, I want to see a comprehensive list of the hotel's amenities, so I can know whether it will have what I want, like a gym. | Guest |
| As a potential guest, I want to see a map of where the hotel is located, so I can determine whether it's close to where I want, or need, to be. | Guest |
| As a potential guest, I want to learn about the area around the hotel, so I can know whether there will be things to do nearby. | Guest |
| As a guest who has decided to book a stay, I want to see multiple photos of every room type, so I can pick a room I know I'll be happy with. | Guest |
| As a guest who has decided to book a stay, I want to see the total cost of my future stay, and its breakdown, prior to booking, so I can determine whether the price is fair and something I can afford. | Guest |
| As a guest who has booked a future stay, I want to see the details of all my bookings, so I can confirm their accuracy and reference them prior to my stay. | Guest |
| As an employee who manages bookings, I want to make, change, and cancel bookings on behalf of guests, so I can help them when they contact the hotel. | Employee |
| As an employee who manages bookings, I want to see whether the hotel has available rooms on any given day, so I can help guests make or change a booking. | Employee |
| As an employee who manages bookings, I want to be able to add notes to a booking, as well as a guest's profile, so I can record guest requests and preferences. | Employee |
| As a housekeeping employee, I want to see a list or graph of the rooms that need to be cleaned or turned over, so I can plan my shift accordingly. | Employee |
| As a housekeeping employee, I want to notify other employees when I've turned over a room, so they can finalize check-in and give the next guest a key. | Employee |

---

## Technology Used

Trip Planner is a full-stack app, built primarily with Django. The Bootstrap framework is incorporated on the front-end, and utilized languages include HTML, CSS, Python, and SQL.

---

## Installation

Here are instructions for installing the app on your local machine.

1. Clone the copy to your local machine.

```
git clone https://github.com/alanavery/base
```

2. Download and install Python. If working on Python 2, install pip (package manager) as well.

3. Create a virtual environment for the project and activate it in your terminal.

4. Navigate to the project's root directory and run the following command to install all of the packages required to run the project:

```
pip3 install -r requirements.txt
```

5. This app utilizes PostgreSQL for its database system. If you don't have PostgreSQL installed on your local machine, you can download it [here.](https://www.postgresql.org/download/)

6. With PostgreSQL installed, create a database on your local machine named `base` and migrate the project's models to it.

```
python3 manage.py makemigrations
python3 manage.py migrate
```

7. Start the server, then check to see that the project is running on your local host.

```
python3 manage.py runserver
```
