def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    distance_to_cover = 0
    fuel_available = 0
    starting_city_index = 0
    current_city_index = starting_city_index
    cities_covered = 0

    total_number_of_cities = len(distances)

    while cities_covered < total_number_of_cities:
        if current_city_index == total_number_of_cities:
            current_city_index = 0
        
        distance_to_next = distances[current_city_index]
        fuel_refilled = fuel[current_city_index] * mpg

        distance_to_cover += distance_to_next
        fuel_available += fuel_refilled

        if fuel_available < distance_to_cover:
            distance_to_cover = 0
            fuel_available = 0
            current_city_index += 1
            starting_city_index = current_city_index
            cities_covered = 0
        else:
            current_city_index += 1
            cities_covered += 1

    return starting_city_index



if __name__ == '__main__':
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpd = 10

    print(validStartingCity(distances, fuel, mpd))