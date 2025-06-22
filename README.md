# Flight Reservation System

A professional web-based application for managing flight reservations, built using **Python** and **PyQt5**, with **MySQL** for data storage and **Twilio** for SMS notifications.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

The Flight Reservation System is a user-friendly desktop application designed to streamline the process of booking, managing, and tracking flight reservations. It provides a graphical user interface (GUI) built with PyQt5, integrates with a MySQL database for persistent storage, and uses Twilio's API to send booking confirmation SMS to users.

---

## Features

- **User Authentication:** Secure login and registration for customers.
- **Flight Search:** Search for available flights based on source, destination, and date.
- **Booking Management:** Book, view, and cancel flight reservations.
- **Real-Time Notifications:** Receive SMS confirmations for bookings via Twilio.
- **Admin Panel:** Manage flight schedules, user data, and bookings (if implemented).
- **Responsive UI:** Intuitive interface with dynamic widgets and animations.

---

## Technologies Used

- **Python 3.x:** Core programming language.
- **PyQt5:** For building the graphical user interface.
  - `PyQt5.uic`: Loads UI files designed with Qt Designer.
  - `PyQt5.QtWidgets`: Provides widgets like dialogs, buttons, and stacked widgets.
  - `PyQt5.QtGui`: Handles graphical elements like QMovie for animations.
  - `PyQt5.QtCore`: Core non-GUI functionality.
- **MySQL Connector:** For database connectivity and operations.
- **Twilio API:** For sending SMS notifications.
- **datetime:** For handling date-related operations.
- **random:** For generating unique booking IDs or random data.
- **sys:** For system-specific parameters and functions.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- MySQL Server
- A Twilio account with a verified phone number
- Qt Designer (optional, for editing `.ui` files)

---

## Installation

**Clone the repository:**
```bash
git clone https://github.com/your-username/flight-reservation-system.git
cd flight-reservation-system
```

**Install Python dependencies:**
```bash
pip install PyQt5 mysql-connector-python twilio
```

**Set up MySQL database:**
- Create a database named `flight_reservation`.
- Import the provided `schema.sql` file (if available) or create tables as described in [Database Schema](#database-schema).

**Configure Twilio:**
- Obtain your Twilio Account SID, Auth Token, and a Twilio phone number from the [Twilio Console](https://console.twilio.com/).
- Update the configuration file or environment variables (see [Configuration](#configuration)).

---

## Configuration

**Database Configuration:**

Update the MySQL connection settings in the main application file (e.g., `main.py`):
```python
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="flight_reservation"
)
```

**Twilio Configuration:**

Set up Twilio credentials as environment variables or in a configuration file:
```bash
export TWILIO_ACCOUNT_SID='your_account_sid'
export TWILIO_AUTH_TOKEN='your_auth_token'
export TWILIO_PHONE_NUMBER='your_twilio_phone_number'
```
Alternatively, update the Twilio client initialization in the code:
```python
client = Client("your_account_sid", "your_auth_token")
```

**UI Files:**

Ensure all `.ui` files designed with Qt Designer are in the project directory and referenced correctly in the code.

---

## Usage

**Run the application:**
```bash
python main.py
```

**Navigate the UI:**
- Register or log in to access the system.
- Search for flights by entering source, destination, and travel date.
- Book a flight and receive an SMS confirmation.
- View or cancel bookings from the user dashboard.

**Admin Features (if implemented):**
- Log in with admin credentials to manage flights and users.

---

## Database Schema

The MySQL database (`flight_reservation`) includes the following tables (example schema, adjust as needed):

### `users` table
```sql
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15)
);
```

### `flights` table
```sql
CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(10) UNIQUE NOT NULL,
    source VARCHAR(50) NOT NULL,
    destination VARCHAR(50) NOT NULL,
    departure_date DATE NOT NULL,
    departure_time TIME NOT NULL,
    seats_available INT NOT NULL
);
```

### `bookings` table
```sql
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    flight_id INT,
    booking_date DATE NOT NULL,
    status ENUM('confirmed', 'cancelled') DEFAULT 'confirmed',
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or support, please contact:

- **Email:** aamodkumar2006@gmail.com
- **GitHub:** [Aamod007]((https://github.com/Aamod007))

---

Built with ❤️ by Aamod 
