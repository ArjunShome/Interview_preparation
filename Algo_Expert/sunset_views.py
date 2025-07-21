def sunsetViews(buildings, direction):
    # Write your code here.
    sunset_view_buildings = []
    if direction == "WEST":
        buildings = buildings[::-1]
        index = 0
    else:
        index = len(buildings) - 1 

    while buildings:
        building_height = buildings.pop()

        if len(sunset_view_buildings) > 0:
            prev_highest_building = sunset_view_buildings[-1][0]
            
            if building_height > prev_highest_building:
                sunset_view_buildings.append((building_height, index))        
        else:
            sunset_view_buildings.append((building_height, index))

        index = index + 1 if direction == "WEST" else index - 1
    
    sunset_view_buildings = [building[1] for building in sunset_view_buildings]
    if direction == "EAST":
        sunset_view_buildings = sunset_view_buildings[::-1]
    return sunset_view_buildings


def sunsetViews(buildings, direction):
    result = []
    start, step = (0, 1) if direction == "EAST" else (len(buildings) - 1, -1)
    max_height = 0

    for i in range(start, len(buildings) if direction == "EAST" else -1, step):
        if buildings[i] > max_height:
            result.append(i)
            max_height = buildings[i]

    return result if direction == "EAST" else result[::-1]


if __name__ == "__main__":

    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "WEST"

    print(sunsetViews(buildings, direction))  