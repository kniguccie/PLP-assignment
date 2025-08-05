# Create a program that stores a list of words. Then, 
# use list comprehension to create a new list that contains only the words that have an odd number of characters

my_list = ["Serendipity", "Quasar", "Umbrella", "Luminous", "Kaleidoscope", "Ephemeral", "Nexus", "Zephyr", "Labyrinth", "Mirage"]

new_list = []
for x in  my_list:
  if len(x) % 2 != 0:
    new_list.append({x})
print(new_list)