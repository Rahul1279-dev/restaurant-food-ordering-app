# QR-Based Restaurant Menu (Django Project)

## Overview

This project is a **Django-based web application** that enables restaurants to provide a **QR code-powered digital menu**. Customers can scan a QR code to instantly access the restaurant’s menu on their device, eliminating the need for physical menus.

The application includes basic menu display functionality, item detail pages, and a simple structure that can be extended for ordering, payments, or admin control.

---

## Features

* 📱 QR code generation for menu access
* 🍽️ Dynamic restaurant menu display
* 📄 Individual menu item detail pages
* 🧩 Modular Django app structure
* 🎨 HTML templates with base layout support
* 🗄️ SQLite database (default)

---

## Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML (Django Templates)
* **Database:** SQLite3
* **Other:** QR code generation via Python script

---

## Project Structure

```
qr_proj/
│
├── manage.py
├── db.sqlite3
├── qr.py                # Script to generate QR code
├── qr.png               # Generated QR code image
│
├── mysite/              # Main Django project
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── restaurant_menu/     # Core app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   └── menu_item_detail.html
│   └── migrations/
│
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd qr_proj
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django
```

*(Add any additional dependencies if used in `qr.py` like `qrcode`)*

---

## Running the Project

### Apply migrations

```bash
python manage.py migrate
```

### Start development server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## QR Code Usage

The file `qr.py` is used to generate a QR code (`qr.png`) that links to the menu URL.

### Example usage:

```bash
python qr.py
```

You can print or display this QR code for customers to scan.

---

## Application Flow

1. User scans QR code
2. Redirected to the homepage (`index.html`)
3. Menu items are displayed
4. Clicking an item opens detailed view (`menu_item_detail.html`)

---

## Future Improvements

* Admin dashboard for menu management
* Categories (Starters, Main Course, etc.)
* Online ordering system
* Payment integration
* Mobile-first UI improvements
* API support (DRF)

---

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new features.

---

## License

This project is open-source and available under the MIT License.

---

## Author

Developed as a simple QR-based digital menu system using Django.
