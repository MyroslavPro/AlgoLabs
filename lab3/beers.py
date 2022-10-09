# 2 D array and then read each worker and satisfy the most picky(repeat) and
# find the min amount of types of beer for the party


def input_read():
    with open("./input.txt", "r") as file:
        n, b = list(map(int, file.readline().split(" ")))
        print(n, b)
        line = file.readline()
        data_for_each_employee = list(line.split(" "))
        data = []

        for i in range(n):
            preferences = []
            for j in range(b):
                if data_for_each_employee[i][j] == 'Y':
                    preferences.append(j+1)
                elif data_for_each_employee[i][j] != 'Y' and data_for_each_employee[i][j] != 'N':
                    raise Exception("The worker's preferences ", i+1, " should only include letters Y and N")
            # Not none check
            if preferences:
                data.append(preferences)

        print("PREFERENCES :", data, "\n")
    return data


def find_the_optimal_num_of_types_of_beer(stats_of_preferences):
    stats_of_preferences.sort(key=len)
    next_types_enjoyers = stats_of_preferences
    counter_of_types = 0

    while next_types_enjoyers:
        stats_of_preferences = next_types_enjoyers
        print(next_types_enjoyers)
        # Looking for the most wanted type of beer
        #   in the worker's preferences(worker who loves small margin of beers)
        num_of_enjoyers_of_current_type = dict()
        for type_beer_selected in stats_of_preferences[0]:
            count = 0
            for i in stats_of_preferences:
                if type_beer_selected in i:
                    count += 1
            num_of_enjoyers_of_current_type[type_beer_selected] = count
        print(num_of_enjoyers_of_current_type)

        # Find the most popular beer among the workers
        #   that the strictest worker likes
        type_of_beer = max(num_of_enjoyers_of_current_type, key=num_of_enjoyers_of_current_type.get)

        print("BEER", type_of_beer, "is selected")
        next_types_enjoyers = []
        for i in stats_of_preferences:
            if type_of_beer not in i:
                next_types_enjoyers.append(i)
        print(next_types_enjoyers)
        print("This beer is checked\n")
        counter_of_types += 1
    return counter_of_types


def output_create(output_result):
    with open("./output.txt", "w") as file:
        print("The number of types of beers needed ->", result_numbers_of_beers)
        file.write(f"{output_result}")


if __name__ == '__main__':
    received_input = input_read()
    result_numbers_of_beers = find_the_optimal_num_of_types_of_beer(received_input)
    output_create(result_numbers_of_beers)
