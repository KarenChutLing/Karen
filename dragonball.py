print ("""
   
        
  _____  _____            _____  ____  _   _   ____          _      _      
 |  __ \|  __ \     /\   / ____|/ __ \| \ | | |  _ \   /\   | |    | |     
 | |  | | |__) |   /  \ | |  __| |  | |  \| | | |_) | /  \  | |    | |     
 | |  | |  _  /   / /\ \| | |_ | |  | | . ` | |  _ < / /\ \ | |    | |     
 | |__| | | \ \  / ____ \ |__| | |__| | |\  | | |_) / ____ \| |____| |____ 
 |_____/|_|  \_\/_/    \_\_____|\____/|_| \_| |____/_/    \_\______|______|
                                                                           
                                                                           
                                                             
    """)
print("Welcome to Dragon Ball")
 
player_name = input('What is your name, adventurer\n') 
 
health = 100 
damage = 20 
 
print('\nwelcome, ' + player_name + ' !you have ' + str(health) + ' health and can do damage ' + str(damage))  
print (' You came acress a dragon !! what will you do ?? ')
print ('1, Fight')
print ('2, Run ')

choice = int(input('Enter either 1 or 2: ')) 

if choice == 1: 
    print("You attack the dragon and do " + str(damage) + ' damage') 
    print('the dragon back off, spit some acid and does 10 damage') 
    health -= (10*5)
    print('Your current health is ' + str(health)) 
elif choice== 2: 
    print('You run away from the dragon') 
    print('live today for tomorrow') 
    print ('Dragon manage to throw rocks at you deals with twice the damage you inflict')
    health -= (10*2)
    print ( 'Your current health is ' + str (health))

else: 
    print('\nInvalid choice, the dragon get to eat you alive!!!') 
print("Thanks for playing!")

