import math
import stdio
import sys

# Computing the two roots of a quadratic equation using the quadratic formula.
# The program do not check for error (squre root of a negative number)
b = float(sys.argv[1])
c = float(sys.argv[2])

discriminant = b*b - 4.0*c
d = math.sqrt(discriminant)

stdio.writeln((-b + d) / 2.0)
stdio.writeln((-b - d) / 2.0)