shopping_list = ["mango", "grapes", "apple", "sugar", "corn"]
search = None
for index in range(len(shopping_list)):
    if shopping_list[index] == "apple":
        search = "apple"
        print(f"{search} was gotten at index position {index}")
        break

# improved
if "apple" in shopping_list:
    found_index = shopping_list.index("apple")
    print("apple found at " + str(found_index))