import os
import csv

csvpath = os.path.join("..", "resources", "election_data.csv")

with open(csvpath,"r") as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))

# Header
print("Election Results")
print("--------------------------")

# The total number of votes cast 
Total = "amount"
for Total in range():
    print(Total)

# A complete list of candidates who received votes 
List = "candidates"
len(List)
print(len(List))


# The percentages of votes each candidate won 
len((Total/list) * 100)
print((Total/list) * 100)

# The total number of votes each candidate won 
sum(Total)
print(Total)

# The winner of the election based on popular vote 
Winner = "popular"
for Winner in List:
    print(Winner)
