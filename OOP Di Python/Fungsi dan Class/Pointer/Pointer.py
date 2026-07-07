def my_function(*kids):
  print("The youngest child is " + kids[2])
  return kids

# If the number of arguments is unknown, add a * before the parameter name:

# Call the function and store the result
kids_names = my_function("Emil", "Tobias", "Linus")

# Loop through the returned kids_names
for i in range(len(kids_names)):
    print(f"{i+1} child's name: {kids_names[i]}")