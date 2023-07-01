# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line


class Player:
    def __init__(self, name, speed, endurance, accuracy):
        if not (0 <= speed <= 1) or not (0 <= endurance <= 1) or not (0 <= accuracy <= 1):
            raise ValueError("Speed, endurance, and accuracy must be between 0 and 1 (inclusive).")
        
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
    
    def introduce(self):
        return f"Hello everyone, my name is {self.name}."
    
    def strength(self):
        attributes = [('speed', self.speed), ('endurance', self.endurance), ('accuracy', self.accuracy)]
        attributes.sort(key=lambda x: (-x[1], x[0]))  # Sort attributes based on values and priority
        
        max_value = attributes[0][1]
        max_attributes = [(name, value) for name, value in attributes if value == max_value]
        
        return tuple(max_attributes[0])

class Commentator:
    def __init__(self, name):
        self.name = name
    
    def sum_player(self, player):
        return player.speed + player.endurance + player.accuracy
    
    def compare_players(self, player1, player2, attribute):
        attr1 = getattr(player1, attribute)
        attr2 = getattr(player2, attribute)
        
        if attr1 > attr2:
            return player1.name
        elif attr1 < attr2:
            return player2.name
        else:
            strength1 = player1.strength()[1]
            strength2 = player2.strength()[1]
            
            if strength1 > strength2:
                return player1.name
            elif strength1 < strength2:
                return player2.name
            else:
                total_score1 = self.sum_player(player1)
                total_score2 = self.sum_player(player2)
                
                if total_score1 > total_score2:
                    return player1.name
                elif total_score1 < total_score2:
                    return player2.name
                else:
                    return "These two players might as well be twins!"

