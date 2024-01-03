from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        return max(self.restaurants, key=lambda restaurant: restaurant.reviews)

    def add_review(self, restaurant, rating):
        review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        session.add(review)
        session.commit()
        return review

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

    @classmethod
    def find_by_name(cls, full_name):
        first_name, last_name = full_name.split()
        return session.query(cls).filter_by(first_name=first_name, last_name=last_name).first()

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return session.query(cls).filter(cls.first_name == given_name).all()
