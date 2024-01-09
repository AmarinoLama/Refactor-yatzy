class Yatzy:

    @staticmethod
    def chance(*numbers):
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        
        Fixes:
        - Make a loop which can accept multiple values
        - Delete arguments (d1, d2, ...)
        '''
        
        total = 0
        for number in numbers:
            total += number
        return total

    @staticmethod
    def yatzy(dices):
        
        '''
        Code smells:
        - A loop is too long and too deeply nested
        
        Fixes:
        - Simplify the function
        - Make the code readable and undestandable
        '''
        
        firstDice = dices[0]
        for dice in dices:
            if dice == firstDice:
                continue
            else:
                return 0
        return  50

    @staticmethod
    def ones(*numbers):

        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 1:
                sum += 1
        return sum
    

    @staticmethod
    def twos(*numbers):
        
        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 2:
                sum += 2
        return sum
    
    @staticmethod
    def threes(*numbers):
        
        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 3:
                sum += 3
        return sum
    
    def fours(*numbers):
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 4:
                sum += 4
        return sum

    def fives(*numbers):
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        sum = 0
        for number in numbers:
            if number == 5:
                sum += 5
        return sum
    

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)): 
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def score_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        at = 0
        for at in range(6):
            if (counts[6-at-1] == 2):
                return (6-at)*2
        return 0
    
    @staticmethod
    def two_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6-i-1] >= 2):
                n = n+1
                score += (6-i)
                    
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0