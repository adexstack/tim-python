# Raw literals usage
a_string = "this is\na string split\t\tand tabbed"
print(a_string)

raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

# The chr(10) might not work well in windows because it handles carriage return and line feeds differently
b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

# seeing the \f as unicode. Best handled by doubling \\
backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

#even though it's raw, backslash at end has to be escaped
error_string = r"this string ends with \\"
