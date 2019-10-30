# Jordan An
# 10/25/2019
# EC: Set fire to a forest basic simulation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random
import copy

n = int(input("Enter the dimension of the grid (> 0): "))

# Input validation
while n <= 0:
    n = int(input("Error! Enter the dimension of the grid (> 0): "))
    
# I love putting stuff in the main function so that I can write other function
# below it
def main():
    '''main'''
    # Make an initial list
    auto_image = init_grid(n, 2)

    # Create a deep copy of the initial generation to animate
    init_im = copy.deepcopy(auto_image)
    
    # 0 is barren, 1 is dry grass, 2 is fire, 3 is hot fire, 4 is burnted
    f = int(input("Enter the number of cells you want to set on fire: "))

    # Input validation
    while f <= 0:
        f = int(input("Error! The number of cells need to be positive: "))
    

    # Randomly setting stuffs on Hot Fire
    for i in range(f):
        auto_image[random.randint(0, n-1)][random.randint(0, n-1)] = 3

    # Create an empty list to store each generation for animation
    im_gen = []
    
    # Update the generation
    next_gen = True
    gen_count = 0
    
    while next_gen:
        # It will stop if last gen doesn't have any Fire or Hot Fire
        next_gen = False
        #print(auto_image)
        # Uncomment this if you want to see each gen
        '''plt.imshow(auto_image, cmap= 'Reds')
        plt.title("Linear Cellular Automata of forest fire")
        plt.xlabel("Gen: %i" % gen_count)
        
        plt.show()'''
        
        # Keep up the generation count
        gen_count += 1
        
        # Make an empty list to make a copy of the old generation
        '''old_grid = []'''

        # For some reason the .copy() still changes the old grid when I change
        # the auto image (Is it because it's 2D?), so I made a copy manually
        #old_grid = auto_image.copy()
        '''for i in range(n):
            old_grid.append([auto_image[i][0]])
            for j in range(1, n):
                old_grid[i].append(auto_image[i][j])'''

        # Be fancy and use deep copy
        old_grid = copy.deepcopy(auto_image)
        im_gen.append(old_grid)
        
        for i in range(n):
            for j in range(n):
                # Follow the rule
                # Set the nex_gen value to True if there is still a fire
                if auto_image[i][j] == 0 and 3 in neighbor(i, j, old_grid):
                    auto_image[i][j] = 2
                    next_gen = True
                elif auto_image[i][j] == 1 and (2 in neighbor(i, j, old_grid)
                                                or
                                                3 in neighbor(i, j, old_grid)):
                    auto_image[i][j] = 3
                    next_gen = True
                elif auto_image[i][j] == 3:
                    auto_image[i][j] = 2
                    next_gen = True
                elif auto_image[i][j] == 2 and 3 in neighbor(i, j, old_grid):
                    auto_image[i][j] = 2
                    next_gen = True
                elif auto_image[i][j] == 2:
                    auto_image[i][j] = 4
        

        # End of loop
    # Add to the list each generation 
    im_gen.append(auto_image)    
    #print(im_gen)

    # Animation
    fig = plt.figure()
    a = np.asarray(im_gen)
    im = plt.imshow(init_im, cmap= 'Reds')
    
    def init():
        '''Initial picture'''
        # Make im the first generation
        im.set_data(init_im)
        im.autoscale()
        return [im]

    def animate(i):
        '''Each frame is a generation'''
        #print(a[i])
        im.set_data(a[i])
        # Yay I found the solution for the color on
        # https://stackoverflow.com/questions
        # /16657334/colormap-issue-using-animation-in-matplotlib
        # But I still dont understand why we don't need to use the autoscale
        # when showing each generation
        im.autoscale()
        return [im]

    #print(gen_count)
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=gen_count, interval=70)

    plt.xlabel("Number of generations: %i" % gen_count)
    plt.title("Linear Cellular Automata of forest fire")
    plt.show()
    
    # It's kinda boring only to show the last gen           
    '''plt.imshow(auto_image, cmap= 'Reds')
    plt.title("Linear Cellular Automata")
    plt.xlabel("Gen: %i" % gen_count)

    plt.show()'''


def init_grid(d, o):
    '''Return a 2D list d x d filled with number from 0 to o (o is the number of
    options).'''

    temp = []
    # Pretty straight forward
    for i in range(d):
        temp.append([])
        for j in range(d):
            temp[i].append(random.choice(range(o)))
            
    return temp

def neighbor(index_x, index_y, grid):
    '''Return a list containing the value of the cell (index_x, index_y)'s
    neighbor in list grid'''
    temp = []

    # loop to go through the neighbor
    for i in range(-1,2):
        for j in range(-1,2):
            # Use try, except in case we are evaluating cell on the edge
            try:
                # Funny what I learnt while trying to solve the magic square
                check1, check2 = i + index_x, j + index_y

                # Ignore if it loops around and ignore the cell itself
                if check1 < 0 or check2 < 0 or (i == 0 and j == 0):
                    continue
                
                temp.append(grid[check1][check2])
                
            # Out of bound then go next    
            except IndexError:
                continue
    #print("The neighbor for (%i,%i) is:" %(index_x,index_y), temp)
    return temp


    
# I was about to make a function to return false when the grid doesn't have
# Fire and Hot Fire
'''def get_out(grid):
    for i in range(n):
        for j in range(n):
            if '''

# Run the thing
main()
