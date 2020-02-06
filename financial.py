import sys
class Financial:
    def __init__(self, param):
        self.atm_digit = param

    def getSize(self):
        return len(self.atm_digit)

    def isValidSize(self):
        if self.getSize() >= 13 and self.getSize() <= 16:
            # print('Card has a valid size')
            return True
        else:
            print('Card is not within the range of 13 to 16')
            sys.exit()

    def sumOfDoubleEvenPlace(self):
        if self.isValidSize():
            number = []
            for num in self.atm_digit:
                number.append(int(num))
            number.reverse()
            sumEvenNo = 0
            for num in number[1::2]:
                numSquare = num * 2
                if numSquare > 9:
                    newSum =((numSquare%10) + (numSquare//10))
                    sumEvenNo += newSum
                else:
                    sumEvenNo += numSquare
            return sumEvenNo

    def sumOfOddPlaces(self):
        if self.isValidSize():
            number = []
            for num in self.atm_digit:
                number.append(int(num))
            number.reverse()

            sumOddNo = 0
            
            for num in number[0::2]:
                sumOddNo+= num

            return sumOddNo

    def getDigit(self):
        totalSum = self.sumOfDoubleEvenPlace() + self.sumOfOddPlaces()
        return totalSum

    def isValidCard(self):
        if self.getDigit() % 10 != 0 :
            print('ATM card is invalid.')
            sys.exit()
        print('ATM card is valid.')
        

        return True

    def prefixMatched(self):
        if self.isValidCard():
            if self.atm_digit[0] == '4':
                print('This is a Visa card')
            elif self.atm_digit[0] == '5':
                print('This is a Mastercard card')
            elif self.atm_digit[0] == '6':
                print('This is a Discover card atm')
            elif self.atm_digit[0] == '3' and self.atm_digit[1] == '7':
                print('This is a mastercard atm')

    def start(self):
        self.prefixMatched()

    

