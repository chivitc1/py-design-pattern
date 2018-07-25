import sys
import re

pattern = sys.argv[1]
source_string = sys.argv[2]
match = re.match(pattern, source_string)

if match:
    template = "'{}' matches pattern '{}'"
else:
    template = "'{}' does not match pattern '{}'"

print(template.format(source_string, pattern))