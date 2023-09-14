#MCS 260 Spring 2022 Project 4
#Joseph Kang 
#Declaration: I, Joseph Kang, am the author of this code, which was developed in accordance with the rules in the course syllabus
import random 
import sys


array_row_length = 15 #the rows of the grid created from arrays
array_column_length = 15 #the columns of the grid created from arrays (15 x 15)
turn_num = 1 
level_num = 1  
enemy_list = [] 
health = 1 #health is set at 1 so it's a oneshot system
enemies = 5 #will start with 5 enemies

#----------------------------------Array Creation---------------------------------
array1 = [] #creates the arrays necessary to create the grid 
for row in range(array_row_length):
  column_list = []
  for column in range(array_column_length):
    if column == 0 and row == 0:
      column_list.append(" YOU ") #starting and ending place "YOU" is your character at the top left and "END" is the place for the next level at the bottom right
    elif column == 14 and row == 14: 
      column_list.append(" END ")
    else: 
      column_list.append("     ")
  array1.append(column_list)


def printarray(array):
  """Print the array visually"""
  print("=======================================================================================================================================")
  for row in array: #prints the visual grid
    print(row)
  print("=======================================================================================================================================\n\n")

#----------------------------------Spawn Enemies----------------------------------
def spawn_enemy(enemies):
  """Will spawn the enemies randomly throughout the grid"""
  for i in range(1, enemies + 1):
    if i < 10:
      enemy = "EMI" + " " + str(i)
    else:
      enemy = "EMI" + str(i)
    row = random.randint(0, 14)
    col = random.randint(0, 14)
    #while statement below makes it so enemies can't spawn on one another, can't spawn on the starting point, and can't block the player's first move
    while ((col == 0 and row == 0) or (col == 14 and row == 14)) or ((col == 0 and row == 2) or (col == 2 and row == 0)) or (str(row) + ' ' + str(col)) in enemy_list:
      row = random.randint(0, 14)
      col = random.randint(0, 14)
    array1[row][col] = enemy
    enemy_list.append(str(row) + ' ' + str(col)) #adds enemy position to list of enemy positions, to make sure enemies can't spawn on one another
  return array1

#------------------------------------Interaction----------------------------------
def interaction(): 
  """The interaction between YOU and EMI"""
  for row in array1: 
    if "YOUEMI" in row: #if"YOUEMI" is existing in any of the rows, then it will return true and end the game as seen from the coded part of the game
      return True
  return False #else return false

#----------------------------------Enemy Movement---------------------------------
def find_current_enemy_row(enemy_num):
  """Function to find the row of an enemy, based on its number"""
  for row in range(len(array1)):
    if ("EMI" + enemy_num) in array1[row]:
      current_row = row 
      return current_row

def find_current_enemy_col(enemy_num):
  """Function to find the column of an enemy, based on its numberfunction to find the column of an enemy, based on its number"""
  for row in range(len(array1)):
    if ("EMI" + enemy_num) in array1[row]:
      current_col = array1[row].index("EMI" + enemy_num) 
      return current_col

  
def enemy_movement(enemy_row, enemy_col):
  """Moves one enemy one space in a direction parameterized by the code below"""
  #uses other functions to find the current position of the player
  current_row = int(find_current_row())
  current_col = int(find_current_col())

  #enemy moves in x-direction 
  x_or_y = random.randint(1, 2)
  if enemy_col < 14 and enemy_col > 0 and enemy_row < 14 and enemy_row > 0:
    if x_or_y == 1:
      #the following conditionals check for nearby enemies
      if "EMI" in array1[enemy_row][enemy_col + 1] and "EMI" in array1[enemy_row][enemy_col - 1]:
        x_or_y = 0
      elif "EMI" in array1[enemy_row][enemy_col + 1]:
        array1[enemy_row][enemy_col] = "     "
        if " YOU " in array1[enemy_row][enemy_col - 1]:
          array1[enemy_row][enemy_col - 1] = "YOUEMI" #this "YOUEMI" statment is for when the player collides with an enemy, and signifies the player's death
        else:
          array1[enemy_row][enemy_col - 1] = "EMI" + enemy_num
      elif "EMI" in array1[enemy_row][enemy_col - 1]:
        array1[enemy_row][enemy_col] = "     "
        if " YOU " in array1[enemy_row][enemy_col + 1]:
          array1[enemy_row][enemy_col + 1] = "YOUEMI"
        else:
          array1[enemy_row][enemy_col + 1] = "EMI" + enemy_num
      #the following conditional occurs if there are no enemies nearby
      else:
        #the program first checks where the player is in relation to the enemy, then moves the enemy toward the player in the x-direction
        if enemy_col < current_col:
          array1[enemy_row][enemy_col] = "     "
          if " YOU " in array1[enemy_row][enemy_col + 1]:
            array1[enemy_row][enemy_col + 1] = "YOUEMI"
          else:
            array1[enemy_row][enemy_col + 1] = "EMI" + enemy_num
        else:
          array1[enemy_row][enemy_col] = "     "
          if " YOU " in array1[enemy_row][enemy_col - 1]:
            array1[enemy_row][enemy_col - 1] = "YOUEMI"
          else:
            array1[enemy_row][enemy_col - 1] = "EMI" + enemy_num


    #enemy moves in y-direction
    elif x_or_y == 2:
      #the following conditionals check for nearby enemies
      if "EMI" in array1[enemy_row + 1][enemy_col] and "EMI" in array1[enemy_row - 1][enemy_col]:
        x_or_y = 0
      elif "EMI" in array1[enemy_row + 1][enemy_col]:
        array1[enemy_row][enemy_col] = "     "
        if " YOU " in array1[enemy_row - 1][enemy_col]:
          array1[enemy_row - 1][enemy_col] = "YOUEMI"
        else:
          array1[enemy_row - 1][enemy_col] = "EMI" + enemy_num
      elif "EMI" in array1[enemy_row - 1][enemy_col]:
        array1[enemy_row][enemy_col] = "     "
        if " YOU " in array1[enemy_row + 1][enemy_col]:
          array1[enemy_row + 1][enemy_col] = "YOUEMI"
        else:
          array1[enemy_row + 1][enemy_col] = "EMI" + enemy_num
      #the following conditional occurs if there are no enemies nearby    
      else:
        #the program first checks where the player is in relation to the enemy, then moves the enemy toward the player in the y-direction
        if enemy_row < current_row:
          array1[enemy_row][enemy_col] = "     "
          if " YOU " in array1[enemy_row + 1][enemy_col]:
            array1[enemy_row + 1][enemy_col] = "YOUEMI"
          else:
            array1[enemy_row + 1][enemy_col] = "EMI" + enemy_num
        else:
          array1[enemy_row][enemy_col] = "     "
          if " YOU " in array1[enemy_row - 1][enemy_col]:
            array1[enemy_row - 1][enemy_col] = "YOUEMI"
          else:
            array1[enemy_row - 1][enemy_col] = "EMI" + enemy_num

            
  #the following conditionals occur when the enemy in question is on the outer edge of the array. "YOUEMI" is still checked for each instance
  elif enemy_col == 14: #far right edge, move left
    array1[enemy_row][enemy_col] = "     "
    if " YOU " in array1[enemy_row][enemy_col - 1]:
      array1[enemy_row][enemy_col - 1] = "YOUEMI"
    elif "EMI" not in array1[enemy_row][enemy_col - 1]:
      array1[enemy_row][enemy_col - 1] = "EMI" + enemy_num
    else:
      array1[enemy_row][enemy_col] = "EMI" + enemy_num
      
  elif enemy_col == 0: #far left edge, move right
    array1[enemy_row][enemy_col] = "     "
    if " YOU " in array1[enemy_row][enemy_col + 1]:
      array1[enemy_row][enemy_col + 1] = "YOUEMI"
    elif "EMI" not in array1[enemy_row][enemy_col + 1]:
      array1[enemy_row][enemy_col + 1] = "EMI" + enemy_num
    else:
      array1[enemy_row][enemy_col] = "EMI" + enemy_num
      
  elif enemy_row == 14: #bottom edge, move up
    array1[enemy_row][enemy_col] = "     "
    if " YOU " in array1[enemy_row - 1][enemy_col]:
      array1[enemy_row - 1][enemy_col] = "YOUEMI"
    elif "EMI" not in array1[enemy_row - 1][enemy_col]:
      array1[enemy_row - 1][enemy_col] = "EMI" + enemy_num
    else:
      array1[enemy_row][enemy_col] = "EMI" + enemy_num
      
  elif enemy_row == 0: #top edge, move down
    array1[enemy_row][enemy_col] = "     "
    if " YOU " in array1[enemy_row + 1][enemy_col]:
      array1[enemy_row + 1][enemy_col] = "YOUEMI"
    elif "EMI" not in array1[enemy_row + 1][enemy_col]:
      array1[enemy_row + 1][enemy_col] = "EMI" + enemy_num
    else:
      array1[enemy_row][enemy_col] = "EMI" + enemy_num



#------------------------------------Turn Start-----------------------------------
def turn_start(turn_num): 
  """Allows the player to choose which direction they'd like to move in"""
  print("Level " + str(level_num) + ", Turn " + str(turn_num)) #Describes which level and turn number it is in the game
  print('In which direction would you like to move? \n-"right" \n-"left" \n-"up" \n-"down"\n') #which direction it will move

  direction_choice = input("DIRECTION> ")
  direction_choice = direction_choice.lower() #make all responses of direction_choice lower case
  return direction_choice 

  
#-------------------------------Defining Movement---------------------------------
def find_current_row(): #will be defining what row "YOU" will be in based on the len of the array and will return that row it is in
  for row in range(len(array1)):
    if " YOU " in array1[row]:
      current_row = row 
      return current_row

def find_current_col(): #same concept as find_current_row() but with columns
  for row in range(len(array1)):
    if " YOU " in array1[row]:
      current_col = array1[row].index(" YOU ") #index will find the second value
      return current_col

def movement(direction_choice):
  current_row = find_current_row()
  current_col = find_current_col()
  # player chooses to move right
  if direction_choice == "right":
    if current_col < 13: 
      array1[current_row][current_col] = "     "
      if "EMI" in array1[current_row][current_col + 2]:
        array1[current_row][current_col + 2] = "YOUEMI"
      else:
        array1[current_row][current_col + 2] = " YOU "
    elif current_col == 13:
      array1[current_row][current_col] = "     "
      if "EMI" in array1[current_row][current_col + 2]:
        array1[current_row][current_col + 1] = "YOUEMI"
      else:
        array1[current_row][current_col + 1] = " YOU "
    else: 
      print("You can't go that way!")
  # player chooses to move left   
  elif direction_choice == "left":
    if current_col > 1:
      array1[current_row][current_col] = "     "
      if "EMI" in array1[current_row][current_col - 2]:
        array1[current_row][current_col - 2] = "YOUEMI"
      else:
        array1[current_row][current_col - 2] = " YOU "
    elif current_col == 1:
        array1[current_row][current_col] = "     "
        if "EMI" in array1[current_row][current_col - 1]:
          array1[current_row][current_col - 1] = "YOUEMI"
        else:
          array1[current_row][current_col - 1] = " YOU "
    else:
      print("You can't go that way!")
  # player chooses to move up    
  elif direction_choice == "up":
    if current_row > 1:
      array1[current_row][current_col] = "     "
      if "EMI" in array1[current_row - 2][current_col]:
        array1[current_row - 2][current_col] = "YOUEMI"
      else:
        array1[current_row - 2][current_col] = " YOU "
    elif current_col == 1:
        array1[current_row][current_col] = "     "
        if "EMI" in array1[current_row - 1][current_col]:
          array1[current_row - 1][current_col] = "YOUEMI"
        else:
          array1[current_row - 1][current_col] = " YOU "
    else:
      print("You can't go that way!")
  # player chooses to move down    
  elif direction_choice == "down":
    if current_row < 13: 
      array1[current_row][current_col] = "     "
      if "EMI" in array1[current_row + 2][current_col]:
        array1[current_row + 2][current_col] = "YOUEMI"
      else:
        array1[current_row + 2][current_col] = " YOU "
    elif current_col == 13:
      array1[current_row][current_col] = "     "
      if "EMI" in array1[current_row + 1][current_col]:
        array1[current_row + 1][current_col] = "YOUEMI"
      else:
        array1[current_row + 1][current_col] = " YOU "
    else:
      print("You can't go that way!")
#----------------------Game Menu + Gameplay----------------------
print("Welcome to TOWER CHASE") #start of the game and welcome menu
print("~~~~~~~~~~~~~~~~~~~~~~\n")
print("Thanks for playing! \nIf you run into an enemy you will die. To complete the level, make it to the bottom right corner of the array \nThis is how the map will look:\n")
spawn_enemy(enemies)
printarray(array1)
  
while health > 0: #a while statement to allow the player to continue playing until they die
  if level_num != 1: #sets up the array again after level 1
    array1 = [] 
    for row in range(array_row_length):
      column_list = []
      for column in range(array_column_length):
        if column == 0 and row == 0:
          column_list.append(" YOU ")
        elif column == 14 and row == 14: 
          column_list.append(" END ")
        else: 
          column_list.append("     ")
      array1.append(column_list)
    spawn_enemy(enemies)
    print("WELCOME TO LEVEL " + str(level_num)) #short intro to new level
    printarray(array1)
  while array1[14][14] != " YOU ": #while statement that runs until player reaches the end goal (lower right corner of the array)
    movement(turn_start(turn_num)) #allows the player to move first
    current_row = find_current_row()
    current_col = find_current_col()
    if interaction() == True: #check if player has died, exit the program if true
      print("YOU DIED \nRestart system to try again")
      sys.exit()
    else:
      for enemy in range(1, enemies + 1): #for loop allows all of the following to occur for each enemy currently on the array
        #the enemy's number is defined first, based on the for loop
        if enemy < 10:
          enemy_num = ' ' + str(enemy)
        else:
          enemy_num = str(enemy)
        #enemy row and column are determined
        enemy_row = int(find_current_enemy_row(enemy_num))
        enemy_col = int(find_current_enemy_col(enemy_num))
        #enemy moves in a semi-random direction
        enemy_movement(enemy_row, enemy_col)
        if interaction() == True: #check if player has died, exit the program if true
          print("YOU DIED \nRestart system to try again")
          sys.exit()
      else:
        printarray(array1)
    
    turn_num += 1 #increases the turn number incrementally
  #short congratulations for the player every time they complete a level
  print("Congrats on completing level " + str(level_num) + "!")
  print("You will now be moved to the next stage. The number of enemies will increase by 2")
  print("=======================================================================================================================================")
  turn_num = 1 #resets turn number
  level_num += 1 #adds to level number
  enemies += 2 #adds two enemies each time a level is completed
  