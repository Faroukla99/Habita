from tracker import HabitTracker
from analytics import *
import os

# ---------------------------------------------------

# Clean CLI function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ---------------------------------------------------

habit_manager = HabitTracker() # Habits manager
habit_manager.load_from_json('data.json') # New user habits data

# ---------------------------------------------------

# Welcome screen
logo = """ 

 /$$   /$$           /$$       /$$   /$$              
| $$  | $$          | $$      |__/  | $$              
| $$  | $$  /$$$$$$ | $$$$$$$  /$$ /$$$$$$    /$$$$$$ 
| $$$$$$$$ |____  $$| $$__  $$| $$|_  $$_/   |____  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$  | $$      /$$$$$$$
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$ /$$ /$$__  $$
| $$  | $$|  $$$$$$$| $$$$$$$/| $$  |  $$$$/|  $$$$$$$
|__/  |__/ \_______/|_______/ |__/   \___/   \_______/
"""

# ---------------------------------------------------

habit_frequency_list = ["daily", "weekly", "monthly", "yearly"] # Frequency checklist
habit_frequency_all_list = ["daily", "weekly", "monthly", "yearly", "all"] # Show habits frequency checklist
menu_options = ["1- Create a Habit", "2- Check a Habit", "3- Show current habits", "4- Delete a Habit", "5- Habit Lab", "6- Help", "7- Exit"] # App menu options

# ---------------------------------------------------

# App main loop
app_running = True
while app_running:
    
    # Welcome screen message
    print(logo,
    "\nWelcome to Habita app\nMake your habits part of you now!\n")

    # Loops till user make right 
    right_option = True
    while right_option:

            # App menu options
            for option in menu_options:
                print(option)

            # ValueError handling
            try:
                user_option = int(input("\nChoose an option: "))


                if user_option not in range(1, 8):
                    clear()
                    print("You have to type one of the numebrs in the screen\n")

                else:
                    right_option = False
                    # ---------------------------------------------------
                    # Create a Habit
                    if user_option == 1:
                        clear()

                        # sub menu loop
                        user_interaction = True
                        while user_interaction:

                            # List of all existing habit names
                            list_of_habits = [habit.name for habit in habit_manager.habits]

                            # sub menu loop
                            print("Welcome to your habit creation section: \n")
                            habit_creation = True
                            while habit_creation:
                                habit_name = input("Name the habit you want to create: ").capitalize()

                                # Duplicate check
                                if habit_name in list_of_habits:
                                    clear()
                                    print(f"the {habit_name} habit already exist. Make a new one: \n")
                                else:
                                    habit_creation = False

                            habit_description = input("\nGive your habit a description: ")

                            # sub menu loop
                            habit_creation = True
                            while habit_creation:
                                habit_frequency = input("\n- Daily\n- Weekly\n- Monthly\n- Yearly"
                                                        "\n\nHow frequently you want to do your habit? ").lower()
                    
                                # Typo check to prevent retrieving erorr
                                if habit_frequency not in habit_frequency_list:
                                    clear()
                                    print("You have to choose either: Daily, Weekly, Monthly or Yearly")
                                else:
                                    habit_manager.add_habit(habit_name, habit_description, habit_frequency)
                                    habit_creation = False

                            clear()
                            print(f"Congratulations! Your new {habit_name.capitalize()} habit is created now, GOOD LUCK.\n")

                            # sub menu loop - Back to main menu or create new habit
                            option = True
                            while option:

                                # ValueError Handling
                                try:
                                    user_option = int(input("1- Create another habit\n2- Go Back\n\nChoose your option: "))

                                    if user_option == 2:
                                        habit_manager.save_to_json("data.json")
                                        clear()
                                        option = False
                                        user_interaction = False
                                    elif user_option not in range(1,3):
                                        clear()
                                        print("This option is not on the list, choose 1 or 2\n")
                                    else:
                                        clear()
                                        option = False

                                except ValueError:
                                    clear()
                                    print("You have to type one of the numebrs in the screen\n")

                    # ---------------------------------------------------

                    # Check a Habit
                    elif user_option == 2:
                        clear()

                        # sub menu loop
                        user_interaction = True
                        while user_interaction:

                            # sub menu loop
                            habit_frequency_checking = True
                            while habit_frequency_checking:
                                print("Type frequency:\n")
                                habit_frequency = input("- Daily\n- Weekly\n- Monthly\n- Yearly"
                                                        "\n\nChoose which habits you want to check?: ").lower()
                                
                                # Typo check to prevent retrieving erorr
                                if habit_frequency not in habit_frequency_list:
                                    clear()
                                    print("You have to choose either: Daily, Weekly, Monthly or Yearly\n")
                                else:
                                    habit_frequency_checking = False

                            habits_by_frequency = get_all_habits_by_frequency(habit_manager.habits, habit_frequency)

                            clear()
                            print(f"Here are your {habit_frequency.capitalize()} habits:\n")
                            for habit in habits_by_frequency:
                                print(f"- {habit.name}")

                            # Empty list - no habits
                            if len([habit.name for habit in habits_by_frequency]) == 0:
                                clear()
                                print(f"There are no {habit_frequency} habits to show, go back and create your first!")
                            else:        
                                # sub menu loop
                                habit_checking = True
                                while habit_checking:

                                    # User type the habit they want to complete
                                    habit_to_complete = input("\nChoose the habit you want to check today: ").capitalize()

                                    if habit_to_complete in [habit.name for habit in habits_by_frequency]:
                                        habit_manager.complete_habit(habit_to_complete)
                                        clear()
                                        print(f"Your {habit_to_complete} habit is completed, you are one step closer to success! Keep going.\n")
                                        habit_checking = False

                                    # Typo error message
                                    else:
                                        clear()
                                        print("You either mistyped the habit or entered a habit that doesn't exist, Try again\n")
                                        for habit in habits_by_frequency:
                                            print(f"- {habit.name}")
                                        
                            
                            # sub menu loop - Back to main menu or check other habit
                            option = True
                            while option:

                                # ValueError handling
                                try:
                                    user_option = int(input("1- Check another habit\n2- Go Back\n\nChoose your option: "))
                                    print("\n")

                                    if user_option == 2:
                                        habit_manager.save_to_json("data.json")
                                        clear()
                                        user_interaction = False
                                        option = False

                                    elif user_option not in range(1, 3):
                                        clear()
                                        print("This option is not on the list, choose 1 or 2\n")

                                    else:
                                        option = False
                                        clear()

                                except ValueError:
                                    clear()
                                    print("You have to type one of the numebrs in the screen\n")

                    # ---------------------------------------------------

                    # Show current habits
                    elif user_option == 3:
                        clear()

                        # sub menu loop
                        user_interaction = True
                        while user_interaction:

                            # sub menu loop
                            habit_frequency_checking = True
                            while habit_frequency_checking:
                                    print("Type frequency:\n")
                                    habit_frequency = input("- Daily\n- Weekly\n- Monthly\n- Yearly\n\n- All"
                                                            "\n\nChoose which habits you want to see?: ").lower()
                                    
                                    # Typo check to prevent retrieving erorr
                                    if habit_frequency not in habit_frequency_all_list:
                                        clear()
                                        print("You have to choose either: Daily, Weekly, Monthly, Yearly or All\n")
                                    else:
                                        habit_frequency_checking = False

                            # Show all habits
                            if habit_frequency == "all":
                                # Empty list - no habits
                                if len(get_all_habits(habit_manager.habits)) == 0:
                                    clear()
                                    print("There are no habits to show, go back and create your first!")
                                else: 
                                    clear()
                                    print("Here are all your habits:")
                                    for habit in get_all_habits(habit_manager.habits):
                                        print(f"\n{habit.name} - {habit.frequency.capitalize()}"
                                            f"\n- Description: {habit.description}")
                            
                            # Show habits only by selected frequency
                            else:
                                # Empty list - no habits
                                if len(get_all_habits_by_frequency(habit_manager.habits, habit_frequency)) == 0:
                                    clear()
                                    print(f"There are no {habit_frequency.capitalize()} habits to show, go back and create your first!\n")
                                else:
                                    clear()
                                    print(f"Here are your {habit_frequency.capitalize()} habits:")
                                    for habit in get_all_habits_by_frequency(habit_manager.habits, habit_frequency):
                                        print(f"\n{habit.name} \n- Description: {habit.description}")

                            # sub menu loop - Back to main menu or show other habits
                            option = True
                            while option:

                                # ValueError handling
                                try:
                                    print("\n---------------------------")
                                    user_choice = int(input("\n1- Show other habits"
                                                            "\n2- Return to main menu"
                                                            "\n\n Choose your option: "))
                                    if user_choice not in range(1, 3):
                                        clear()
                                        print("You have to choose 1 or 2")
                                    elif user_choice == 1:
                                        option = False
                                        clear()
                                    else:
                                        option = False
                                        user_interaction = False
                                        clear()
                                except ValueError:
                                    clear()
                                    print("You have to type a number")
                                            
                    # ---------------------------------------------------

                    # Delete a Habit
                    elif user_option == 4:
                        clear()

                        # sub menu option
                        user_interaction = True
                        while user_interaction:

                            # sub menu loop    
                            habit_frequency_checking = True
                            while habit_frequency_checking:
                                print("Type frequency:\n")
                                habit_frequency = input("- Daily\n- Weekly\n- Monthly\n- Yearly"
                                                        "\n\nChoose which habits you want to delete?: ").lower()
                                
                                # Typo check to prevent retrieving erorr
                                if habit_frequency not in habit_frequency_list:
                                    clear()
                                    print("You have to choose either: Daily, Weekly, Monthly or Yearly\n")
                                else:
                                    habit_frequency_checking = False

                            habits_by_frequency = get_all_habits_by_frequency(habit_manager.habits, habit_frequency)

                            clear()
                            print(f"List of your {habit_frequency.capitalize()} habits: \n")
                            for habit in habits_by_frequency:
                                print(f"- {habit.name}")

                            # Empty list - no habits
                            if len([habit.name for habit in habits_by_frequency]) == 0:
                                clear()
                                print(f"There are no {habit_frequency} habits to delete.\n")

                            else:         
                                # sub menu loop
                                habit_process = True
                                while habit_process:
                                    selected_habit = input("\nType the habit you want to delete: ").capitalize()

                                    # Typo checking
                                    if selected_habit in [habit.name for habit in habits_by_frequency]:
                                        clear()

                                        double_check = True
                                        while double_check:
                                            double_check_decision = input(f"Are you sure you want to delete the {selected_habit} habit? Type yes or no: ").lower()

                                            if double_check_decision == "yes":
                                                clear()
                                                habit_manager.delete_habit(selected_habit)
                                                print(f"Your {selected_habit} habit is deleted.\n")
                                                habit_process = False
                                                double_check = False

                                            elif double_check_decision == "no":
                                                clear()
                                                habit_process = False
                                                double_check = False
                                                #  user_interaction = False
                                            else:
                                                clear()
                                                print("You have to type yes or no\n")

                                    else:
                                        clear()
                                        print("You either mistyped the habit or entered a habit that doesn't exist, Try again\n")
                                        for habit in habits_by_frequency:
                                            print(f"- {habit.name}")

                            # sub menu loop - Back to main menu or delete other habit
                            option = True
                            while option:

                                # ValueError handling
                                try:
                                    user_option = int(input("1- Delete another habit\n2- Go Back\n\nChoose your option: "))
                                    print("\n")
                                    if user_option == 2:
                                        habit_manager.save_to_json("data.json")
                                        clear()
                                        option = False
                                        user_interaction = False
                                    elif user_option not in range(1, 3):
                                        clear()
                                        print("This option is not on the list, choose 1 or 2")
                                    else:
                                        option = False
                                        clear()
                                except ValueError:
                                    clear()
                                    print("You have to type one of the numebrs in the screen")

                    # ---------------------------------------------------

                    # Habit Lab
                    elif user_option == 5:
                        clear()

                        # sub menu loop
                        user_interaction = True
                        while user_interaction:
                            print("Welcome to your Habit Lab!\n")

                            # sub menu loop
                            option = True
                            while option:
                                
                                # ValueError handling
                                try:
                                    
                                    submenu_options = int(input("1- Show my longest streak\n2- Show my struggling habit\n\nChoose an option: "))
                                    
                                    # Checks if user typed other number than the presented ones
                                    if submenu_options not in range(1, 3):
                                        clear()
                                        print("You have to choose 1 or 2\n")
                                    else:
                                        option = False
                                except ValueError:
                                    clear()
                                    print("You have to type a number\n")

                            # Show my longest streak
                            if submenu_options == 1:
                                clear()

                                # sub menu loop
                                habit_frequency_checking = True
                                while habit_frequency_checking:
                                    print("Type frequency:\n")
                                    habit_frequency = input("- Daily\n- Weekly\n- Monthly\n- Yearly"
                                                            "\n\nChoose which habits you want to analyze?: ").lower()
                                    
                                    # Typo check to prevent retrieving erorr
                                    if habit_frequency not in habit_frequency_list:
                                        clear()
                                        print("You have to choose either: Daily, Weekly, Monthly or Yearly\n")
                                    else:
                                        habit_frequency_checking = False


                                longest_streak_habit = get_longest_streak_habits(habit_manager.habits, habit_frequency)

                                # Empty tuple - no habits
                                if len(longest_streak_habit) == 0:
                                    clear()
                                    print("There are no habits to analyze")
                                else:
                                    clear()
                                    for habit, streak in longest_streak_habit[0].items():
                                        print(f"- Longest streak of {habit} habit: {streak} streaks\n")

                                    for habit, streak in longest_streak_habit[1].items():
                                        print(f"📈 '{habit} habit' have highest numbers of streak with {streak} streaks comparing to other habits.") 

                            # Show my longest break
                            elif submenu_options == 2:
                                clear()

                                # sub menu loop
                                habit_frequency_checking = True
                                while habit_frequency_checking:
                                    print("Type frequency:\n")
                                    habit_frequency = input("- Daily\n- Weekly\n- Monthly\n- Yearly"
                                                            "\n\nChoose which habits you want to analyze?: ").lower()
                                    
                                    # Typo check to prevent retrieving erorr
                                    if habit_frequency not in habit_frequency_list:
                                        clear()
                                        print("You have to choose either: Daily, Weekly, Monthly or Yearly\n")
                                    else:
                                        habit_frequency_checking = False

                                longest_break_habit = get_longest_break_habits(habit_manager.habits, habit_frequency)

                                # Empty tuple - no habits
                                if len(longest_break_habit) == 0:
                                    clear()
                                    print("\nThere are no habits to analyze")
                                else:
                                    clear()
                                    for habit, miss in longest_break_habit[0].items():
                                        print(f"- Longest breaks of {habit} habit: {miss} breaks\n")

                                    for habit, miss in longest_break_habit[1].items():
                                        print(f"📉 '{habit} habit' have highest number of breaks with {miss} breaks comparing to other habits.") 

                            # sub menu loop - Back to main menu or delete other habit
                            second_option = True
                            while second_option:

                                # ValueError handling
                                try:
                                    print("\n---------------------------")
                                    user_option = int(input("\n1- Analyze other habits\n2- Go Back\n\nChoose your option: "))
                                    if user_option == 2:
                                        clear()
                                        second_option = False
                                        user_interaction = False
                                    elif type(user_option) == int and user_option != 1:
                                            clear()
                                            print("This option is not on the list, choose 1 or 2")
                                    else:
                                        clear()
                                        second_option = False
                                except ValueError:
                                        clear()
                                        print("You have to type one of the numebrs in the screen")
                        
                    # ---------------------------------------------------

                    # Help
                    elif user_option == 6:
                        clear()
                        print("Welcome to your Help section, your guide through the app\n")

                        # sub menu loop
                        user_interaction = True
                        while user_interaction:
                            

                            # ValueError handling
                            try:

                                choices = int(input("1- How to use the app\n2- How to make a successful habit\n3- Go Back\n\nChoose your option: "))

                                if choices not in range(1, 4):
                                    clear()
                                    print("You have to choose 1, 2 or 3\n")

                                # User guide
                                elif choices == 1:
                                    clear()
                                    print("--- Habita User Guide ---")
                                    print("Welcome to our Habita, an app that will help you build habits and make them for good.")
                                    
                                    print("\n**1. Create a Habit**")
                                    print("   - This is your first step! Give your new habit a name (like 'Reading')")
                                    print("     and a description plus a frequency (like 'Daily' or 'monthy').")

                                    print("\n**2. Check a Habit**")
                                    print("   - When you complete a habit, use this option to 'check it off'")
                                    print("     for the day and build your streak.")

                                    print("\n**3. Show current habits**")
                                    print("   - See a list of all your active habits. You can choose to see")
                                    print("     'all' habits or filter them by frequency (e.g., show 'Daily' habits only).")

                                    print("\n**4. Delete a Habit**")
                                    print("   - If you want to remove a habit, this is the place. You'll")
                                    print("     choose a frequency first, then type the name of the habit to delete.")

                                    print("\n**5. Habit Lab**")
                                    print("   - This is your analytics center. Go here to see your 'report card.'")
                                    print("   - 'Show my longest streak' shows you the number of streaks for all your habits and give you the winning habit or habits.")
                                    print("   - 'Show my struggling habit' shows you the number of breaks for all your habits and finds the habit or habits that you've had the most struggles with.")

                                    print("\n**6. Help**")
                                    print("   - This where you are now :)")

                                    print("\n**7. Exit**")
                                    print("   - This will close the application but all your habits and changes will be saved.")
                                    
                                    input("\nPress Enter to return to the Help menu...")
                                    clear()

                                # Habit advices
                                elif choices == 2:
                                    clear()
                                    print("--- Practical Tips for Building Habits ---")
                                    print("'Building habits is a 'short race' ,not a marathon. Stick enough till it becomes automatic'")

                                    print("\n**1. Start Small and Simple**")
                                    print("   - Choose a habit that is easy to achieve. Simplicity helps")
                                    print("     you stay consistent and motivated. This is your 'lead domino' .")
                                    
                                    print("\n**2. Use Habit Stacking**")
                                    print("   - Do your new habit right after something you already do,")
                                    print("     like brushing your teeth or your first coffee.")

                                    print("\n**3. Use Triggers and Reminders**")
                                    print("   - Attach the new habit to an existing routine. Visual cues")
                                    print("     like sticky notes or mobile reminders can increase your chances of success.")

                                    print("\n**4. Track Progress and Stay Accountable**")
                                    print("   - Monitor your habit streaks right here in the app!")
                                    print("     Your Habit Lab will help you.")

                                    print("\n**5. Reward Your Efforts**")
                                    print("   - Celebrate your small wins. This builds positive momentum.")

                                    print("\nAnd Lastly, We wish you all the good luck and We trust in YOU!")

                                    input("\nPress Enter to return to the Help menu...")
                                    clear()

                                else:
                                    clear()
                                    user_interaction = False
                                    
                            except ValueError:
                                clear()
                                print("You have to type a number\n")

                    # ---------------------------------------------------

                    # Exit
                    elif user_option == 7:
                        clear()
                        app_running = False

            except ValueError:
                clear()
                print("You have to type a number (e.g. 1 2 3)\n")