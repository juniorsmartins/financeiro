class Client:

    def __init__(self, firstName="", lastName="", yearOfBirth=0):
        self.firstName = firstName
        self.lastName = lastName
        self.yearOfBirth = yearOfBirth

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.yearOfBirth}"


# Primeiro Client
client1 = Client("Anne", "Frank", 1932)
print(client1)


