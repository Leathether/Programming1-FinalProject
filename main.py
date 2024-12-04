import time
import random

# Dice functions
def d20():
    return random.randint(1, 20)

def d6():
    return random.randint(1, 6)

# Helper function to ask questions
def ask(question, choices=None):
    """
    A function to ask a question and return the answer.
    """
    while True:
        print(question)
        if choices:
            print("Choices: " + ", ".join(choices))
        answer = input("> ").strip().lower()
        if choices is None or answer in choices:
            return answer
        print("Invalid choice, please try again.")

# Main game function
def mad_libs_game():
    COLORS = ["red", "blue", "green"]  # Constants for trap wire colors
    player_hp = 100  # Starting HP for the player

    print("Welcome to You: The Legendary Tale of Rescue and Risk!")
    print("This is a long, intricate game full of twists and turns. Choose wisely, as the fate of the Legendary Fighter, the biggest hero of the land, depends on YOU!")
    time.sleep(2)
    print("The Legendary Fighter set out to destroy the Powerful Warrior one day and has since been missing. Your job is to find them and help take down the Powerful Warrior!")

    legendary_fighter = input("Enter the name of the Legendary Fighter, the hero of the land: ")
    powerful_warrior = input("Enter the name of the Powerful Warrior, the enemy of the land: ")

    print(f"Remember your mission: Rescue {legendary_fighter}, who is the only one capable of defeating {powerful_warrior}.")
    time.sleep(2)

    # Intro--Ending one
    while True:
        path = ask("You stand at the edge of a dark, looming forest. Will you take the 'left' path towards the forest or the 'right' path leading to the hills? \nIf you're scared, you can also turn around and go 'home'.", ["left", "right", "home"])
        if path == "left":
            print("You venture into the dark forest. The trees whisper and the path grows narrow.")
            break
        elif path == "right":
            print("You take the right path, but soon find a treacherous cliffside blocking your way. You head back to go another way.")
            continue
        elif path == "home":
            print("You turn around and go home, leaving this epic quest to a braver soul. \nTHE END!")
            print("This window will close in 20 seconds")
            time.sleep(20)
            return

    # The dark forest
    while True:
        action = ask("A mysterious figure approaches. Will you 'talk' to them or 'attack' them?", ["talk", "attack"])
        if action == "talk":
            time.sleep(1)
            print(f"The figure reveals themselves to be an ally who knows the location of {legendary_fighter}. They offer to guide you.")
            break
        elif action == "attack":
            time.sleep(1)
            print("The figure swiftly defends themselves and leaves you disoriented. You get the feeling this figure is much more powerful than you, you are unsure if you can defet them. \nYou get back on your feet.")
            continue

    # Finding the Legendary Fighter
    print(f"You finally reach the hidden lair where {legendary_fighter} is being held.")
    time.sleep(2)
    while True:
        trap = ask(f"To rescue {legendary_fighter}, you must disarm a trap. Choose a wire to cut: 'red', 'blue', or 'green'.", COLORS)

        # Use dice roll to determine correct wire
        roll = d6() % 3
        roll_color = COLORS[roll]

        if trap == roll_color:
            print(f"You cut the {trap} wire. The trap was disabled successfully!")
            break
        else:
            player_hp -= 10
            print(f"You cut the {trap} wire. The trap explodes!")
            print(f"You take damage! Your HP is now: {player_hp}")
            if player_hp <= 0:
                print("The explosion was fatal. Game over!")
                return
            print("You wake up and must try again.")
            continue

    print(f"{legendary_fighter} is free! They thank you for rescuing them and agree to join you in defeating {powerful_warrior}.")
    time.sleep(2)

    # The journey to face the powerful warrior
    print(f"Now, you and {legendary_fighter} must journey to {powerful_warrior}'s fortress.")
    while True:
        mode_of_travel = ask("Will you travel by 'horse', 'foot', or 'boat'?", ["horse", "foot", "boat"])
        if mode_of_travel == "horse":
            time.sleep(1)
            print("You and your companion travel quickly by horse, covering great distance.")
            time.sleep(1)
            break
        elif mode_of_travel == "foot":
            time.sleep(1)
            print("Traveling by foot is exhausting and takes longer than expected. You lose some supplies and have to return for more. \nYou start to think maybe another option would be better.")
            continue
        elif mode_of_travel == "boat":
            time.sleep(1)
            print("The boat ride is smooth, but river bandits attack! You fend them off but lose time. \nYou start to think another option would be better.")
            continue

    # Reaching the fortress
    print(f"You finally reach {powerful_warrior}'s fortress. The walls are high, and guards are everywhere.")
    while True:
        entrance = ask("Do you try to 'sneak' through a small opening or 'fight' the guards?", ["sneak", "fight"])
        if entrance == "sneak":
            time.sleep(1)
            print("You manage to sneak in unnoticed, but it was a close call.")
            break
        elif entrance == "fight":
            time.sleep(1)
            print(f"The guards are too strong! You and {legendary_fighter} barely escape and need to try a different strategy.")
            continue

    # Final battle
    print(f"Inside the fortress, you find {powerful_warrior}. It's time for the final showdown.")
    while True:
        strategy = ask(f"Do you want {legendary_fighter} to attack first, or do you want to use a 'surprise attack'?", ["attack", "surprise", "talk"])
        if strategy == "attack":
            while True:
                time.sleep(1)
                print(f"{legendary_fighter} attempts to attack {powerful_warrior}!")
                roll = d20()
                print(f"You roll a d20 and get: {roll}")
                if roll >= 11:
                    print(f"The attack is successful! {legendary_fighter} defeats {powerful_warrior} after a fierce battle!")
                    break
                else:
                    time.sleep(1)
                    print("The attack misses!")
                    player_hp -= 20
                    print(f"The enemy strikes back! Your HP is now: {player_hp}")
                    if player_hp <= 0:
                        print("You have been defeated. Game over!")
                        print("This window will close in 20 seconds.")
                        time.sleep(20)
                        return
                    continue
            break
        elif strategy == "surprise":
            while True:
                time.sleep(1)
                print(f"You attempt a surprise attack on {powerful_warrior}!")
                roll = d20()
                print(f"You roll a d20 and get: {roll}")
                if roll >= 11:
                    print(f"The surprise attack works! {legendary_fighter} follows up, and together you defeat {powerful_warrior}!")
                    break
                else:
                    time.sleep(1)
                    print("The surprise attack fails!")
                    player_hp -= 20
                    print(f"The enemy notices you and strikes back! Your HP is now: {player_hp}")
                    if player_hp <= 0:
                        print("You have been defeated. Game over!")
                        print("This window will close in 20 seconds.")
                        time.sleep(20)
                        return
                    continue
            break
        elif strategy == "talk":
            time.sleep(1)
            print(f"It turns out that {powerful_warrior} is not the actual Powerful Warrior! After a long talk, you decide to team up to form a powerful team called the Destroyers.\nThe Destroyers run off into the sunset in search of the Powerful Warrior. \nTHE TRUE END")
            print("This window will close in 20 seconds")
            time.sleep(20)
            return

    # Conclusion
    print(f"Congratulations! You and {legendary_fighter} have defeated {powerful_warrior} and brought peace to the land.")
    time.sleep(2)
    print("Thanks for playing You: The Legendary Tale of Rescue and Risk!\nTHE END")
    print("This window will close in 20 seconds")
    time.sleep(20)

# Start the game
mad_libs_game()
