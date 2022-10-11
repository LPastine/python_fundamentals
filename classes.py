# A class is like a blueprint for creating objects.
# An object has properties and methods(functions)
# associated with it. Almost everything in Python is an object

class User:
    """User class"""

    def __init__(self, name: str, email: str, age: int):
        """Constructor of Person initializes props"""
        self.name = name
        self.email = email
        self.age = age

    def greeting(self) -> str:
        """Greet the user"""
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self) -> None:
        """Increments age by one"""
        self.age += 1


# Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
janet = User('Janet Williams', 'janet@gmail.com', 27)

# Edit property
brad.age = 38
janet.has_birthday()

# Print prop
print(brad.name)
# Call method
print(janet.greeting())


class Customer(User):
    """Customer inherits User class"""

    def __init__(self, name: str, email: str, age: int, balance: int = 0) -> None:
        """Constructor of Customer initializes props"""
        super().__init__(name, email, age)
        self.balance = balance

    def set_balance(self, balance):
        """Set Customer's balance"""
        self.balance = balance

    def greeting(self) -> str:
        """Greet the user"""
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

# Init customer


john = Customer('John Doe', 'john@gmail.com', 40)

john.set_balance(500)

print(john.greeting())
