from matchmaking_service.models import Player, Match

class GameState:
    def __init__(self):
        self.players: dict[str, Player] = {}
        self.queue: list[Player] = []
        self.matches: list[Match] = []


    def add_player(self, id: int, username: str, rating: float):
        if username in self.players:
            return False

        self.players[username] = Player(id, username, rating)
        return True


    def enqueue_match_request(self, player: Player):
        if player is None:
            return False

        self.queue.append(player)
        return True


    def add_match(self, match: Match):
        if match is None:
            return False

        self.matches.append(match)
        return True
