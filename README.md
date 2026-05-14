# NOT CANDIES

A sleek, cyberpunk-styled web application for managing a candy/product inventory with a modern UI and real-time database connectivity.

## Features

- 🎨 Modern cyberpunk design with neon gradient effects
- 📊 View all products in a responsive table
- 🔍 Search for individual products by ID
- ➕ Add new products to the database
- 🗄️ Real-time database connection status checker
- 📱 Fully responsive layout
- ✨ Smooth animations and visual feedback

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL (PyMySQL)
- **Frontend**: HTML, CSS (Jinja2 templating)
- **Styling**: Custom CSS with gradient animations

## Project Structure

```
Not_Candies/
├── app.py                 # Flask application and routes
├── README.md             # This file
├── static/
│   └── style.css        # Main stylesheet
├── templates/
│   ├── base.html        # Base template with header/footer
│   ├── home.html        # Home page with product management UI
│   └── footer.html      # Fixed footer component
└── img/
    └── favicon_NC.png   # Project favicon
```

## Installation

### Prerequisites

- Python 3.7+
- MySQL Server running locally
- Virtual environment (recommended)

### Setup Steps

1. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install flask pymysql
   ```

3. **Configure the database**
   - Create a MySQL database named `chucheria`
   - Create a table `chuches` with the following structure:
     ```sql
     CREATE TABLE chuches (
         id INT AUTO_INCREMENT PRIMARY KEY,
         nombre VARCHAR(255) NOT NULL,
         descripcion TEXT NOT NULL
     );
     ```

4. **Update database credentials** (if needed)
   - Edit `app.py` and update the `get_connection()` function with your MySQL credentials

5. **Run the application**
   ```bash
   python app.py
   ```
   
   The app will start on `http://127.0.0.1:5001/`

## Usage

### Home Page (`/`)
- View all products in the database
- Search for a product by ID
- Add a new product
- Check database connection status

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page with UI |
| GET | `/db` | Check database connection (JSON) |
| GET | `/candies` | Get all products (JSON) |
| GET | `/candies/<id>` | Get a specific product by ID (JSON) |
| POST | `/candies` | Add a new product (form data) |

### Form Parameters

**Add Product**
- `nombre` (required): Product name
- `descripcion` (required): Product description

**Search Product**
- `candy_id` (required): Product ID to search for

## Database Schema

**Table: `chuches`**

| Column | Type | Constraints |
|--------|------|-------------|
| id | INT | AUTO_INCREMENT, PRIMARY KEY |
| nombre | VARCHAR(255) | NOT NULL |
| descripcion | TEXT | NOT NULL |

## Features in Detail

### 1. Product List
Displays all products from the database in a clean, sortable table with hover effects.

### 2. Search Functionality
Enter a product ID to instantly search and display product details. Shows clear error messages if the product is not found.

### 3. Add Product
Simple form to insert new products into the database with real-time confirmation.

### 4. Database Connection Checker
Button to verify the application's connection to MySQL. Provides instant feedback on connection status with color-coded responses (green for success, pink for failure).

## Styling

The application features a custom cyberpunk aesthetic with:
- Dark background (`#0a0a0a`)
- Neon gradients (magenta to cyan)
- Glassmorphism effects (semi-transparent cards with backdrop blur)
- Smooth animations and transitions
- Responsive design for mobile, tablet, and desktop

## Error Handling

- Database connection errors are caught and displayed to the user
- Form validation ensures required fields are filled
- HTTP error responses with appropriate status codes (404 for not found, 400 for bad requests, 500 for server errors)

## Notes

- The application uses port `5001` to avoid conflicts with other Flask projects
- All product names and descriptions are stored in Spanish-language field names (`nombre`, `descripcion`)
- The footer is fixed and displays system operational status

## License

Created by Nil Creus © 2026 NOT CANDIES LABS

## Future Enhancements

- User authentication and authorization
- Product image uploads
- Advanced filtering and sorting
- Export product data to CSV
- Product categories and tags
- Inventory quantity tracking
