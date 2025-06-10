class Symbol:
    """
    Symbol class represents a card symbol with a color and icon.
    :color: The color of the symbol, which is either "red" or "black".
    :icon: The icon representing the symbol, which can be one of ["♡", "♢", "♣", "♠"].
    """

    # Attribute to store the color of the symbol.
    color: str = "" 

    # The constructor (__init__) accepts an integer to determine the icon and color.
    def __init__(self, item: int):
        # Initially set color to empty string
        self.color = ""
        
        # List of possible icons (symbols)
        icons = ["♡", "♢", "♣", "♠"]
        
        # Assign the corresponding icon based on the 'item' index (0, 1, 2, or 3)
        self.icon = icons[item]

        # Assign color based on the icon's index (red for first two icons, black for the rest)
        if item < 2:
            self.color = "red"
        else:
            self.color = "black"

    # String representation of the Symbol object, showing color and icon
    def __str__(self):
        return f"{self.color} {self.icon}"


class Card(Symbol):
    """
    Card class represents a card that inherits from the Symbol class.
    :inherits Symbol: Card inherits the color and icon attributes from Symbol class.
    :value: The value of the card, one of ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'].
    """

    # Constructor (__init__) accepts 'icon' and 'item' as arguments.
    def __init__(self, icon, item: int):
        # List of card values (Ace, 2-10, Jack, Queen, King)
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # Call the parent constructor (Symbol) to set color and icon
        super().__init__(icon)
        
        # Assign the card's value based on the 'item' index
        self.value = values[item]

    # String representation of the Card object, showing both icon and value
    def __str__(self):
        # Return a string in the format of "icon value", e.g., "♠ A"
        return f"{self.icon} {self.value}"