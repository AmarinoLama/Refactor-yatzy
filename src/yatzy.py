from pips import Pips

class Yatzy:
    
    NOPOINTS = 0
    MAXPOINTS = 50

    @staticmethod
    def listRepeted(dices, min):
        return list(filter(lambda x:dices.count(x)>=min,dices))

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
    def yatzy(*dices):
        
        '''
        Code smells:
        - A loop is too long and too deeply nested
        
        Fixes:
        - Simplify the function
        '''
        
        return Yatzy.MAXPOINTS if len(set(dices)) == 1 else Yatzy.NOPOINTS

    @staticmethod
    def ones(*numbers):
        
        ONE = Pips.ONE.value
        
        #
        
        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
        
        return numbers.count(ONE) if numbers.count(ONE) != 0 else Yatzy.NOPOINTS
    

    @staticmethod
    def twos(*numbers):
        
        TWO = Pips.TWO.value
        
        #
        
        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(TWO) * TWO if numbers.count(TWO) != 0 else Yatzy.NOPOINTS
    
    @staticmethod
    def threes(*numbers):
        
        THREE = Pips.THREE.value
        
        #
        
        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(THREE) * THREE if numbers.count(THREE) != 0 else Yatzy.NOPOINTS
    
    @staticmethod
    def fours(*numbers):
        
        FOUR = Pips.FOUR.value
        
        #
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(FOUR) * FOUR if numbers.count(FOUR) != 0 else Yatzy.NOPOINTS

    @staticmethod
    def fives(*numbers):
        
        FIVE = Pips.FIVE.value
        
        #
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(FIVE) * FIVE if numbers.count(FIVE) != 0 else Yatzy.NOPOINTS
    
    @staticmethod
    def sixes(*numbers):
        
        SIX = Pips.SIX.value
        
        #
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(SIX) * SIX if numbers.count(SIX) != 0 else Yatzy.NOPOINTS
    
    @staticmethod
    def score_pair(*dices):
        
        #
        
        TWO = Pips.TWO.value
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        - A parameter list has too many parameters
        
        Fixes:
        - Make the code more readable
        - Build a loop which can accept multiple values
        '''
    
        return TWO * max(Yatzy.listRepeted(dices, TWO)) if Yatzy.listRepeted(dices, TWO) else Yatzy.NOPOINTS

    @staticmethod
    def two_pair(*dices):

        TWO = Pips.TWO.value
        THREE = Pips.THREE.value
        FOUR = Pips.FOUR.value
        
        #
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        - A parameter list has too many parameters
        
        Fixes:
        - Make the code more readable
        - Build a loop which can accept multiple values
        - Simplify the code
        '''

        numNoDuped = list(set(dices))
        pair_counter = []
        for number in numNoDuped:
            if (dices.count(number) == TWO or dices.count(number) == THREE) and len(pair_counter) < TWO:
                pair_counter.append(number)
            elif dices.count(number) >= FOUR:
                return dices.count(number) * FOUR
        return sum(pair_counter) * TWO if len(pair_counter) == TWO else Yatzy.NOPOINTS
    
    @staticmethod
    def four_of_a_kind(*dices):
        
        FOUR = Pips.FOUR.value
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        - A parameter list has too many parameters
        
        Fixes:
        - Make the code more readable
        - Build a loop which can accept multiple values
        '''
        
        dices_sorted = list(sorted(dices, reverse=True))
        for number in dices_sorted:
            if dices.count(number) >= FOUR:
                return number * FOUR
        return Yatzy.NOPOINTS
    

    @staticmethod
    def three_of_a_kind(*dices):
        
        THREE = Pips.THREE.value
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        - A parameter list has too many parameters
        
        Fixes:
        - Make the code more readable
        - Build a loop which can accept multiple values
        '''
        
        dices_sorted = list(sorted(dices, reverse=True))
        for number in dices_sorted:
            if dices.count(number) >= THREE:
                return number * THREE
        return Yatzy.NOPOINTS
    
    @staticmethod
    def smallStraight(*dices):
        
        #
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        - A parameter list has too many parameters
        
        Fixes:
        - Make the code more readable
        - Build a loop which can accept multiple values
        - Simplify the code
        '''
        
        return sum(list(range(1,6))) if sorted(dices) == list(range(1,6)) else Yatzy.NOPOINTS

    @staticmethod
    def largeStraight(*dices):
        
        #
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        - A parameter list has too many parameters
        
        Fixes:
        - Make the code more readable
        - Build a loop which can accept multiple values
        - Simplify the code
        '''
        
        return sum(list(range(2,7))) if sorted(dices) == list(range(2,7)) else Yatzy.NOPOINTS
    

    @staticmethod
    def fullHouse(*dices):
        
        '''
        Code smells:
        - A loop is too long or too deeply nested
        - A parameter list has too many parameters
        
        Fixes:
        - Make the code more readable
        - Build a loop which can accept multiple values
        - Simplify the code
        '''

        noDuplicated = set(dices)
        result = 0
        switch = False
        for number in noDuplicated:
            if dices.count(number) >= 2 and len(noDuplicated) == 2:
                if dices.count(number) == 3:
                    result += number * 3
                    switch = True
                else: 
                    result += number * dices.count(number)
                    
        return result if switch is True else Yatzy.NOPOINTS
    
print(Yatzy.x)