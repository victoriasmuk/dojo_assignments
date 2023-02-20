class Player:
    def __init__(self,data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']

    @classmethod
    def add_players(cls,data):
        player_objects = []
        for item in data:
            player_objects.append(cls(item))
        return player_objects
    

kevin = {
    "name": "Kevin Durant", 
	"age":34, 
    "position": "small forward", 
	"team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
	"age":24, 
    "position": "small forward", 
	"team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
	"age":32,
    "position": "Point Guard", 
	"team": "Brooklyn Nets"
}
# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

