 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 17:37:59 2025

@author: C1 - base_ferry first elts define the parameters of the new system 
"""

def multi_lanes(s_car = (350,400), m_car = (400,450), l_car = (450,500), van = (500,600), lorry = (600,2000)):
   # These are the intervals for each type of vehicle that are going to be seperated into different queues 
    

    
    return {"s_car": s_car, "m_car": m_car, "l_car": l_car, "van": van, "lorry": lorry}


def main():
# opens file of vehicle length 
    L = []
    with open("input_vals.txt", "r") as f:
        c = int(f.readline())
        numLanes = int(f.readline())
        for line in f:
            L.append(int(line))
            
    size_intervals = multi_lanes()
    # creates the 5 seperate queues that are desired
    lorry = []
    van = []
    l_car = []
    m_car = []
    s_car = []
    
    for v in L:
    
        if 600 <= v <= 2000:
            lorry.append(v)

        elif 500 <= v < 600:
            van.append(v)
        
        elif 450 <= v < 500:
            l_car.append(v)
        
        elif 400 <= v < 450:
            m_car.append(v)
        
        elif 350 <= v < 400:
            s_car.append(v)
        
        
    
    lanes = [[] for i in range(numLanes)]
    overflow = []
    start_lane = 0
    #orders the 5 queues
    loading_order = [lorry, van, l_car, m_car, s_car]
    
    for queue in loading_order:
        for vehicle in queue:
            lane_order = find_lane_for_vehicle(vehicle, lanes, c, start_lane)
            
            if lane_order == -1:
                overflow.append(vehicle)
            else:
                lanes[lane_order].append(vehicle)
                start_lane = (lane_order + 1) % numLanes

    
        
    print("vehicles that overflowed", overflow)
    print("total overflow", len(overflow))
    print("total overflow in cm", (sum(overflow)))
       
    
   
                
                
   
def find_lane_for_vehicle(vehicle_length, lanes, capacity, start_lane=0):
    num_lanes = len(lanes)


    for x in range(num_lanes):
        i = (start_lane + x) % num_lanes  
      
        if sum(lanes[i]) + vehicle_length <= capacity:
            return i

    
    return -1


if __name__ == "__main__":
    main()


    

   






    








                
     

         
        
    
