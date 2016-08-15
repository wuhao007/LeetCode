# enum type for Vehicle
class VehicleSize:
    Motorcycle = 1
    Compact = 2
    Large = 3
    Other = 99

class Vehicle:
    # Write your code here
    def __init__(self):
        self.parking_spots = []
        self.spots_needed = 0
        self.size = None
        self.license_plate = None

    def get_spots_needed(self):
        return self.spots_needed

    def get_size(self):
        return self.size

    def park_in_spot(self, spot):
        self.parking_spots.append(spot)

    def clear_spots(self):
        for spot in self.parking_spots:
            spot.remove_vehicle()
        
        self.park_sports = []  

    def can_fit_in_spot(self, spot):
        raise NotImplementedError('This method should have implemented.')


class Motorcycle(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Motorcycle

    def can_fit_in_spot(self, spot):
        return True


class Car(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 1
        self.size = VehicleSize.Compact

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large or \
                spot.get_size() == VehicleSize.Compact


class Bus(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spots_needed = 5
        self.size = VehicleSize.Large

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large


class ParkingSpot:
    # Write your code here
    def __init__(self, lvl, r, n, sz):
        self.level = lvl
        self.row = r
        self.spot_number = n
        self.spot_size = sz
        self.vehicle = None

    def is_available(self):
        return self.vehicle == None

    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park(self, v):
        if not self.can_fit_vehicle(v):
            return False

        self.vehicle = v
        self.vehicle.park_in_spot(self)
        return True

    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None

    def get_row(self):
        return self.row
    
    def get_spot_number(self):
        return self.spot_number

    def get_size(self):
        return self.spot_size


class Level:
    # Write your code here
    def __init__(self, flr, num_rows, spots_per_row):
        self.floor = flr
        self.spots_per_row = spots_per_row
        self.number_spots = 0
        self.available_spots = 0;
        self.spots = []
        
        for row in xrange(num_rows):
            for spot in xrange(0, spots_per_row / 4):
                sz = VehicleSize.Motorcycle
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

            for spot in xrange(spots_per_row / 4, spots_per_row / 4 * 3):
                sz = VehicleSize.Compact
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

            for spot in xrange(spots_per_row / 4 * 3, spots_per_row):
                sz = VehicleSize.Large
                self.spots.append(ParkingSpot(self, row, self.number_spots, sz))
                self.number_spots += 1

        self.available_spots = self.number_spots
        
    def park_vehicle(self, vehicle):
        if self.get_available_spots() < vehicle.get_spots_needed():
            return False

        spot_num = self.find_available_spots(vehicle)

        if spot_num < 0:
            return False
        return self.park_starting_at_spot(spot_num, vehicle)

    def find_available_spots(self, vehicle):
        spots_needed = vehicle.get_spots_needed()
        last_row = -1
        spots_found = 0
        
        for i in xrange(len(self.spots)):
            spot = self.spots[i]
            if last_row != spot.get_row():
                spots_found = 0
                last_row = spot.get_row()
            if spot.can_fit_vehicle(vehicle):
                spots_found += 1
            else:
                spots_found = 0
            
            if spots_found == spots_needed:
                return i - (spots_needed - 1)

        return -1

    def park_starting_at_spot(self, spot_num, vehicle):
        vehicle.clear_spots()
        success = True

        for i in xrange(spot_num, spot_num + vehicle.get_spots_needed()):
            success = success and self.spots[i].park(vehicle)
        
        self.available_spots -= vehicle.get_spots_needed()
        return success

    def spot_freed(self):
        self.available_spots += 1

    def get_available_spots(self):
        return self.available_spots


class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        # Write your code here
        self.levels = []
        for i in xrange(n):
            self.levels.append(Level(i, num_rows, spots_per_row))

    # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        # Write your code here
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        # Write your code here
        vehicle.clear_spots()
