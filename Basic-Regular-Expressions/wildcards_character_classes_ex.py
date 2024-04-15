import re

# prints the first space it finds
print(re.search(r"[^a-zA-Z]", "This is a sentense with spaces."))

print(re.search(r"[^a-zA-Z ]", "This is a sentense with spaces."))