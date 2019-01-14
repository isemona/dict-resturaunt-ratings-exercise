"""Restaurant rating lister."""


# put your code here
import sys

filename = sys.argv[1]
ratings = {}
for line in open(filename):
    new_tup = tuple(line.rstrip().split(":"))
    ratings[new_tup[0]] = new_tup[1]

for key,value in sorted(ratings.items()):
    print("{} is rated at {}.".format(key,value))
