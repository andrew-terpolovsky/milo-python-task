import re
import datetime
import itertools

# Read single line from file input.txt which should be placed in root folder.
f = open("input.txt", "r")
input_str = f.read().strip()
f.close()

# Generate validation message and initial variables
illegal = "{0} is illegal".format(input_str)
available_dates = []
days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Check if date string is valid with regular expression
p = re.compile("^(?P<n1>\d{1,4})/(?P<n2>\d{1,4})/(?P<n3>\d{1,4})$")
s = p.search(input_str)
if not s:
    print(illegal)
    exit()

# Extract integers separated by "/" from string and sort in asc order
future_date = [int(s.group('n1')), int(s.group('n2')), int(s.group('n3'))]
future_date.sort()

# Check if integers are in range(0, 3000)
if future_date[0] < 0 or future_date[0] > 2999:
    print(illegal)
    exit()

# Check all possible dates with provided integers.
# Exclude illegal (day,month,year) pairs
for i in itertools.permutations(future_date):
    if 0 < i[2] <= 31 and 0 < i[1] <= 12 and (0 <= i[0] < 100 or 2000 <= i[0] <= 2999):
        day = i[2]
        month = i[1]
        year = i[0] if i[0] >= 2000 else 2000 + i[0]
        leap = 1 if year % 4 == 0 else 0
        if leap and year % 100 == 0:
            leap = 1 if year % 400 == 0 else 0
        if day <= (days_in_month[month] + leap):
            available_dates.append((year, month, day))

# Check if no legal dates in list
if not len(available_dates):
    print(illegal)
    exit()

# Print earliest legal date in format "yyyy-mm-dd"
available_dates.sort()
print(datetime.date(*available_dates[0]).strftime("%Y-%m-%d"))
