# Global Variable to hold tasks in the to do list
task_list = []

# Function to display a welcome message and start the application
def init_welcome_message():
    print(f'Welcome to the To Do List Application.')
    # Call the menu_options function right away to let the user interact
    menu_options()

# Function to display the main menu and handle user input
def menu_options():
     # Exception handling input that is not the right value
     try:
          # create a correct input list to compare with the use input
          correct_input = ['a', 'b', 'c', 'd', 'e']
          # get the user selection and convert it to a string data type
          user_choice = str(input('''\nWhat would you like to do?
          \rA. Add A Task
          \rB. View All Tasks
          \rC. Delete A Task
          \rD. Delete All Tasks
          \rE. Quit\n'''))

          # Convert user choice to lower case for consistent processing
          user_choice = user_choice.lower();
          # if statement to match user input with correct function or raise an error if selection not in list 
          if (user_choice not in correct_input):
               raise ValueError("Please enter a valid selection. (A, B, C, D, or E)")
          elif (user_choice == 'a'):
               add_task()
          elif (user_choice == 'b'):
               view_tasks()
          elif (user_choice == 'c'):
               delete_task()
          elif (user_choice == 'd'):
               delete_all()
          else: quit_application() # if nothing else evaluates to true, quit program
     # handle the error and show the menu again
     except ValueError:
          print("Please select a letter not a number.")
          menu_options()

# define a function to add a task to the to do list
def add_task():
      task = input('Enter a task\n') #prompt user to enter a task
      task_list.append(task) # append the task to the list

      #loop to allow thte user to add more tasks
      isActive = True
      while isActive:
        question = input('Would you like to enter another task? (Yes or No)')
        if (question.title() == 'Yes'):
             task = input('Enter a task\n')
             task = task_list.append(task)
        elif (question.title() == "No"):
             isActive = False
             view_tasks() # display the updated task list
        else: print("Please enter either yes or no.")
      
# Function to dislplay all tasks in the to-do list
def view_tasks():
     if not task_list: # first check to see if the list is empty
          add_tasks = input('''You have no To Do\'s in your To Do List Yet.\nWould you like to add some? (Yes or No)\n''')
          if (add_tasks.title() != "Yes" and add_tasks.title() != "No"):
               answer = input('Please enter yes or no.')
               if (answer.title() != "Yes" and answer.title() != "No"):
                    print("You need to answer either yes or no.")
                    menu_options()
               elif (answer.title() == "No"):
                    menu_options()
               else:
                    add_task()

          if (add_tasks.title() == 'Yes'):
               add_task()
          elif (add_tasks.title() == 'No'):
               menu_options()
          else: 
               menu_options()
     else:
          print(f'Here is your To Do List\n') # display list
          for index, task in enumerate(task_list): #enumerate for index and value
               print(f'{index+1}: {task}')
          menu_options()

# Function to delete a specific task from the to-do list
def delete_task():
     try:
          if not task_list: # check if the list is empty
               print('There are no tasks in the list to delete.')
               menu_options()
               return
          #show the tasks in the list 
          print(f'Here is your To Do List currently:\n')
          for index, task in enumerate(task_list):
               print(f'{index+1}: {task}')

          # prompt the user to select a task to delete
          del_task = int(input('What task would you like to delete?\nEnter the number associated with the task.'))
          index = del_task - 1

          if (index < 0 or index >= len(task_list)): #validate the index
               print("Please enter a valid number within the list.")
               delete_task()
               return
          # remove the selected task and confirm it with the user
          deleted_task = task_list.pop(index)
          print(f'You have successfully deleted: [{deleted_task}]..')
          view_tasks() #display the updated list
          
     except ValueError: # handle invalid input
          print('That is not a valid number. Let\'s look at the main menu.')
          menu_options()

# Function to delete all tasks from the to do list
def delete_all():
     delete_list = input('Are you sure you want to delete your entire to do list? (Yes or No)\n')
     if (delete_list.title() != "Yes" and delete_list.title() != "No"):
               answer = input('Please enter yes or no.')
               if (answer.title() != "Yes" and answer.title() != "No"):
                    print("You need to answer either yes or no.")
                    menu_options()
               else:
                    menu_options()
     elif (delete_list.title() == "Yes"):
          task_list.clear() # clear the entire list
          print('You have just deleted your entire to do list.')
          menu_options()
     else:
          menu_options()

# function to quit the application
def quit_application():
     print('Until next time! Have a great day!')
     exit() # exit the program

# Start the program
init_welcome_message()