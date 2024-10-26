from users.models import Notification
from users.models import Offers


def create_notification(username, notification):
    Notification.objects.create(username=username, notification=notification)


def create_offers(username, offers):
    Offers.objects.create(username=username, offers=offers)
