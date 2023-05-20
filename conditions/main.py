# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather,time_of_day,cow_milking_status,location_of_the_cows,season,is_slurry_tank_full,is_grass_status_long):
  
    if cow_milking_status == True:
        cow_milking_status_txt = "need milking"
    else:
        cow_milking_status_txt = "don't need milking"

    if is_slurry_tank_full == True:
        is_slurry_tank_full_txt = "full"
    else: 
        is_slurry_tank_full_txt = "empty"
    
    if is_grass_status_long == True:
        is_grass_status_long_txt = "long"
    else:
        is_grass_status_long_txt = "short"

    x = "Good day!\nIn the " + season + " season, at " + time_of_day + " with a " + weather + " condition,\nand your cows " + cow_milking_status_txt + ",\ntheir at the "  + location_of_the_cows + ",\nyour slurry tank is " + is_slurry_tank_full_txt + ",\nand the grass is " + is_grass_status_long_txt + "\n\n\nThis is what you need to do:\n\n"

    if time_of_day == 'night':
        x = x + "take cows to cowshed because it is night\n"
    elif weather == 'rainy':
        x = x + "take cows to cowshed because it is raining\n"
    elif cow_milking_status == True and location_of_the_cows == "pasture":
        x = x + "take cows to cowshed because they need milking\n"
    else:
         x = x + "let cows at pasture\n"
        
    if cow_milking_status == True:
        x = x + "milk the cows\n"
        if location_of_the_cows == "pasture":
            x = x + "bring the cows back to the pasture\n"

    
    if is_slurry_tank_full == True and location_of_the_cows == "cowshed":
        if weather == "neutral" or weather == "rainy":
            x = x + "Fertilize pasture\n"
        else: 
            x = x + "It is " + weather + " now, you need other weather conditions to Fertilize your pasture\n"
    elif is_slurry_tank_full == True and location_of_the_cows == "pasture":
        if weather == "neutral" or weather == "rainy":
            x = x + "take cows to cowshed to Fertilise the pasture\n"
            x = x + "Fertilize pasture\n"
        else:
            x = x + "It is " + weather + " now, you need other weather conditions to Fertilize your pasture\n"
 
    if is_grass_status_long == True and season == "spring" and weather == "sunny":
        if location_of_the_cows == "pasture":
            x = x + "take cows to cowshed so you can mow the grass\n"
            x = x + "mow your grass"
        else:
            x = x + "mow your grass"
              
    return x


print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, False))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, False))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', True, True))
print(farm_action('sunny', 'day', True, 'cowshed', 'spring', True, True))