'''
Question 3 :
Print the first ArmStrong number in the range of 1042000 to 702648265 and exit the loop as soon you
encounter the first armstrong number
Use While Loop
Output:-
The first armstrong number is:-
'''


Starting_Number = 1042000
Ending_Number = 702648265
arm = [ ]

for num in range(Starting_Number, Ending_Number + 1):

   order = len(str(num))

   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       arm.append(num)
       print('The first armstrong number is:-',arm[0])
       break