# Data Annotation Tool

A Django web application for uploading and annotating (retailer and segment information only) CSV files

## Setup Instructions

### 1. Clone the Repository
```bash
git clone AmyshaDixon/data_annotater
cd data_annotater
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

### 6. Access the Application
Open your browser and navigate to: `http://127.0.0.1:8000/`

### 7. (Optional) Create a SuperUser
```bash
python manage.py createsuperuser
```

### 8. (Optional) Access the Admin Interface
In your browser, navigate to: `http://127.0.0.1:8000/admin`

## CSV Format

Your CSV file should include the following columns:
- `merchant` - Merchant name
- `sku` - Product SKU
- `productcountry` - ISO country code
