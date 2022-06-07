# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x97 in position 334: invalid start byte
# This happens because 'Jabberwocky.txt' is encoded in 'windows-1252'
# with open('Jabberwocky.txt', encoding='utf-8') as jabber:
#     for line in jabber:
#         print(line.rstrip())

# This is OK as 'Jabberwocky.txt' is encoded in 'windows-1252' and also read in 'windows-1252'
with open('Jabberwocky.txt', encoding='windows-1252') as jabber:
    for line in jabber:
        print(line.rstrip())
