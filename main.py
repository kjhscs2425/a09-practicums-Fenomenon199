def choose_practicum(): 
    response = input   ( "Can you sign up for practicum?")
    if response == "Costumes" or response== "scenery" or response== "lighting" or response== "sound":
        return response
    else: 
        return choose_practicum()

def signup():
    name=input("whats your name") 
    choice= choose_practicum() 
    print(f"Congratulations {name}, you are signed up for {choice}!")

signup()