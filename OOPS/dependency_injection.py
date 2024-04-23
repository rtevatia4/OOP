class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")

class NotificationService:
    def __init__(self, email_service):
        self.email_service = email_service

    def send_notification(self, recipient, message):
        self.email_service.send_email(recipient, message)

# Creating instances of EmailService and NotificationService
email_service = EmailService()
notification_service = NotificationService(email_service)

# Using the NotificationService to send a notification
notification_service.send_notification("example@example.com", "Hello from the NotificationService!")