import string
import sys
movieName=input("Enter  the name of the movie: ")
if(movieName==' '):
	print('Invalid Input!!!')
	exit()
encryptedName=''
print('\n'*100)
movieName=movieName.upper()
wordList=movieName.split()
movieName=' '.join(wordList)
wordList=list(movieName)
lengthList=len(wordList)
for i in range(0,lengthList,1):
    if((wordList[i].isalpha()!=True)and(wordList[i].isdigit()!=True)and(wordList[i]!=' ')):
        print('Invalid Input1!!!')
        exit()
for i in range(0,lengthList,1):
    if wordList[i] in "AEIOU":
        encryptedName+='*'
    elif(wordList[i]==' '):
        encryptedName+='/'
    else:
        encryptedName+='-'
print("Let's begin!!!This is your movie's Hangman Name!")
print(encryptedName)
encryptedList=list(encryptedName)
result=''
for i in range(len(encryptedList)):
    if(encryptedList[i]=='/'):
        result+=' '
    else:
        result+=encryptedList[i]
result=list(result)
i=6
while(i>=0):
    guess=input('Enter your guess: ')
    guess=guess.upper()
    if((len(guess)!=1)or((guess.isalpha()!=True)and(guess.isdigit())!=True)):
        print('Invalid Input!!!Please enter another character')
        i+=1
        continue
    else:
        smallFlag=0
        for j in range(0,lengthList,1):
            if(wordList[j]==guess):
                smallFlag=1
                encryptedList[j]=guess
                result[j]=guess
        if((''.join(result))!=(''.join(wordList))):    
            print(''.join(encryptedList))
        else:
            print("Congratulations!You Won!The movie's name is: ",''.join(result))
            exit()
        if(smallFlag==0):
            if(i==0):
              sys.stdout.write("\033[F")
              print('You Lost!!!')
              exit()
            else:
              i=i-1
              print('Oops!Wrong Answer!You have ',(i+1),' chances left')
              #(wordList[i]=='A')or(wordList[i]=='E')or(wordList[i]=='I')or(wordList[i]=='O')or(wordList[i]=='U')
