
favoriteNum=66
count=0

while True:

   try:
       count+=1;
       guess=int(input('Enter your guess: '))

   except:

       print ('Error! please enter only integers')

   else:

       if guess == favoriteNum:
           print("You guess correct")

           break

       elif guess>favoriteNum:

            print ('Try a smaller number.')

       elif guess<favoriteNum:

           print ('Try a larger number')

print("you finally got it in ", count," tries" )






