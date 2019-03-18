import math

#this function first takes numberber of coordinates and then coordinates accordingly and calculate center of mass,
#distance of each point to center of mass and gives the closest and farthest point.

def create_list(number):
    while number > 0:
        
        input_coords = input("Please enter the coordinates in tuple form. i.e (6,1)")
        
        coordinates = (int(input_coords.split(',')[0][1:]) , int(input_coords.split(',')[1].split(')')[0]))
        
        coord_list.append(coordinates)
        number -= 1
        
    print("Coordinate list: ",coord_list)

    

#this function calculate center of mass and gives is as a tuple
def calculate_com(number):
    xc     = 0
    yc     = 0
    i = 0
    
    
    while number > 0:
        xc     += coord_list[i][0]
        yc     += coord_list[i][1]
        number   -= 1
        i += 1
        
        
    xc = xc / i
    yc = yc / i
    
    print("Center of mass: ", (xc,yc))
    return (xc, yc)
    
#this function calculates distances between center of mass and input points

def euclidean_distance(number):
    i = 0
    
    while number > 0:
        x     = 0
        y     = 0
        x     += (com[0] - coord_list[i][0])**2
        y     += (com[1] - coord_list[i][1])**2
        
        euclidean = math.sqrt(x + y)
        euclidean_list.append(euclidean)
        number      -= 1
        i    += 1
    
    print("The list of distance: ", euclidean_list)



#This function finds the closest and farthest point
def closest_and_farthest(number):
    i = 0
    min_dist = min(euclidean_list)
    max_dist = max(euclidean_list)
    
    while number > 0:
        if min_dist == euclidean_list[i]:
            print("Closest point is : ", coord_list[i])
        if max_dist == euclidean_list[i]:
            print("Farthest point is: ", coord_list[i])
        i += 1
        number   -= 1
    


if __name__ == "__main__":
    
    coord_list = []

    print("Please enter how many coordinates will be given.")
    a = input()
    
    # takes the total number of coordinates
    num_elements = int(a)
    print("numberber of coordinate tuples is: ", num_elements)
    
    # create_list function call
    create_list(num_elements)
    
    # calculate_com function call
    com = calculate_com(num_elements)
    
    euclidean_list = []
    
    # euclidean_distance function call
    # calculate all distances, and save them to euclidean_list
    euclidean_distance(num_elements)
    
    # closest_and_farthest function call
    closest_and_farthest(num_elements)