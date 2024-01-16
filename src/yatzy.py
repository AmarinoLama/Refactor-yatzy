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
    def yatzy(*dices):
        
        '''
        Code smells:
        - A loop is too long and too deeply nested
        
        Fixes:
        - Simplify the function
        '''
        
        return 50 if len(set(dices)) == 1 else 0

    @staticmethod
    def ones(*numbers):

        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
        
        return numbers.count(1) if numbers.count(1) != 0 else 0
    

    @staticmethod
    def twos(*numbers):
        
        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(2) * 2 if numbers.count(2) != 0 else 0
    
    @staticmethod
    def threes(*numbers):
        
        '''
        Code smells:
        - Code is duplicated
        
        Fixes:
        - Make the code readable and undestandable
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(3) * 3 if numbers.count(3) != 0 else 0
    
    def fours(*numbers):
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(4) * 4 if numbers.count(4) != 0 else 0

    def fives(*numbers):
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(5) * 5 if numbers.count(5) != 0 else 0
    

    def sixes(*numbers):
        
        '''
        Code smells:
        - A routine uses more features of another class than of its own class
        
        Fixes:
        - Unify the class to make it static
        - Delete self argument
        - Build a loop which can accept multiple values
        '''
    
        return numbers.count(6) * 6 if numbers.count(6) != 0 else 0
    
    @staticmethod
    def score_pair(*dices):
        
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
            if dices.count(number) >= 2:
                return number*2
        return 0

    @staticmethod
    def two_pair(*dices):

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
            if (dices.count(number) == 2 or dices.count(number) == 3) and len(pair_counter) < 2:
                pair_counter.append(number)
            elif dices.count(number) >= 4:
                return dices.count(number) * 4
        return sum(pair_counter) * 2 if len(pair_counter) == 2 else 0
    
    @staticmethod
    def four_of_a_kind(*dices):
        
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
            if dices.count(number) >= 4:
                return number*4
        return 0
    

    @staticmethod
    def three_of_a_kind(*dices):
        
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
            if dices.count(number) >= 3:
                return number*3
        return 0
    

    @staticmethod
    def smallStraight(*dices):
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        - A parameter list has too many parameters
        
        Fixes:
        - Make the code more readable
        - Build a loop which can accept multiple values
        - Simplify the code
        '''
        
        dices_sorted = sorted(dices)
        
        if dices_sorted == [1,2,3,4,5]:
            return 15
        else:
            return 0


    @staticmethod
    def largeStraight(*dices):
        
        '''
        Code smells:
        - A chain of routines passes tramp data
        - A parameter list has too many parameters
        
        Fixes:
        - Make the code more readable
        - Build a loop which can accept multiple values
        - Simplify the code
        '''
        
        dices_sorted = sorted(dices)
        
        if dices_sorted == [2,3,4,5,6]:
            return 20
        else:
            return 0
    

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
                    
        return result if switch is True else 0