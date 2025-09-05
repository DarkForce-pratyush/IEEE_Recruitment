# Define the cutoff list with tuples (Campus, Branch, Cutoff) 2024 cutoff
cutoff_list = [
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Eco", 271),
    ("Pilani", "Bio", 236),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "Eco", 263),
    ("Goa", "Bio", 234),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Eco", 261),
    ("Hyderabad", "Bio", 234),
]

# Convert the list of tuples into a nested dictionary
cutoff_dict = {}
for campus, branch, cutoff in cutoff_list:
    if campus not in cutoff_dict:
        cutoff_dict[campus] = {}
    cutoff_dict[campus][branch] = cutoff

# Print the nested dictionary
print(cutoff_dict)