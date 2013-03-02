import re

a = 'This is a@text.com in which we:2 can search11 anything you like Ramon@google.com'

match = re.search('\w+@\w+.\w+', a)
print match.group()

match = re.findall('\w+@\w+.\w+', a)
print match
