class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._last_name = value

    def reviews(self):
        return [review for review in Review.all if review.customer == self]

    def restaurants(self):
        return list(set([review.restaurant for review in self.reviews()]))

    def num_negative_reviews(self):
        return sum(1 for review in self.reviews() if review.rating <= 2)

    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self.reviews())


class Restaurant:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name

    name = property(get_name, set_name)

    def reviews(self):
        return [review for review in Review.all if review.restaurant == self]

    def customers(self):
        return list(set([review.customer for review in self.reviews()]))

    def average_star_rating(self):
        ratings = [review.rating for review in self.reviews()]
        return round(sum(ratings) / len(ratings), 1) if ratings else 0.0

    @classmethod
    def top_two_restaurants(cls):
        sorted_restaurants = sorted(cls.reviews(), key=lambda r: r.average_star_rating(), reverse=True)
        return sorted_restaurants[:2] if len(sorted_restaurants) >= 2 else None


class Review:
    all = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all.append(self)

    def get_rating(self):
        return self._rating

    def set_rating(self, val):
        if isinstance(val, int) and 1 <= val <= 5:
            self._rating = val

    rating = property(get_rating, set_rating)

    def get_customer(self):
        return self._customer

    def set_customer(self, value):
        if isinstance(value, Customer):
            self._customer = value

    customer = property(get_customer, set_customer)

    def get_restaurant(self):
        return self._restaurant

    def set_restaurant(self, value):
        if isinstance(value, Restaurant):
            self._restaurant = value

    restaurant = property(get_restaurant, set_restaurant)
