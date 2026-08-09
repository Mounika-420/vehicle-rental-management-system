# 🚗 Vehicle Rental Management System

> **Rent. Manage. Track. — All in one place.**

A web-based vehicle rental management system built using **Python Flask and MySQL**, designed to simplify vehicle management, customer bookings, booking history, and rental information through a single platform.

---

## 🎯 About the Project

Managing vehicle rentals manually can become difficult when handling vehicle availability, customer information, bookings, rental rates, and booking history.

The **Vehicle Rental Management System** provides a centralized web application where vehicle owners can manage vehicles and users can browse vehicles, make bookings, and view their rental information.

The system also includes a **database-powered chatbot assistant** that allows users to ask simple questions about vehicles, rates, bookings, profiles, and database information.

---

## ✨ Key Features

- 🔐 **User Registration & Login**
  - New users can create an account.
  - Registered users can securely log in.

- 👨‍💼 **Owner/Admin Management**
  - Owners can add rental vehicles.
  - Vehicle information and images can be managed through the application.

- 🚘 **Vehicle Management**
  - Vehicle type
  - Vehicle number
  - Vehicle model
  - Rental rate
  - Vehicle image

- 📅 **Vehicle Booking**
  - Users can select a vehicle.
  - Users can enter booking date and rental duration.
  - Booking information is stored in MySQL.

- 📋 **Booking History**
  - Users can view their booking information.
  - Owners can view booking requests related to their vehicles.

- 💰 **Vehicle Rates**
  - Rental rates are stored in the database.
  - Users can view vehicle pricing through the application.

- 🖼️ **Vehicle Image Upload**
  - Owners can upload vehicle images.
  - Uploaded images are displayed in the vehicle interface.

- 🤖 **Database Chatbot Assistant**
  - Users can ask questions about rental data.
  - The chatbot retrieves information directly from the application database.

- 👤 **User Profile**
  - Users can view their stored profile information.

---

## 🤖 Smart Rental Assistant

The project includes a lightweight chatbot integrated with the Flask application.

Users can ask questions such as:

```text
Available vehicles
Vehicle rates
My bookings
My profile
Show table columns
Help
```

The assistant processes the question and retrieves relevant information from the MySQL database.

### Example

```text
You: my profile

Bot: Profile:
name=Mounika,
role=owner,
username=Mounika
```

This makes database information easier to access without manually checking tables.

---

## 🧩 Application Flow

```text
                    👤 USER
                      │
                      ▼
                🔐 LOGIN / SIGNUP
                      │
                      ▼
              🚘 VEHICLE DASHBOARD
                      │
              ┌───────┴────────┐
              │                │
              ▼                ▼
        📅 BOOK VEHICLE     🤖 CHATBOT
              │                │
              ▼                ▼
        📋 BOOKING HISTORY   🗄️ DATABASE
              │                │
              └───────┬────────┘
                      ▼
                  🐬 MySQL
```

### Owner Flow

```text
Owner Login
     ↓
Owner Dashboard
     ↓
Add Vehicle
     ↓
Vehicle Details + Image
     ↓
MySQL Database
     ↓
View Booking Requests
```

### User Flow

```text
User Signup/Login
       ↓
Vehicle Dashboard
       ↓
View Vehicles
       ↓
Select Vehicle
       ↓
Enter Date & Duration
       ↓
Create Booking
       ↓
Booking Stored in MySQL
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Backend programming |
| 🌶️ Flask | Web application framework |
| 🐬 MySQL | Database |
| 🔌 PyMySQL | Python-MySQL connection |
| 🌐 HTML | Web page structure |
| 🎨 CSS | User interface styling |
| ⚙️ JavaScript | Client-side interaction |
| 🔐 python-dotenv | Environment variable management |
| 🧰 Git | Version control |
| ☁️ GitHub | Source code hosting |

---

## 📂 Project Structure

```text
vehicle_rental/
│
├── main.py
│
├── data_base.py
│
├── test_db.py
│
├── requirements.txt
│
├── vehicle_rental.sql
│
├── .gitignore
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── home.html
│   ├── user.html
│   ├── booking-history.html
│   └── chatbot.html
│
└── static/
    ├── css/
    │   └── styles.css
    │
    ├── image/
    │   └── bgv.webp
    │
    └── upload/
        └── vehicle images
```

---

## 🗄️ Database

The project uses **MySQL** as the backend database.

The database contains information related to:

```text
User Details
     ↓
Vehicle Details
     ↓
Booking Details
```

### Main Tables

#### `user_details`

Stores user and owner information.

```text
id
name
number
email
role
username
password
status
```

#### `add_vehicle`

Stores vehicle information.

```text
id
vehicle_type
number
model
rate
image
status
```

#### `add_book`

Stores booking information.

```text
id
vehicle_name
date
duration
user_id
vehicle_id
status
user_name
```

The complete database structure is provided in:

```text
vehicle_rental.sql
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Mounika-420/vehicle-rental-management-system.git
```

Move into the project directory:

```bash
cd vehicle-rental-management-system
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

After activation, the terminal should show:

```text
(venv)
```

---

## 4️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

If required, install the environment package manually:

```bash
pip install python-dotenv
```

---

## 5️⃣ Create the MySQL Database

Open MySQL and create the database:

```sql
CREATE DATABASE vehicle_rental;
```

Then import the provided SQL file:

```text
vehicle_rental.sql
```

---

## 6️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=vehicle_rental
```

Replace:

```text
your_mysql_password
```

with your local MySQL password.

### 🔒 Important

The `.env` file contains private database credentials and should **never be uploaded to GitHub**.

The project uses `.gitignore` to keep `.env` outside the repository.

---

## 7️⃣ Run the Application

Start the Flask application:

```bash
python main.py
```

If the application starts successfully, open:

```text
http://127.0.0.1:5000
```

---

# 🖥️ Application Pages

The application contains different pages for managing the rental process.

### 🔐 Login

Users and owners can log into the system.

### 📝 Signup

New users can register with their details.

### 🚘 Vehicle Dashboard

Users can view available vehicle information.

### 📅 Booking

Users can select a vehicle and create a rental booking.

### 📋 Booking History

Booking information can be viewed through the booking history page.

### 👨‍💼 Owner Dashboard

Owners can add vehicles and view booking requests.

### 🤖 Rental Assistant

Users can interact with the chatbot to retrieve rental information.

---

# 🔐 Security

The project uses environment variables for database configuration.

Instead of storing the database password directly in the source code:

```python
os.getenv("DB_PASSWORD")
```

is used to load the password from `.env`.

This prevents sensitive database credentials from being exposed in the GitHub repository.

> ⚠️ Never commit your real `.env` file or database password.

---

# 🚀 Future Enhancements

The project can be further improved with:

- 💳 Online payment integration
- 📧 Email booking confirmation
- 🔔 Booking notifications
- 📱 Fully responsive mobile interface
- 📊 Admin analytics dashboard
- 🔎 Advanced vehicle search and filtering
- ⭐ Vehicle reviews and ratings
- 📍 Location-based vehicle search
- 🤖 Advanced AI-powered rental recommendations
- 📄 Digital rental invoice generation
- 📈 Revenue and booking reports

---

# 📌 Project Highlights

```text
✔ Flask Web Application
✔ MySQL Database Integration
✔ User Authentication
✔ Vehicle Management
✔ Vehicle Booking
✔ Booking History
✔ Image Upload
✔ Database Chatbot
✔ Environment Variable Configuration
✔ Git & GitHub
```

---

# 🎓 Project Purpose

This project demonstrates practical implementation of:

- Web application development
- Backend programming
- Database management
- CRUD operations
- User authentication
- Session management
- File uploads
- Database integration
- Git/GitHub version control
- Chatbot-based database interaction

---

## 👩‍💻 Developer

### Mounika Selvaraj

Computer Science & Business Systems

---

## 🔗 Repository

**GitHub:**

https://github.com/Mounika-420/vehicle-rental-management-system

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

> **Vehicle Rental Management System — making vehicle rental management simple, organized, and accessible. 🚗✨**