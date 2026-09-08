import questionary
from auth import ask_username, ask_password, login_user, register_user
from deliveries import create_delivery, get_user_deliveries, update_delivery_status, delete_delivery

def display_main_menu():
    while True:
        ans = questionary.select(
            "\n=== SPACE DELIVERY MANAGER ===\n",
            choices=["Register", "Login", "Exit"]).ask()
        if ans == "Register":
            username = ask_username()
            password = ask_password()
            try:
                register_user(username, password)
                print("Registration successful!")
            except ValueError as e:
                print(e)
        elif ans == "Login":
            username = ask_username()
            password = ask_password()
            try:
                user = login_user(username, password)
                if user:
                    print("Successful login!")
                    while True:
                        ans = questionary.select(
                            f"\nWelcome, {user.username}!\n",
                            choices=["Create delivery", "Show my deliveries", "Update delivery status","Delete delivery", "Logout"]).ask()
                        if ans == "Create delivery":
                            package_name = questionary.text("Enter package name: ").ask()
                            destination = questionary.text("Enter destination:").ask()
                            weight = questionary.text("Enter package weight: ").ask()
                            try:
                                create_delivery(user, package_name, destination, float(weight))
                                print("Added successfully!")
                            except ValueError as e:
                                print(e)
                        elif ans == "Show my deliveries":
                            deliveries = get_user_deliveries(user)
                            if not deliveries:
                                print("You do not have any deliveries.")
                            else:
                                for d in deliveries:
                                    print(
                                        f"\nID: {d.id}\nPackage: {d.package_name}\nDestination: {d.destination}\nWeight: {d.weight}\nStatus: {d.status}")
                                    print("-" * 20)
                        elif ans == "Update delivery status":
                            delivery_id = questionary.text("Enter delivery ID:").ask()
                            new_status = questionary.select(
                                "Choose new status to update",
                                choices=["Waiting", "In Transit", "Delivered", "Cancelled"]).ask()
                            try:
                                res = update_delivery_status(user, int(delivery_id), new_status)
                                if res:
                                    print("Updated successfully.")
                                else:
                                    print("You cannot modify this delivery or it does not exist.")
                            except ValueError:
                                print("Invalid delivery ID.")
                        elif ans == "Delete delivery":
                            delivery_id = questionary.text("Enter delivery ID:").ask()
                            try:
                                res = delete_delivery(user, int(delivery_id))
                                if res:
                                    print("Deleted successfully.")
                                else:
                                    print("You cannot modify this delivery or it does not exist.")
                            except ValueError:
                                print("Invalid delivery ID.")
                        elif ans == "Logout":
                            print("Logged out successfully.")
                            break
                else:
                    print("Login failed. Incorrect username or password.")
            except ValueError as e:
                print(e)
        elif ans == "Exit":
            print("Goodbye!")
            return

if __name__ == "__main__":
    display_main_menu()