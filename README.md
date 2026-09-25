# Django Online Store

This project is a Django-based e-commerce web application with sections for users, products, the shopping cart, and orders.

## Requirements

- Python 3
- Django and the other dependencies required by the project

## Setup

1. Navigate to the project directory:

```bash
cd shop
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# On Windows: .venv\Scripts\activate
```

3. Install the project dependencies. If a dependency file is available:

```bash
pip install -r requirements.txt
```

4. Set up the database and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Then visit http://127.0.0.1:8000/.

## Applications

- `home`: Main pages and the custom user model
- `account`: User accounts
- `product`: Products and categories
- `cart`: Shopping cart
- `order`: Orders
- `payment`: Payments

> The current settings are intended for development. Review the security settings and production configuration before deployment.