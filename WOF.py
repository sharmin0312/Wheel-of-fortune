import random
import test
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    def __init__(self,name):
        self.name=name
        self.prizeMoney=0
        self.prizes=[]
    def addMoney(self,amt):
        self.prizeMoney +=amt
        
    def goBankrupt(self):
        self.prizeMoney=0
        
    def addPrize(self,prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney) 
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        user_inp = input("{} has ${}\nCategory: {}\nPhrase: {}\nGuessed: {}\n\n\nGuess a letter, phrase, or type 'exit' or 'pass':".format(self.name,self.prizeMoney,self.category,self.obscuredPhrase,self.guessed))
        
    # Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES='ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self,name,difficulty):
        WOFPlayer.__init__(self,name)
        self.difficulty=difficulty
    def smartCoinFlip(self):
        rnd_num = random.randint(1, 10)
        if rnd_num > self.difficulty:
            return True
        else:
            return False
    def getPossibleLetters(self,guessed):
        possible_letters = []
        for char in LETTERS:
            if char not in guessed:
                if (char in VOWELS and self.prizeMoney > VOWEL_COST) or (char not in VOWELS):
                    possible_letters.append(char) 
        return possible_letters
        
    def getMove(self,category, obscuredPhrase, guessed):
        gu = self.getPossibleLetters(guessed)
        if gu ==[]:
            return 'pass'
        scf = self.smartCoinFlip
        if scf == True:
            return SORTED_FREQUENCIES[0]
        else:
            return random.choice(gu)