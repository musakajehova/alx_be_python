def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            print("\n")
            listadd = input("What would you like to add to the list: ")
            shopping_list.append(listadd)
        elif choice == '2':
            # Prompt for and remove an item
            print("\n")
            delete = input("What element would you like to remove? : ")
            if delete in shopping_list:
                shopping_list.remove(delete)
            else :
                print("Item was not found in the list.")
        elif choice == '3':
            # Display the shopping list
            print("\n")
            for i in shopping_list:
                print(f"{i}")
        elif choice == '4':
            print("\n")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()