

text = open('WorldSeriesWinners.txt')

reader = text.read().split('\n')

name = dict()

for line in reader:

    if line in name:
        name[line] += 1
    else:
        name[line] = 1

# for key in list(name.keys()):
#     print(key, ":", name[key], sep = ' ')


years = dict()

year = 1903

for line in reader:
    if year == 1903 or year == 1993:
        years[year] = line
        year += 2
    else:
        years[year] = line
        year += 1

# for key in years:
#     print(key, ':', years[key])

chosen_year = int(input("Please select a year between 1903 and 2008 (Note: There was no World Series in 1904 and 1994): "))

if chosen_year != 1904 and chosen_year != 1994 and chosen_year > 1902 and chosen_year < 2009:
    for l in years:
        if chosen_year == l:
            team = years[chosen_year]
    for line in name:
        if team == line:
            wins = str(name[line])
    print(team + ': ' + wins)
else:
    print("Incorrect year.")

        
