import copy
my_street = "Tomášikova"
duplicate_of_my_street = my_street
duplicate_of_my_street = "Jana Babáka"
print(my_street)
print(duplicate_of_my_street)
my_sports = ["hokej", "fotbal", "plavání","basketbal", "volejbal", "lyžování", "bruslení", "gymnastika"]
duplicate_of_my_sports = copy.deepcopy(my_sports)
duplicate_of_my_sports[-1] = "cyklistika"
print(my_sports)
print(duplicate_of_my_sports)