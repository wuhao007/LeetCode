'''
Definition of Location:
class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        # This will create a new location object

Definition of Restaurant:
class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        # This will create a new restaurant object,
        # and auto fill id

Definition of Helper
class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        # return calculate the distance between two location

Definition of GeoHash
class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethom
    def encode(cls, location):
        # return convert location to a geohash string
    
    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        # return convert a geohash string to location
'''
import bisect
from YelpHelper import Location, Restaurant, GeoHash, Helper

class MiniYelp:

    def __init__(self):
        # initialize your data structure here.
        self.restaurants = {}
        self.ids = {}
        self.geo_value = []

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        # Write your code here
        restaurant = Restaurant.creat(name, location)
        hashcode = "%s.%s" % (GeoHash.encode(location), restaurant.id)
        bisect.insort(self.geo_value, hashcode)
        self.restaurants[hashcode] = restaurant
        self.ids[restaurant.id] = hashcode
        return restaurant.id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        # Write your code here
        hashcode = self.ids[restaurant_id]
        index = bisect.bisect_left(self.geo_value, hashcode)
        self.geo_value.pop(index)
        del self.restaurants[hashcode]
        del self.ids[restaurant_id]

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by 
    # distance from near to far.
    def neighbors(self, location, k):
        # Write your code here
        length = self.get_length(k)
        hashcode = GeoHash.encode(location)[0:length]
        left = bisect.bisect_left(self.geo_value, hashcode)
        right = bisect.bisect_right(self.geo_value, hashcode + '{')
        results = []
        for index in range(left, right):
            hashcode = self.geo_value[index]
            restaurant = self.restaurants[hashcode]
            distance = Helper.get_distance(location, restaurant.location)
            if distance <= k:
                results.append((distance, restaurant))
        results = sorted(results, key=lambda obj: obj[0])
        return [rt[1].name for rt in results]

    def get_length(self, k):
        ERROR = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.01911, 0.00478, 0.0005971, 0.0001492, 0.0000186]
        for i, error in enumerate(ERROR):
            if k > error:
                return i
        return len(ERROR)

