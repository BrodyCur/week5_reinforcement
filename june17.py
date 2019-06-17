class Location:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

class Trip:

    def __init__(self):
        self.stops = []

    def __str__(self):
        return f'{self.stops}'

    def add_location(self, location):
        self.stops.append(location)

    def trip_info(self):
        print('Began trip.')
        for num in range(0, len(self.stops) - 1):
            print(f'Travelled from {self.stops[num]} to {self.stops[num + 1]}')
        print('Ended trip.')


toronto = Location('Toronto')
montreal = Location('Montreal')
halifax = Location('Halifax')
winnipeg = Location('Winnipeg')
erieau = Location('Erieau')

my_trip = Trip()

my_trip.add_location(toronto)
my_trip.add_location(montreal)
my_trip.add_location(halifax)
my_trip.add_location(winnipeg)
my_trip.add_location(erieau)

my_trip.trip_info()