def setup():
    """
    This function will take the player through
    the introduction and explain the rules.
    """
    # Game Welcome
    print("""
-----------------------------------------------------------
-----------------------------------------------------------
Welcome to Python Battleships Adventure
A terminal python game where you VS a computer in battleships
-----------------------------------------------------------
-----------------------------------------------------------
""")
    start = input("""
Would you like to read the instructions? Type 'Yes' or 'No'
""").lower()
    if start == ('yes'):
        print("Instructions")
    elif start == ('no'):
        print("Get ready to play!")
    else:
        print("Invlaid response, restarting terminal")
        setup()
