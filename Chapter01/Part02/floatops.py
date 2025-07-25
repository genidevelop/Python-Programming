import stdio
import sys

# floatops.py illustrates basic operations for manipulate float objects
# The program do not check for error (division by zero)
a = float(sys.argv[1])
b = float(sys.argv[2])

total = a + b
diff = a - b
prod = a * b
quot = a / b
rem = a % b
exp = a ** b

stdio.writeln(str(a) + ' +  ' + str(b) + ' = ' + str(total))
stdio.writeln(str(a) + ' -  ' + str(b) + ' = ' + str(diff))
stdio.writeln(str(a) + ' *  ' + str(b) + ' = ' + str(prod))
stdio.writeln(str(a) + ' /  ' + str(b) + ' = ' + str(quot))
stdio.writeln(str(a) + ' %  ' + str(b) + ' = ' + str(rem))
stdio.writeln(str(a) + ' ** ' + str(b) + ' = ' + str(exp))