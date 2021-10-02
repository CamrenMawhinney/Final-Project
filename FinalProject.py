#Camren Mawhinney
#Final Project
#Sept 2021

#intialize item prices
pricem = {'Peperoni': 0.39,'Sausage': 0.65, 'Pineapple': 0.23, 'Chicken': 0.35, 'Mushroom': 0.68}

#define classes 
def ptopping1():
    print('\tPeperoni \t$0.35')
    print('\nPricing:\n\tChicken \t$0.30')
    print('\tMushroom  \t$0.65')
    print('\tSausage \t$0.60')
    print('\tPineapple \t$0.21')
    print('\tTotal:\t\t${:4.2f}'.format(total) + '\n')
 
def ptopping2():
    print('\tLarge 16" \t$7.75')
    print('\tMedium 12" \t$5.50')
    print('\nPricing:\n\tSmall 8" \t$4.10')
    print('\tCustom calculated by diameter of pizza.\tEach inch is $0.52\n')

#iterate sequence with for loop 
for word in 'Welcome to Camren\'s Pizza'.split():
    print(f'{word.capitalize():=^65}')
print("\n")


#Allow for user to check on their cart
print('During anytime while ordering, enter "Pricing" to show the pricing\n')
print('of toppings and the complete cost of your order so far.\n')
ordering = True
order = list()
order = []
total = 0
 
#test condition with while loop 
while ordering:
    size = input('What size of pizza are you in the mood for, large, medium, small, or custom?')
    if size.upper()[0] == 'S':
        print('\n\tSmall pizza selected.')
        order.append('"Small" pizza')
        total = total + 4
        print('\nYou have to pick three toppings.')
        num2 = 1
        while num2 != 4:
            print('\nPlease select your topping.')
            #if, elif, else statements for user experience
            topping1 = input('\nChicken, Sausage, Peperoni, Pineapple, Mushroom:').title()
            if topping1[0] == 'C':
                total = total + pricem['Chicken']
                order.append('Chicken')
                num2 = num2 + 1
                print('\n\tChicken topping chosen.')
            elif topping1[0] == 'S':
                total = total + pricem['Sausage']
                order.append('Sausage')
                num2 = num2 + 1
                print('\n\tSausage topping chosen.')
            elif topping1.upper()[1] == 'E':
                total = total + pricem['Peperoni']
                order.append('Peperoni')
                num2 = num2 + 1
                print('\n\tPeperoni topping chosen.')
            elif topping1.upper()[1] == 'I':
                total = total + pricem['Pineapple']
                order.append('Pineapple')
                num2 = num2 + 1
                print('\n\tPineapple topping chosen.')
            elif topping1[0] == 'M':
                total = total + pricem['Mushroom']
                order.append('Mushroom')
                num2 = num2 + 1
                print('\n\tMushroom topping chosen.')
            elif topping1.upper()[1] == 'R':
                ptopping1()
            else:
                print('Error!')
        print('\nDone ordering')
        print('You have chosen a ' + order[0] + ' with\nthe following toppings: ' + order[1] + ', ' + order[2] + ' and ' + order[3] + '.')
        tot2 = total * 1.060
        tot1 = total * 0.06
        print('Your total is: ${:4.2f}'.format(total) + ' with ${:4.2f}'.format(tot1) + ' tax, equal to ${:4.2f}'.format(tot2))
        print('Thank you for your order.')
       
 
  #initialize sizes of pizza      
    elif size.upper()[0] == 'M':
        order.append('Medium Pizza')
        print('\n\tMedium size pizza chosen.')
        total = total + 5.75
        print('\nYou must select three toppings.')
        num1 = 1
        while num1 != 4:
            print('\nPlease pick first topping.')
            topping1 = input('\nChicken, Peperoni, Sausage, Mushroom, Pineapple:').title()
            if topping1[0] == 'C':
                total = total + pricem['Chicken']
                order.append('Chicken')
                num1 = num1 + 1
                print('\n\tChicken topping chosen.')                            
            elif topping1[0] == 'S':
                total = total + pricem['Sausage']
                order.append('Sausage')
                num1 = num1 + 1
                print('\n\tSausage topping chosen.')                
            elif topping1.upper()[1] == 'E':
                total = total + pricem['Peperoni']
                order.append('Peperoni')
                num1 = num1 + 1
                print('\n\tPeperoni topping chosen.')                
            elif topping1.upper()[1] == 'I':
                total = total + pricem['Pineapple']
                order.append('Pineapple')
                num1 = num1 + 1
                print('\n\tPineapple topping chosen.')                
            elif topping1[0] == 'M':
                total = total + pricem['Mushroom']
                order.append('Mushroom')
                num1 = num1 + 1
                print('\n\tMushroom topping chosen.')                
            elif topping1.upper()[1] == 'R':
                ptopping1()
            else:
                print('Error!')
        print('\nfinished ordering')
        print('You have selected a ' + order[0] + ' with\nthe following toppings: ' + order[1] + ', ' + order[2] + ' and ' + order[3] + '.')
        tot2 = total * 1.060
        tot1 = total * 0.06
        print('Your total is: ${:4.2f}'.format(total) + ' with ${:4.2f}'.format(tot1) + ' tax, equal to ${:4.2f}'.format(tot2))
        print('Thank you your order is appreciated.')
     
 
 #initialize pizza toppings
    elif size.upper()[0] == 'L':
        order.append('Large Pizza')
        print('\n\tLarge pizza selected.')
        total = total + 7.50
        print('\nYou may pick three toppings.')
        num = 1
        while num != 4:
            print('\nPlease select a topping.')
            topping1 = input('\nChicken, Sausage, Peperoni, Pineapple, Mushroom:').title()
            if topping1[0] == 'C':
                total = total + pricem['Chicken']
                order.append('Chicken')
                num = num + 1
                print('\n\tChicken topping selected.')                            
            elif topping1[0] == 'S':
                total = total + pricem['Sausage']
                order.append('Sausage')
                num = num + 1
                print('\n\tSausage topping selected.')                
            elif topping1.upper()[1] == 'E':
                total = total + pricem['Peperoni']
                order.append('Peperoni')
                num = num + 1
                print('\n\tPeperoni topping selected.')                
            elif topping1.upper()[1] == 'I':
                total = total + pricem['Pineapple']
                order.append('Pineapple')
                num = num + 1
                print('\n\tPineapple topping selected.')                
            elif topping1[0] == 'M':
                total = total + pricem['Mushroom']
                order.append('Mushroom')
                num = num + 1
                print('\n\tMushroom topping selected.') 
            elif topping1.upper()[1] == 'R':
                ptopping1()
            else:
                print('Error!')
        print('\nDone ordering')
        print('You selected a ' + order[0] + ' with\nthe following toppings: ' + order[1] + ', ' + order[2] + ' and ' + order[3] + '.')
        tot2 = total * 1.060
        tot1 = total * 0.06
        print('Your total is: ${:4.2f}'.format(total) + ' with ${:4.2f}'.format(tot1) + ' tax, equal to ${:4.2f}'.format(tot2))
        print('Thank you for your order.')
 
         
  #Allow user to select their desired size of pizza   
    elif size.upper()[0] == 'C':
        print('\n\tCustom size selected.')
        num1 = 1
        while num1 != 2:
            psize = int(input('\nWhat size (inches) would you like the diameter of your pizza to be?'))
            if psize > 50:
                print('\nPlease select less than or a 50" pizza.')
            elif psize < 3:
                print('\nPlease select more than or a 3" pizza') 
            elif psize <= 50 and psize >= 3:
                num1 = num1 + 1
        order.append('' + str(psize)[0:4] + '" Custom pizza')
        print('\n' + str(psize) + '" pizza selected.')
        psize = psize * 0.52
        total = total + psize
        print('\nYou may pick three toppings.')
        num = 1
    #Allow user to selct their desired toppings for their pizza
        while num != 4:
            print('\nPlease select a topping.')
            topping1 = input('\nChicken, Sausage, Peperoni, Pineapple, Mushroom:').title()
            if topping1[0] == 'C':
                total = total + pricem['Chicken']
                order.append('Chicken')
                num = num + 1
                print('\n\tChicken topping selected.')                            
            elif topping1[0] == 'S':
                total = total + pricem['Sausage']
                order.append('Sausage')
                num = num + 1
                print('\n\tSausage topping selected.')                
            elif topping1.upper()[1] == 'E':
                total = total + pricem['Peperoni']
                order.append('Peperoni')
                num = num + 1
                print('\n\tPeperoni topping selected.')                
            elif topping1.upper()[1] == 'I':
                total = total + pricem['Pineapple']
                order.append('Pineapple')
                num = num + 1
                print('\n\tPineapple topping selected.')                
            elif topping1[0] == 'M':
                total = total + pricem['Mushroom']
                order.append('Mushroom')
                num = num + 1
                print('\n\tMushroom topping selected.') 
            elif topping1.upper()[1] == 'R':
                ptopping1()
            else:
                print('Error!')
        print('\nDone ordering')
        print('You selected a ' + order[0] + ' with\nthe following toppings: ' + order[1] + ', ' + order[2] + ' and ' + order[3] + '.')
        tot2 = total * 1.060
        tot1 = total * 0.06
        print('Your total is: ${:4.2f}'.format(total) + ' with ${:4.2f}'.format(tot1) + ' tax, equal to ${:4.2f}'.format(tot2))
        print('Thank you for your order.\n')
 
 
     
    elif size.upper()[0] == 'P':
        ptopping2()
         
    else:
        print('Sorry, unexpected error. Please try again.')
 
    cont = input('Would you like to order another pizza?')
    if cont.upper()[0] == 'Y':
        total = 0
        del order[0:4]
    elif cont.upper()[0] == 'N':
        print('\nThank you!')
        break
    else:
        print('\nYo no entender, lo sentimos, salir de. A intentarlo mas tarde.')
        break
