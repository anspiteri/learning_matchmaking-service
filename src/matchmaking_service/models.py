class Player:
    def __init__(self, id: int, username: str, rating: float):
        self.id = id
        self.username = username
        self.rating = rating

class Match:
    def __init__(self, players: list[Player]):
        self.players = players
        self.winner = None
