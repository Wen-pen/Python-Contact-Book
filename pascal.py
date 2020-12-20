class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def list(self):
        print(
           f"Name: {self.name},\n"
           f"Email: {self.email},\n"
           f"Phone Number: {self.phone}"
        )
