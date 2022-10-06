from collections import deque


# get graph from text file
def search_for_cycles(graph_adj_list):
    visited = set()
    bfs_check_queue = deque()
    parents = {}
    # Start of the queue for BFS
    bfs_check_queue.append(next(iter(graph_adj_list)))
    while bfs_check_queue:
        key = bfs_check_queue.popleft()
        for i in graph_adj_list[key]:
            if (i in visited) and (parents.get(key) != i):
                print("Cycle")
                return True

            # Adding next element to the queue
            if i not in visited:
                bfs_check_queue.append(i)
                parents[i] = key
        visited.add(key)
    return False


def read_input():
    read_dict = dict()
    with open("./input.txt", "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            values = list(map(int, line.strip().split(" ")))

            # if the same value -> error
            if (len(values) != 2) or (values[0] == values[1]):
                raise Exception("The input row isn't matching edge requirements")

            try:
                if values[1] not in read_dict[values[0]]:
                    read_dict[values[0]].append(values[1])
            except KeyError:
                read_dict[values[0]] = [values[1]]

            try:
                if values[0] not in read_dict[values[1]]:
                    read_dict[values[1]].append(values[0])
            except KeyError:
                read_dict[values[1]] = [values[0]]

        print(read_dict)
        return read_dict


def create_output(output_result):
    f = open("./output.txt", "w")
    f.write(f"{output_result}")
    f.close()


# return True if there is a cycle from text file
if __name__ == '__main__':
    graph = read_input()

    result = search_for_cycles(graph)
    create_output(result)

    print(result)
