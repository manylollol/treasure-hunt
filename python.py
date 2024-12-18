import random 
import math 

#this is the funtion to calculate distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

#this is the function to display the grid 
def display_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


    
##################################################################################################################


#this is the main game funtion ######
def treasure_hunt():
    print("🌟 Welcome to Treasure hunt! 🌟 ")
    print("You will have to find the hidden treasue. Get hints as you play: 'Hotter' or 'Colder'!\n")


    print("Select a starting level: ")
    print("""
            |---------------Treasure Hunt---------------|
            |   Level          -         1              |
            |   Level          -         2              |
            |   level          -         3              |
            |   level          -         4              |
            |   level          -         5              |
            |   level          -         6              |
            |   level          -         7              |
            |   level          -         8              |
            |   level          -         9              |
            |   level          -         10             |
            |-------------------CHOOSE------------------|
            """)
    print()



    while True:
        try:
            level = int(input("Enter the level you want to start at (1-10)"))
            if 1 <= level <= 10:
                break
            else:
                print("Invalid choice: Please select a level betweeen 1 and 10.\n")

        except ValueError:
            print("Invalid input.Please eneter a number between 1 and 10.\n")










    max_attempts = 8 
    total_score = 0 

    while True:
        print(f"--- Level {level} ---")


        #to increase levels and grid size 
        grid_size = 4 + level 
        grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]


        #where the treasure located random 
        treasure = (random.randint(0, grid_size - 1), random.randint(0, grid_size -1))
        previous_distance = None
        attempts_left = max_attempts

        print(f"Grid Size:{grid_size}x{grid_size} | Attempts: {max_attempts}")
        display_grid(grid)
    
        
        #loop for the level

        while attempts_left > 0:
            try:
                row = int(input(f"Enter row (1-{grid_size}): "))-1
                col = int(input(f"Enter column (1-{grid_size}): "))-1


                if not (0 <= row < grid_size and 0 <= col < grid_size):
                    print("Invalid input. Try again.\n")
                    continue 

                if (row, col) == treasure:
                    print("\n 🎉 Congratulations! You found the treasure 🎉\n  You are rich now\n")
                    break


                grid[row][col] = "x"
                current_distance = distance((row, col), treasure)


                if previous_distance is None:
                    print("You missed! Keep going.")
                else:
                    if current_distance < previous_distance:
                        print("🔥 Hotter! your getting closer.")
                    else:
                        print("❄️ Colder! You're getting farther away.")
                
                previous_distance = current_distance 
                attempts_left -=1
                print(f"Attempts Left: {attempts_left}\n")
                display_grid(grid)

            except ValueError:
                print("Invalid input. Enter number only.\n")

        else:
            print("\n💀 Game Over! You ran out of attempts. ")
            print(f"The treasure was at: Row {treasure[0] + 1}, Column {treasure[1]+1}\n")
            print(f"Your final score: {total_score}")
            break

        level += 1
        print(f" Great job! Moving to level {level}....\n")
    print("Thank for playing the Treasure Hunt Game! 👏")
            

#####################################################################################################################################
# this is to start the game 

if __name__ == "__main__":
    treasure_hunt()




