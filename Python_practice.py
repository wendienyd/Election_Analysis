print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#outputs all three counties
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

#same as above but modified using the range() function
for num in range(5):
    print(num)

#outputs all three counties with the range() function
for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

#Getting the values
for voters in counties_dict.values():
    print(voters)

#Getting the values
for counties in counties_dict:
    print(counties_dict[county])

#Getting the values
for county in counties_dict:
    print(counties_dict.get(county))

#Getting all three counties w their values
for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voter.")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    F"You received {candidate_votes:,} number of votes."
    F"The total number of votes in the election was {total_votes:,}."
    F"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

