class OldCoinStash: 
    def __init__(self, owner): 
        self.owner = owner

        self._riksdaler = 0 
        self._skilling = 0 

    def deposit(self, riksdaler, skilling): 
        if riksdaler < 0 or skilling < 0: 
            raise ValueError(f"You try to deposit {riksdaler} and {skilling}. They have to be positive.")
        self._riksdaler += riksdaler
        self._skilling += skilling

    def withdraw(self, rikstaler, skilling): 
        if rikstaler > self._riksdaler or skilling > self._skilling:
            raise ValueError(f"You can't withdraw more than you have in your stash.")
        
        self._riksdaler -= rikstaler
        self._skilling -= skilling

    def checkBalance(self): 
        return f"Coins in stash: {self._riksdaler} rikstaler, {self._skilling} skilling"
    

    def __repr__(self): 
        return f"OldCoinStash(owner = '{self.owner})"