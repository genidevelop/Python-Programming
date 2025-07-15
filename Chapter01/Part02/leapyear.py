import stdio
import sys

# Checks whether a given year is a leap year
year = int(sys.argv[1])

isLeap = ((year % 4) == 0) and ((year % 100) != 0)
isLeap = isLeap or ((year % 400) == 0)

stdio.writeln(isLeap)