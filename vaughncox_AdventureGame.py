def makeGame():
    game = {
      "start": ["You just got off the subway, but on the exit escalator is a flaming goat blocking your path", "Look around", "look", "Approach the goat", "approach"], 
      "look": ["You see the empty railway, a vending machine, and of course, the goat.", "Go to the vending machine", "vending", "Drop onto the railway", "railway"], 
      "approach": ["The goat is quite angry, because it's on fire. It lights you on fire. You will not make it to work.", "Start over", "start", "Quit", "quit"], 
      "vending": ["The vending machine serves soda, but it's not plugged in.", "Shake the machine", "shake", "Plug it in", "plug"], 
      "railway": ["You drop onto the railway. It is powered and electrocutes you. You will not make it to work.", "Start over", "start", "Quit", "quit"], 
      "shake": ["You shake the machine. A Pepsi falls out! But also, the machine falls on you. Ouch.", "Start over", "start", "Quit", "quit"], 
      "plug": ["You plug it in, and it works! However, you have no change for a drink.", "Check the change return slot", "change", "Shake the machine", "shake"], 
      "change": ["The change return has some quarters, just enough for a drink! How lucky.", "Buy yourself a drink", "buy", "Throw coins at the goat to distract it", "throw"], 
      "buy": ["The machine dispenses your drink and you pick it up.", "Drink it", "drink", "Approach the goat", "approach2"], 
      "throw": ["The angry flaming goat is not distracted. It charges you. You will not make it to work.", "Start over", "start", "Quit", "quit"], 
      "drink": ["You are still stuck in the subway, but at least you're refreshed. Except now you're stuck here forever.", "Start over", "start", "Quit", "quit"], 
      "approach2": ["The goat is angry, but perplexed at what is in your hand.", "Pour the soda on the goat", "pour", "Offer the goat a drink", "offer"], 
      "pour": ["The flame is out! But the goat is still angry.", "Pet it", "pet", "Let it chew on the can", "chew"], 
      "offer": ["It goes to grab the drink from you, but lights you on fire. Unlucky.", "Start over", "start", "Quit", "quit"], 
      "pet": ["The angry goat does NOT want pet. It knocks you off the escalator.", "Start over", "start", "Quit", "quit"], 
      "chew": ["The goat starts chewing on the can, and you slip past it, up the escalator. Congrats, you made it!", "Start over", "start", "Quit", "quit"], 
    }
    return game

def playNode(game, currentKey):
    currentNode = game[currentKey]
    (description, menu1, node1, menu2, node2) = currentNode
    print(f"""
{description}

    1. {menu1} 
    2. {menu2} 
    """)
    userChoice = input("Which will you do? ")
    if userChoice == "1":
        newKey = node1
    elif userChoice == "2":
        newKey = node2
    else:
        newKey = currentKey
        print("Please choose 1 or 2")
        
    return newKey
def main():
    game = makeGame()
    currentKey = "start"
    
    keepGoing = True
    while keepGoing:
        if currentKey == "quit":
            keepGoing = False
        else:
            currentKey = playNode(game, currentKey)
    
main()