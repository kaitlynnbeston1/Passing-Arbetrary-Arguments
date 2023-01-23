def makeSandwich(*items):
    """Makes sandwich with requested toppings."""
    print("Making sandwich with the following items:")
    for item in items:
        print(item)


makeSandwich("turkey", "cheese", "mayo", "lettuce", "tomato")
makeSandwich("bacon", "lettuce", "tomato")
makeSandwich("cheese wiz")
