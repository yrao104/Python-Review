#overriding a method offers a new definition for the method in our sublcass
#an overriden method is one that has a different definition from its parent class
#example below calls constructor from the superclass
    #super().__init__(basin, nozzle)

#Admin class overrides method edit_message, allowing Admin to override any messages form User class
class Message:
    def __init__(self, sender, reciepient, text):
        self.sender = sender
        self.recipient = reciepient
        self.text = text

class User:
    def __init__(self, username):
        self.username = username

    def edit_message(self, message, new_text):
        if(message.sender == self.username):
            message,text = new_text

class Admin(User):
    def edit_message(self, message, new_text):
        message.ntext = new_text