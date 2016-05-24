class Trip:
    def __init__(self, rider_id, lat, lng):
        self.id = 1
        self.rider_id = rider_id
        self.driver_id = None
        self.lat = lat
        self.lng = lng

class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
        return (lat1 - lat2) ** 2 + (lng1 - lng2) ** 2

class MiniUber:

    def __init__(self):
        # initialize your data structure here.
        self.drivers = {}
        self.riders = {}
        self.trip = None

    def search(self, lat, lng, positions):
        id = None
        mn = float("inf")
        for key, value in positions.items():
            distance = Helper.get_distance(lat, lng, value[0], value[1])
            if distance < mn:
                id = key
                mn = distance 
        return id    
            
        
    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        # Write your code here
        self.drivers[driver_id] = (lat, lng)
        if self.trip:
            if driver_id == self.trip.driver_id:
                return self.trip
        if not self.riders:
            return None
        rider_id = self.search(lat, lng, self.riders)
        rider_lat, rider_lng = self.riders[rider_id]
        trip = Trip(rider_id, rider_lat, rider_lng)
        trip.driver_id = driver_id
        if trip:
            self.riders.pop(rider_id, None)
            self.drivers.pop(driver_id, None)
        self.trip = trip
        return trip

    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        # Write your code here
        self.riders[rider_id] = (lat, lng) 
        if self.trip:
            if rider_id == self.trip.rider_id:
                return self.trip
        if not self.drivers:
            return None
        driver_id = self.search(lat, lng, self.drivers)
        trip = Trip(rider_id, lat, lng)
        trip.driver_id = driver_id
        if trip:
            self.riders.pop(rider_id, None)
            self.drivers.pop(driver_id, None)
        self.trip = trip
        return trip
        
miniuber = MiniUber()

def printtrip(trip):
    if trip:
        print trip.id, trip.rider_id, trip.driver_id, trip.lat, trip.lng
    else:
        print None
printtrip(miniuber.report(1, 36.1344, 77.5672))
printtrip(miniuber.report(2, 45.1344, 76.5672))
printtrip(miniuber.request(2, 39.1344, 76.5672))
printtrip(miniuber.report(1, 38.1344, 75.5672))
printtrip(miniuber.report(2, 45.1344, 76.5672))
