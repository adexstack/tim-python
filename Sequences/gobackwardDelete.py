# Improved and optimized deleting
data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# ranging from start at end of list '12' up to 0 and stepping back -1
for index in range(len(data) - 1, - 1, - 1):
    if data[index] < 100 or data[index] > max_valid:
        print(index, data)
        del data[index]
print(data)

print ("-------Using reversed method to achieve the above-------")
data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    #print(index, value) prints value from 0 to 12, I want 12 - 0
    if value < 100 or value > max_valid:
        print(top_index - index, data)
        #subtracting index from top_index 12 to get the desired 12 - 0 and deleting
        del data[top_index - index]
print(data)
