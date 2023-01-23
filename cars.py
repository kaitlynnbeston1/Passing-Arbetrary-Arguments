def makeCar(manufacturer, name, **args):
    """ Designs a car. """
    args["carManufacturer"] = manufacturer
    args["carName"] = name
    return args
car = makeCar("ford", "f150", 
color = "white",
heatedSeats = "yes")

for key, value in car.items():
    print(f"{key}: {value}")