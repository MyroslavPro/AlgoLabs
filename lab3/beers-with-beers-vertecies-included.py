# 2 dictionaries and do kinda dfs and stop at the beers(kill their linked likers)
#  find the min amount of types of beer for the party


def input_read():
    with open("./input.txt", "r") as file:
        n, b = list(map(int, file.readline().split(" ")))
        print(n, b)
        line = file.readline()
        data_for_each_employee = list(line.split(" "))
        data = dict()
        beers = dict()

        for i in range(n):
            for j in range(b):
                if data_for_each_employee[i][j] == 'Y':
                    try:
                        data[i+1].append(j+1)
                    except KeyError:
                        data[i+1] = [j+1]

                    try:
                        beers[j+1].append(i+1)
                    except KeyError:
                        beers[j+1] = [i+1]

                elif data_for_each_employee[i][j] != 'Y' and data_for_each_employee[i][j] != 'N':
                    raise Exception("The worker's preferences ", i+1, " should only include letters Y and N")

        print("PREFERENCES :", data)
        print("Beers :", beers, "\n")
    return data, beers


def find_the_optimal_num_of_types_of_beer(stats_of_preferences, beers):
    counter_of_types = 0

    while stats_of_preferences:
        print(stats_of_preferences)
        # Looking for the most wanted type of beer
        #   in the worker's preferences(in a selected worker)
        array_of_the_worker_with_the_same_preferences = []

        # for type_beer_selected in stats_of_preferences[next(iter(stats_of_preferences))]:
        for type_beer_selected in stats_of_preferences[list(stats_of_preferences.keys())[0]]:
            array_of_the_worker_with_the_same_preferences.append(beers[type_beer_selected])
        array_of_the_worker = max(array_of_the_worker_with_the_same_preferences, key=len)

        # Find the most popular beer among the workers
        #   that the current worker likes
        for i in array_of_the_worker:
            if i in stats_of_preferences:
                stats_of_preferences.pop(i)

        print("This beer is checked\n")
        counter_of_types += 1
    return counter_of_types


def output_create(output_result):
    with open("./output.txt", "w") as file:
        print("The number of types of beers needed ->", output_result)
        file.write(f"{output_result}")


if __name__ == '__main__':
    received_workers, received_beers = input_read()
    result_numbers_of_beers = find_the_optimal_num_of_types_of_beer(received_workers, received_beers)
    output_create(result_numbers_of_beers)
