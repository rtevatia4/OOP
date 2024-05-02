# Subtypes must be substitutable for their base types.

# Voilation

class Notification:
  def __init__(self, type):
    self.__type = type
  
  def send_text_notification(self):
    print("Sent Text notification")

  def send_email_notification(self):
    print("Sent Email notification")

class TextNotification(Notification):
  def __init__(self, type):
    super().__init__(type)
  
  def send_text_notification(self):
    print("Sent Text Notification")

t = TextNotification("phone")
t.send_email_notification()    # text notifcation is also able to do the email notification, here this voidates the LSP
t.send_text_notification()


# Follows the LSP

class Notification:
  def __init__(self, type):
    self.__type = type

  def send_notification(self):
    print("Sent notification")

class EmailNotification(Notification):
  def __init__(self, type):
    super().__init__(type)

  def send_notification(self):
    print("Sent Email notification")

class TextNotification(Notification):
  def __init__(self, type):
    super().__init__(type)
  
  def send_notification(self):
    print("Sent Text Notification")

email = EmailNotification("email")
text = TextNotification("phone")
email.send_notification()
text.send_notification()