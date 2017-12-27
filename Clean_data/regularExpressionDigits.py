# Import the regular expression module
import re

# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result = prog.match('1123-456-7890')
print(bool(result))




# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')
#\d is the pattern required to find digits.
# This should be followed with a + so that the previous element is matched
# one or more times. This ensures that 10 is viewed as one number and not as 1 and 0.

# Print the matches
print(matches)