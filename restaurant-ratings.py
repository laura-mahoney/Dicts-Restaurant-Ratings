# your code goes here
# import sys
# get_scores = open(sys.argv[0])
# import unicode


def rate_restaurant(scores):
    """Opens given text file and creates a dictionary"""
    get_scores = open(scores)
    restaurant_ratings = {}

    for line in get_scores:
        restaurant_names_ratings = line.rstrip().split(":")
        restaurant_ratings[restaurant_names_ratings[0]] = restaurant_names_ratings[1]
    return restaurant_ratings

# print rate_restaurant("scores.txt")

def print_restaurant_ratings(restaurant_ratings):
    for restaurant in restaurant_ratings:
        print "{} is rated at {}".format(restaurant, restaurant_ratings[restaurant])
    return "print successfully"

restaurant_dictionary = rate_restaurant("scores.txt")

printed_ratings = print_restaurant_ratings(restaurant_dictionary)