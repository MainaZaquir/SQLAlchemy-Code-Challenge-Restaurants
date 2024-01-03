# Imporing the classes
from customer import Customer
from restaurant import Restaurant
from review import Review

# Creating the engine and the session
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Our example code
customer1 = Customer("Elvin", "Kamau")
customer2 = Customer("Ryan", "Kuria")

restaurant1 = Restaurant("Mama Nilishe")
restaurant2 = Restaurant("Shawarma Street")

review1 = customer1.add_review(restaurant1, 4)
review2 = customer2.add_review(restaurant1, 5)
review3 = customer1.add_review(restaurant2, 3)

# Access information
print(customer1.full_name())  
print(restaurant1.average_star_rating())  
print(Customer.find_by_name("Elvin Kamau")) 
print(Customer.find_all_by_given_name("Elvin"))  
