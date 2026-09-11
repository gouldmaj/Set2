# This code asks for the length of a given row, in feet
row_length = float(input("Enter the length of the row in feet: "))

# This code asks for the amount of distance, in feet used by the end-post assembly
end_post_assembly = float(input("Enter the amount of distance used by the end-post assembly in feet: "))

# This code asks for the amount of distance, in feet between vines
vine_distance = float(input("Enter the amount of distance between vines in feet: "))

# This code calculates the number of vines that can be planted in the row using the values provided by the user
vines_amount = (row_length - 2 * end_post_assembly) / vine_distance

# This code rounds the number of vines to the nearest whole number so it can be displayed as a whole number
vines_amount = round(vines_amount)