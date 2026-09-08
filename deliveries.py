from models import Delivery, User

def create_delivery(user: User, package_name, destination, weight):
    if not package_name:
        raise ValueError("Package name cannot be empty.")
    if not destination:
        raise ValueError("Destination cannot be empty.")
    if weight <= 0:
        raise ValueError("Weight must be greater than 0.")
    delivery = Delivery.create(owner=user,package_name=package_name,destination=destination,weight=weight,status="Waiting")
    return delivery


def get_user_deliveries(user):
    return list(user.deliveries)


def update_delivery_status(user: User, delivery_id, new_status):
    allowed_statuses = ["Waiting", "In Transit", "Delivered", "Cancelled"]
    if new_status not in allowed_statuses:
        raise ValueError("Invalid delivery status.")
    delivery = Delivery.get_or_none(Delivery.id == delivery_id)
    if delivery is None or delivery.owner != user:
        return False
    delivery.status = new_status
    delivery.save()
    return True


def delete_delivery(user: User, delivery_id):
    delivery = Delivery.get_or_none(Delivery.id == delivery_id)
    if delivery is None or delivery.owner != user:
        return False
    delivery.delete_instance()
    return True