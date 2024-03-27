# class Customer:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def reviews(self):
#         pass

#     def restaurants(self):
#         pass

#     def num_negative_reviews(self):
#         pass

#     def has_reviewed_restaurant(self, restaurant):
#         pass
    
# class Restaurant:
#     def __init__(self, name):
#         self.name = name

#     def reviews(self):
#         pass

#     def customers(self):
#         pass

#     def average_star_rating(self):
#         pass

#     @classmethod
#     def top_two_restaurants(cls):
#         pass
    
# class Review:
#     def __init__(self, customer, restaurant, rating):
#         self.customer = customer
#         self.restaurant = restaurant
#         self.rating = rating


class Customer:
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        self.restaurants = []
        self.all.append(self)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def add_review(self, review):
        self.reviews.append(review)

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def has_reviewed_restaurant(self, restaurant):
        return restaurant in self.restaurants

    def num_negative_reviews(self):
        return sum([1 for r in self.reviews if r.rating < 3])


class Restaurant:
    all = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        self.customers = []
        self.all.append(self)

    def __str__(self):
        return self.name

    def add_review(self, review):
        self.reviews.append(review)

    def add_customer(self, customer):
        self.customers.append(customer)

    def average_star_rating(self):
        return sum([r.rating for r in self.reviews]) / len(self.reviews)


class Review:
    all = []

    def __init__(self, customer, restaurant, rating):
        if isinstance(customer, str) or isinstance(restaurant, str):
            raise Exception("Customer and Restaurant should be instances of their respective classes.")

        if not isinstance(rating, int) or not 1 <= rating <= 5:
            raise Exception("Rating should be an integer between 1 and 5.")

        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        customer.add_review(self)
        restaurant.add_review(self)
        self.all.append(self)

    def __str__(self):
        return f"{self.customer.__str__()} reviews {self.restaurant.name} with a rating of {self.rating}"


# Include the following lines to make the all property work
Customer.all = []
Restaurant.all = []
Review.all = []

# Add the following line to complete the multiple inheritance
class MetaRestaurant(type(Restaurant), type(Customer)):
    pass

Restaurant = MetaRestaurant('Restaurant', (object,), dict(Restaurant.__dict__))