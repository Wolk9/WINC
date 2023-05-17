# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather,time_of_day,cow_milking_status,location_cows,season,is_slurry_tank_full,is_grass_status_long):
    if weather == 'rainy':
        take_cow_to_cowshed = True
        milk_cows = True
        fertilize_pasture = True
        mow_grass = False
    elif weather == 'sunny':
        take_cow_to_cowshed = True
        milk_cows = True
        fertilize_pasture = False
        mow_grass = True
    elif weather == 'windy':
        take_cow_to_cowshed = True
        milk_cows = True
        fertilize_pasture = False
        mow_grass = False
    elif weather == 'neutral':
        take_cow_to_cowshed = True
        milk_cows = True
        fertilize_pasture = True
        mow_grass = False
    else: 
        take_cow_to_cowshed = False
        milk_cows = False
        fertilize_pasture = False
        mow_grass = False

    if time_of_day == 'day':
        take_cow_to_cowshed = False
        milk_cows = True
        fertilize_pasture = True
        mow_grass = True
    elif time_of_day == 'night':
        take_cow_to_cowshed = True
        milk_cows = True
        fertilize_pasture = True
        mow_grass = True
    else:
        take_cow_to_cowshed = False
        milk_cows = False
        fertilize_pasture = False
        mow_grass = False

    if cow_milking_status == True:
        milk_cows = True
    elif cow_milking_status == False:
        milk_cows = False
    else:
        milk_cows = False

    if location_cows == 'cowshed':
        take_cow_to_cowshed = False
        fertilize_pasture = True
        mow_grass = True  
    elif location_cows == 'pasture':
        take_cow_to_cowshed = True
        fertilize_pasture = False
        mow_grass = False
    else:
        take_cow_to_cowshed = False
        mow_grass = False

    if season == 'winter':
        mow_grass = False
    elif season == 'spring':
        mow_grass = True
    elif season == 'summer':
        mow_grass = False    
    elif season == 'fall':
        mow_grass = False
    else: 
        mow_grass = False

    if is_slurry_tank_full == True:
        fertilize_pasture = True
    else:
        fertilize_pasture = False


    if is_grass_status_long == True:
        mow_grass = True 
    else:
        mow_grass = False

    if take_cow_to_cowshed == True:
        print("take cows to cowshed")
    elif (milk_cows == True):
        print("milk cows")
    elif (fertilize_pasture == True):
        print("fertilize pasture")
    elif (mow_grass == True):
        print("mow grass") 
    else:
        print("wait")


print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))