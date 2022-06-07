# jabber = open('Jabberwocky.txt', 'r')
# for line in jabber:
#    # print(line, end='') # removes the newline (\n)
#     #print(line.strip()) # removes all blank lines at start and end
#     print(line.lstrip()) # will strip all blanks at the start of the line
# jabber.close()

# with open('Jabberwocky.txt') as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines() # would print lines as list
# print(lines)
# print(lines[-1:])
# print(lines[::-1])
# for line in reversed(lines):
#     print(line, end='') # do something in reverse order
#
# print('*' * 80)
# with open('Jabberwocky.txt') as jabber:
#     text = jabber.read()
# print(text)
# for char in reversed(text):
#     print(char, end='')

# with open('Jabberwocky.txt') as jabber:
#     while True:
#         line = jabber.readline()
#         print(line.rstrip())
#         if "jubjub" in line.casefold():
#             break

with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if "jubjub" in line.casefold():
            break
