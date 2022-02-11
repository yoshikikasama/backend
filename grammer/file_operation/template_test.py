import string

# s = """\
# Hi $name.

# $contents

# Have a good day
# """
with open('template.txt') as f:
    t = string.Template(f.read())
# t = string.Template(s)
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)