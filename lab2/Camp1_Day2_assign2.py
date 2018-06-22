from random import randint
if __name__ == '__main__':
    GuessNumber=randint(1, 10)
    #print("GuessNumber=",GuessNumber)
    correct=False
    while(correct==False):
        InputNumber = input("Guess the number: ")
        if(int(InputNumber) == int(GuessNumber)):
            print("Correct! ")
            correct=True
        else:
            print("Wrong, try again! ")
