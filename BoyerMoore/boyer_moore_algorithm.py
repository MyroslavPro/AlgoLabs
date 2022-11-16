def search(text, pattern, dictionary_displace):
    i = len(pattern)-1
    while i < len(text):
        for j in range(len(pattern)-1, -1, -1):
            if text[i-(len(pattern)-1-j)] == pattern[j]:
                if j == 0:
                    return True
                continue
            else:
                try:
                    i += dictionary_displace[text[i-(len(pattern)-1-j)]]
                except KeyError:
                    i += dictionary_displace["else"]
                # print("break")
                break
    return False


def create_table_of_displacement(pattern):
    displacement_dict = dict()
    letters_in_pattern_set = set()
    last_elem_pos = len(pattern)-1

    for i in range(last_elem_pos-1, -1, -1):
        if pattern[i] not in letters_in_pattern_set:
            displacement_dict[pattern[i]] = last_elem_pos-i
            letters_in_pattern_set.add(pattern[i])

    if pattern[last_elem_pos] not in letters_in_pattern_set:
        displacement_dict[pattern[last_elem_pos]] = len(pattern)

    displacement_dict["else"] = len(pattern)
    print(displacement_dict)
    return displacement_dict


def main(text, search_pattern):
    dict_displacement = create_table_of_displacement(search_pattern)
    found = search(text, search_pattern, dict_displacement)
    if found:
        print(f"We found it -> : {search_pattern}")
    else:
        print("Not found")


if __name__ == '__main__':
    text_inp = "fowboyfsafafeafafggfffffffffffffffffffffffffffffcowboy"
    search_pattern_inp = "cowboy"
    main(text_inp, search_pattern_inp)
