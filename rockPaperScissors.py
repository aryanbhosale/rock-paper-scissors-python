import random

import sys

count = 1

wins = 0

losses = 0

ties = 0

rock = 1

paper = 2

scissors = 3

print('\n\tROCK, PAPER, SCISSORS')

print('\n\t0 Wins, 0 Losses, 0 Ties')

while True :

    num = random.randint(1,3)

    print('\n\n\n\tROUND ',count)

    count+=1

    move = input('\n\tEnter your move : (r)ock (p)aper (s)cissors or (q)uit : ')

    if(move == 'r') :

        print('\n\tROCK versus...')

        if(num == 1) :

            print('\n\tROCK')

            print('\n\tIt is a tie!')

            ties+=1

            print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)
            
        elif(num == 2) :

            print('\n\tPAPER')

            print('\n\tI win!')

            losses+=1

            print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)

        elif(num == 3) :

            print('\n\tSCISSORS')

            print('\n\tYou win!')

            wins+=1

            print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)

    elif(move == 'p') :

        print('\n\tPAPER versus...')

        if(num == 1) :

            print('\n\tROCK')

            print('\n\tYou win!')

            wins+=1

            print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)
            
        elif(num == 2) :

            print('\n\tPAPER')

            print('\n\tIt is a tie!')

            ties+=1

            print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)

        elif(num == 3) :

            print('\n\tSCISSORS')

            print('\n\tI win!')

            losses+=1

            print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)

    elif(move == 's') :

        print('\n\tSCISSORS versus...')

        if(num == 1) :

            print('\n\tROCK')

            print('\n\tI win!')

            losses+=1

            print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)
            
        elif(num == 2) :

            print('\n\tPAPER')

            print('\n\tYou win!')

            wins+=1

            print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)

        elif(num == 3) :

            print('\n\tSCISSORS')

            print('\n\tIt is a tie!')

            ties+=1

            print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)

    elif(move == 'q') :

        print('\n\tYou quit.')

        print('\n\tWINS : ',wins,', LOSSES : ',losses,', TIES : ',ties)

        if(wins>losses) :

            print('\n\tHuman wins.')

        if(wins<losses) :

            print('\n\tToo bad human. AI wins.')

        if(wins==losses) :

            print('\n\tWe are equals human.')

        sys.exit()

            
        
        
        
