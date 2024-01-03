# Restaurant Review Management System

##Overview

- This project is a simple Restaurant Review Management System implemented using SQLAlchemy, a powerful SQL toolkit for Python. The system includes three main entities: Customer, Restaurant, and Review, with relationships between them to manage restaurant reviews.

## Project Structure

The project is organized into several files, each responsible for different components:

- `main.py`: Example usage and testing of the classes and methods.
- `customer.py`: Definition of the Customer class.
- `restaurant.py`: Definition of the Restaurant class.
- `review.py`: Definition of the Review class.
- `migrations.py`: Database migration script for setting up the initial schema.
- `models.py`: Shared SQLAlchemy models for the Customer, Restaurant, and Review classes.
  
## Installation and Setup

1. Clone the repository:
Copy this code `git clone https://github.com/MainaZaquir/SQLAlchemy-Code-Challenge-Restaurants.git` and then on your terminal run this code `cd SQLAlchemy-Code-Challenge-Restuarants`
2. Install dependencies:
Copy this code `pip install -r requirements.txt` and then run the migrations to set up the initial database schema copy this code `python migrations.py`
3. Run the main script for testing: Copy this code `python main.py`
   
# Usage

Feel free to use and extend this project as a foundation for your restaurant review management system. Update the classes and methods as needed for your specific requirements. You can integrate this system into a larger application or build additional features on top of it.

## Credits

This application was created by [Maina Zaquir](https://github.com/MainaZaquir).
This project uses SQLAlchemy for database interactions.

## Contributing

Contributions are always welcome! If you have any suggestions for improvement or would like to add new features, please feel free to open an issue or submit a pull request. I will look into it immediately.
