# OpenShop – Django Backend API

## Project Overview

OpenShop is an e-commerce platform developed by the Technical Steering Committee (TSC) team with the
goal of creating an open and accessible online marketplace. The platform is designed to allow
sellers from various product categories to offer their products easily, while providing users with a
simple and scalable shopping experience.

This project represents the **first development phase**, focusing on building a **core REST API**
for product management. Future enhancements are planned to include wishlist features, product search
and filtering, and price comparison across stores.

---

## Key Features

- Add new products
- Update existing product information
- Delete products
- Retrieve product data from the database

---

## Tech Stack

- Python **3.10**
- Django
- Pipenv (dependency management)
- pyenv (Python version management)
- SQLite (default development database)

---

## 🚀 Getting Started

Follow the steps below to run the project locally.

---

### 1️⃣ Clone the Repository

Clone the repository from Github and switch to the new directory:

    git clone https://github.com/raihanromzi/dicoding-openshop-django-be.git
    cd dicoding-openshop-django-be

Setup Python version:

    pyenv install 3.10
    pyenv local 3.10

Create a virtual environment and install dependencies from Pipfile.lock

    make setup

Apply database migration

    make migrate

Run development server

    make run