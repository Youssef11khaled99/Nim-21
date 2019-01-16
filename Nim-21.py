R=0
while R!="n":
    print("Welcome to Nim 21 game! Take one to three coins per turn!")
    Coins=21
    Limit=[1, 2, 3]
    print("Coins: ", Coins)
    while Coins > 1:
        A=int(input("Player 1's turn: "))
        if A not in Limit:
            print("You can only take from one to three coins.")
            print("Coins: ", Coins)
            continue
        Coins=Coins-A
        while Coins==0 or Coins==-1:
            Coins=Coins+A
            print("You can only take one or two coins.")
            print("Coins: ", Coins)
            A=int(input("Player 1's turn: "))
            Coins=Coins-A
        print("Coins: ", Coins)
        if Coins==1:
            print("Player 2 takes the last coin.")
            print("Coins: 0")
            print("Player 1 wins!")
            break
        B=int(input("Player 2's turn: "))
        if B not in Limit:
            while B not in Limit:
                print("You can only take from one to three coins.")
                print("Coins: ", Coins)
                B=int(input("Player 2's turn: "))
        Coins=Coins-B
        while Coins==0 or Coins==-1:
            Coins=Coins+B
            print("You can only take one or two coins.") 
            print("Coins: ", Coins)
            B=int(input("Player 2's turn: "))
            Coins=Coins-B
        print("Coins: ", Coins)
        if Coins==1:
            print("Player 1 takes the last coin.")
            print("Coins: 0")
            print("Player 2 wins!")
            break
    print("Thanks for playing!")
    R=str(input("Do you want to play again?(y/n) "))
    print('''   ''')
