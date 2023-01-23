def buildProfile(first, last, ** userInfo):
    """Builds a user profile."""
    userInfo["firstName"] = first
    userInfo["lastName"] = last
    return userInfo


user = buildProfile("kaitlynn", "beston", 
dreamJob = "computer programmer", 
favoriteAnimal = "dog", education = "high school")


for key, value in user.items():
    print(f"{key}: {value} \n")
