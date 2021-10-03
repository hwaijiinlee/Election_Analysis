temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")
#What is the score?
score = int(input("What is your test score?"))
#Determine the grade.
if score >= 90:
    print("Your grade is an A")
elif score >= 80:
    print("Your grade is a B")
elif score >=70:
    print("Your grade is a C")
elif score >=90:
    print("Your grade is a D")
else:
    print("Your grade is an F")
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
percentage_votes = (my_votes / total_votes * 100)
print(f"I received {my_votes / total_votes*100}% of the total votes.")

