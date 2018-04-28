class Car(object):

    # Variables
    regNo = None
    make = None
    model = None
    variant = None
    price = None
    year = None
    colour = None
    mileage = None
    seats = None
    doors = None
    body = None
    engine = None
    gearbox = None
    drivetrain = None
    fuel = None
    insurance = None
    consumption = None
    tax = None
    acceleration = None
    emissions = None

	def __init__(self, results):
		# Assign each value in the session array
		# to the local attribute
		for k, v in results.iteritems():
			setattr(self, k, v)
