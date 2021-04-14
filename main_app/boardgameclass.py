class Boardgame:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, genre, players, playtime):
        self.name = name
        self.genre = genre
        self.players = players
        self.playtime = playtime


boardgames = [
    Boardgame('Dominion', 'Deck Building', '2-4', '30 min'),
    Boardgame('Flash Point: Fire Rescue', 'Adventure', '2-6', '45 min'),
    Boardgame('Chaos in the Old World', 'Strategy', '3-4', '60-120 min')
]
