def towerBreakers(n, m):
    # Write your code here
    
    # if the number of towers is even or the heights are 1, player 2 wins
    
    if n % 2 == 0 or m == 1 :
        return 2
    
    else:
        return 1

        '''
        explanation by Vic65
    There are only 3 cases:
    1. when m=1, the tower heights are all minimum already, player 1 has no moves, so the winner is player 2 in this case. 
    2. When the number of towers is an even number, player 2 can follow the same move as player 1, and the winner is always player 2.
    3. when the number of towers is odd, player 1 takes control, so the winner is always player 1.
        '''
