def show_help():

    """
    Display the list of avaliable commands and their descriptions.
    """
    print(
          "\nCommands:\n"
        "  help                      -> Show this help message\n"
        "  cancel/back               -> Cancel from current operation\n"
        "  add                       -> Add a new contact\n"
        "  update                    -> Update original contact\n"
        "  view/contacts/list/show   -> View all contacts\n"
        "  search                    -> Search contacts by keyword\n"
        "  remove/delete             -> Remove a contact by keyword\n"
        "  clear                     -> Remove all contacts\n"
        "  exit/quit                 -> Exit the program\n"
    )

def empty_contacts(contacts):
    """
    Check if the contacts dictionary is empty.
    Return True if empty, False otherwise.
    """
    if not contacts:
        print("No contacts here.")
        return True
    return False

def found_contacts(contacts):
    """
    Search for contacts by a keyword and display matching contacts.
    """
    keyword = input("Enter keyword to search contact: ").strip().lower()
    if is_cancel(keyword):
        print("Searching contact cancelled.")
        return {}
    found = {name:phone for name,phone in contacts.items() if keyword in name.lower() or keyword in phone}
    if not found:
        print("No matching contact here.")
        return {}
    
    print("Contacts")
    for i,(name,phone) in enumerate(found.items(),1):
        print(f"{i}. Name: {name} | Phone: {phone}")
    
    return found

def show_contacts(contacts):
    """
    Display all contacts in the dictionary.
    """
    print("Contacts")
    for i,(name,phone) in enumerate(contacts.items(),1):
        print(f"{i}. Name: {name} | Phone: {phone}")
    
    return contacts

def is_cancel(user_input):
    return user_input.strip().lower() in ["cancel","back"]

def add_contacts(contacts):
    """
    Add a new contact to contacts dictionary.
    """
    while True:
        name = input("Name (or type 'back' or 'cancel' to cancel): ").strip().title()
        if is_cancel(name):
            print("Adding contact cancelled.")
            return
        if not name:
            print("Name can't be empty. Please enter name.")
            continue
        if name in contacts:
            print(f"{name} already exists. Choose another name.")
            continue
        break

    while True:
        phone = input("Phone (or type 'back' or 'cancel' to cancel): ").strip()
        if is_cancel(phone):
            print("Adding contact cancelled.")
            return
        if not phone:
            print("Phone number can't be empty. Please enter phone number.")
            continue
        if phone in contacts.values():
            print(f"This phone number already exists. Choose a different phone number.")
            continue
        break

    contacts[name]  = phone
    print("New contact added.")

def view_contacts(contacts):
    """
    Display all contacts in the dictionary.
    """
    if empty_contacts(contacts):
        return
    show_contacts(contacts)

def search_contacts(contacts):
    """
    Search and display contact from contacts by keyword.
    """
    if empty_contacts(contacts):
        return
    found_contacts(contacts)

def update_contacts(contacts):
    """
    Update an existing contact's name and/or phone number by keyword.
    """
    if empty_contacts(contacts):
        return
    
    found = found_contacts(contacts)
    if not found:
        return
    
    old_name = input("Select name to update (or type 'back' or 'cancel' to cancel): ").strip().title()
    if is_cancel(old_name):
        print("Updating contact cancelled.")
        return
    if old_name in found:
        while True:
            new_name = input("Name (or type 'back' or 'cancel' to cancel): ").strip().title()
            if is_cancel(new_name):
                print("Updating contact cancelled.")
                return
            if not new_name:
                new_name = old_name
            if new_name != old_name and new_name in contacts:
                print("Contact name already exists. Please choose another name.")
                continue
            break
        
        while True:
            new_phone = input("Phone (or type 'back' or 'cancel' to cancel): ").strip()
            if is_cancel(new_phone):
                print("Updating contact cancelled.")
                return
            if not new_phone:
                new_phone = contacts[old_name]
            if new_phone != contacts[old_name] and new_phone in contacts.values():
                print(f"This phone number already exists. Choose a different phone number.")
                continue
            break

        new_contacts = {}
        for name,phone in contacts.items():
            if name == old_name:
                new_contacts[new_name] = new_phone
            else:
                new_contacts[name] = phone
        contacts.clear()
        contacts.update(new_contacts)
        print("Contact updated.")
        show_contacts(contacts)
        return


def remove_contacts(contacts):
    """
    Remove contact from contacts by keyword.
    """
    if empty_contacts(contacts):
        return

    found = found_contacts(contacts)
    if not found:
        return
    
    try:
        choice = input("Enter number of contacts to remove (or type 'back' or 'cancel' to cancel): ")
        if is_cancel(choice):
            print("Removing contact cancelled.")
            return
        choice = int(choice)
        if 1 <= choice <= len(found):
            selected_name = list(found.keys())[choice - 1]
            confirm = input("Are you sure to remove this contact? (y/n) (or type 'back' or 'cancel' to cancel): ").strip().lower()
            if is_cancel(confirm):
                print("Removing contact cancelled.")
                return
            if confirm in ["y","yes"]:
                del contacts[selected_name]
                print("Contact removed.")
                show_contacts(contacts)
                return
            else:
                print("Removal cancelled.")
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter valid number.")

def clear_contacts(contacts):
    """
    Clear all contacts in the contacts.
    """
    if empty_contacts(contacts):
        return
    
    confirm = input("Are you sure to clear all contacts? (y/n)(or type 'back' or 'cancel' to cancel): ").strip().lower()
    if is_cancel(confirm):
        print("Clearing contacts cancelled.")
        return
    if confirm in ["y","yes"]:
        contacts.clear()
        print("All contacts cleared.")
    return

def contact_book():

    """
    Main function to start contact book.
    """
    
    contact_list = {}
    view_command = ["view","contacts","list","show"]
    quit_command = ["exit","quit"]
    remove_command = ["remove","delete"]
    
   
    print("Welcome to Contact Book!")
    print("Type 'help' to see available commands.")
   
    while True:

        command = input("> ").strip().lower()

        if command in quit_command:
            break

        elif command == "add":
            add_contacts(contact_list)
            continue

        elif command in view_command:
            view_contacts(contact_list)
            continue

        elif command == "search":
            search_contacts(contact_list)
            continue

        elif command == "update":
            update_contacts(contact_list)
            continue

        elif command in remove_command:
            remove_contacts(contact_list)
            continue

        elif command == "clear":
            clear_contacts(contact_list)
            continue

        elif command == "help":
            show_help()
            continue

        else:
            print("Invalid input. Type 'help' to see valid command.")
            continue


if __name__ == "__main__":
    contact_book()