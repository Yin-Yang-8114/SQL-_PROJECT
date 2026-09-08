import questionary
from models import Delivery
from auth import ask_username, ask_password, login_user, register_user
from deliveries import *
def display_main_menu():

    while True:
        ans = questionary.select("\n=== SPACE DELIVERY MANAGER ===\n", choices=["Register", "Login", "Exit"]).ask()
        if ans == "Register":
            username = ask_username()
            password = ask_password()
            register_user(username, password)

        elif ans == "Login":
            username = ask_username()
            password = ask_password()
            
            user = login_user(username, password)

            if  user:
                print("Seccessful login!")

                ans = questionary.select("Welcome, {user.username}!\n", choices=["Create delivery", "Show my deliveries", "Update delivery status", "Delete delivery", "Logout"]).ask()

                if ans == "Create delivery":
                    package_name = questionary.text("Enter package name: ").ask()
                    destination = questionary.text("Enter destination:").ask()
                    weight = questionary.text("Enter package weight: ").ask()
                    create_delivery(user, package_name, destination, weight)
                    print("Added successfully")
                    
                elif ans == "Show my deliveries":

                    print(get_user_deliveries(user))
                    

                elif ans =="Update delivery status":
                    delivery_id = questionary.text("Enter delivery ID:").ask()
                    new_status = questionary.select("Choose new status to update", choices=["Waiting", "In Transit", "Delivered", "Cancelled"]).ask()
                    delivery = Delivery.select().where(Delivery.id == delivery_id)
                    if delivery.id == user.id:
                        update_delivery_status(user, delivery_id, new_status) 
                    else:
                        print("You must be delivery's owner to update!")

                elif ans == "Delete delivery":
                    delivery_id = questionary.text("Enter delivery ID:").ask()
                    delivery = Delivery.select().where(Delivery.id == delivery_id)
                    if delivery.id == user.id:
                        delete_delivery(user, delivery_id)
                    else:
                        print("You must be delivery's owner to delete!")

                elif ans == "Logout":
                    user = None

        elif ans == "Exit":
            return
            
display_main_menu()
