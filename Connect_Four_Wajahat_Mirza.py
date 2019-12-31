# Connect Four Game

# 1. Initialize the grid
# 2. Display the Grid
# 3. Ask user 1 for input. Place it and display
# 4. Check for win coordinates
# 5. Ask user 2 for input. Place it and display.
# 6. Check for win coordinates
# 7. Provide option for destroying a disc
# 8. Ask for play again or terminate the game

import os

# To change the grid size without disturbing the code, just change following: 
# num_row(line 16), num_col(line 17), digit_list(line 33) and alphabet(line 39)
num_row = 6
num_col = 7

grid = []
signs = ["X","O"]

# Initialize the grid
def grid_initialize():
    for row in range(num_row):
        height_list = []
        for col in range(num_col):
            height_list.append(" ")
        grid.append(height_list)

# Display the grid
def grid_display():
    #Display Numeric values for columns
    digit_list = [" ","1","  2","  3 "," 4","  5 "," 6 "," 7"]
    for col in range(num_col + 1):
        print(digit_list[col], end=" ")
    print()

    # Display Alphabet letter for rows
    alphabet = ["A","B","C","D","E","F"]
    for row in range(num_row):
        print(alphabet[row], end=" ")
        for col in range(num_col):
            print(grid[row][col],"|",end=" ")
        print("\n " + "---+" * num_col)
        print()

def user_data():
    # input names of two users and assign signs
    player_1_name = input("Player 1, please input your name:")
    player_2_name = input("Player 2, please input your name:")
    players = [player_1_name, player_2_name]
    
    #Assign Signs 
    print(players[0],",you are going FIRST and your sign is,",signs[0],"\n",\
         (players[1]),",you are going SECONd and your sign is,",signs[1],".") 
    print("INSTRUCTIONS: \n \
        Get combination of four either horizontal, vertical, Diagonal. \n \
        Each Player has a chance to destroy one disc any time of the game.\n \
        Disc on top of destroyed disc will fall down ")
    print("We wish you Best of Luck!")
    return players 

def user_input(players): 
    global grid

    # Input Validation. Input should be only the columns 
    valid_inputs = []
    for i in range(1,num_col + 1):
        valid_inputs.append(str(i))
    
    # Count for the number of times each player can destroy a disc 
    count = [1,1]
    # Keep checking if game has ended or not. One of the most important loops in this code
    has_game_end = False
    while True: 
        for turn, name in list(enumerate(players)):
           
            is_destroyed = False
            # Ask user for destroying grid only if user previously have not destroyed a disc or grid is not empty
            if count[turn] == 1 and not check_grid():
                player_target = input(name + ", do you want to destroy a disc on the grid? Give 'Y' for yes or any key for no: ").upper()
                if player_target == "Y":
                    # Update the value of count to 0 so player cannot be to destroy a disc again
                    count[turn] = 0
                    destroy_disc()
                    # Update the value of is_destroyed 
                    is_destroyed = True
            
            if not is_destroyed:
                # if disc is not destroyed, proceed normally
                player_target = input(name + ", please input the column you want to place: ")
            # Check user input is only given in numeric-digit between 1 to 7 and top row in the column has to be empty. 
                while player_target not in valid_inputs or grid[0][int(player_target) - 1] != " ":
                    print("Column is either full or out of range. Enter Again!") 
                    player_target = input(name + ", please hit the correct column you want to target: ")
               
                # Assign targeted column a place in the grid
                grid_col_target = int(player_target) - 1
                display_user_disc(grid_col_target, turn)

            # Check if win combination is True to print winner 
            if win_checker(turn) == True: 
                has_game_end = True
                display_winner(name)
                break
            
            # Check if game is draw to print Game is draw
            elif draw_checker(turn) == True:
                has_game_end = True
                print("Game is drawn. Sorry!")
                break
        
        # Is game has ended, Ask the user if they want to play again
        if has_game_end == True: 
            play_again = input("Game has ended. Do you want to play again? Type 'Y' or 'N': ").upper()
            if play_again == "Y":
                # Use Global grid to assing local grid value to the global variabel grid in line 17
                grid = []
                count = [1,1]
                grid_initialize()
                grid_display()
                # Re-Assign has game ended to False 
                has_game_end = False
            else: 
                break 

    return grid_col_target, turn, name

def display_user_disc(col_targeted, turn):
    #Place target column in the last available cell of column 
    for row, element in reversed(list(enumerate(grid))):
        os.system("cls" if os.name=="nt" else "clear")
        if grid[row][col_targeted] == " ": 
            grid[row][col_targeted] = signs[turn]
            break
        else:
            print("Looks like coordinate is already full. enter again.")

    grid_display()

def win_checker(turn):
    # Win check for horizontal combination
    for col in range(num_col - 3):
        for row in range(num_row):
            if grid[row][col] == signs[turn] and grid[row][col + 1] == signs[turn] and \
                grid[row][col + 2] == signs[turn] and grid[row][col + 3] == signs[turn]:
                return True 

    # Win check for vertical combination
    for col in range(num_col):
        for row in range(num_row - 3):
            if grid[row][col] == signs[turn] and grid[row + 1][col] == signs[turn] and \
                grid[row + 2][col] == signs[turn] and grid[row + 3][col] == signs[turn]:
                return True
       
    # Win Check for Positive Diagonal combination
    for col in range(num_col - 3):
        for row in range(num_row - 3):
            if grid[row][col] == signs[turn] and grid[row + 1][col + 1] == signs[turn] and \
                grid[row + 2][col + 2] == signs[turn] and grid[row + 3][col + 3] == signs[turn]:
                return True
    
    # Win Check Negative Diagonal combination 
    for col in range(num_col - 3):
        for row in range(3, num_row):
            if grid[row][col] == signs[turn] and grid[row - 1][col + 1] == signs[turn] and \
                grid[row - 2][col + 2] == signs[turn] and grid[row - 3][col + 3] == signs[turn]:
                return True  
    # If win combination is not detected, return False value
    return False
    
def draw_checker(turn): 
    is_draw = True
    # Even if a single cell is empty, game is not draw
    for col in range(num_col):
        for row in range(num_row): 
            if grid[row][col] == " ":
                is_draw = False
    return is_draw

def check_grid():
    is_empty = True
    for col in range(num_col):
        for row in range(num_row): 
            if grid[row][col] != " ":
                is_empty = False
    return is_empty

def destroy_disc(): 
    while True:
        disc_target = input("Please input which disc you want to destro: Enter as '7 D': ")
        elements = disc_target.split(" ")
        if len(elements) != 2:
            continue
        if (elements[0].isdigit() == False) or (elements[1].isalpha() == False) or (len(elements[1]) != 1): 
            continue
        target_row = ord(elements[1].upper()) - ord('A') 
        target_column = int(elements[0]) - 1 

        if target_row not in range(6) or target_column not in range(7):
            continue
        if grid[target_row][target_column] == " ":
            continue

        for i in range(target_row, 0, - 1):
            grid[i][target_column] = grid[i-1][target_column]
        grid[0][target_column] = ' '
        break
    grid_display()

def display_winner(name): 
   print(name, " HAS WON THE GAME! It's your lucky day!")

def main():
    grid_initialize()
    grid_display()
    players = user_data()
    col_targeted, turn, name = user_input(players)

main()

