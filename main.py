class WordNode:
    def __init__(self, name):
        self.name = name
        self.children = set()


class WchainProcessing:
    def __init__(self, words):
        self.words = words
        self.dict_chain_length = dict()

    def max_chain(self, value):
        # REMOVING FROM WORDS CURRENT VALUE
        self.words.remove(value)
        word_obj = WordNode(value)

        # Removing one letter and searching for a new word in a dict -> if true ? add to children array :else - skip
        for i in range(len(word_obj.name)):
            check_word = word_obj.name[:i] + word_obj.name[i + 1:]
            print(check_word)
            if check_word in self.words:
                word_obj.children.add(check_word)

        print("Obj Word :", word_obj.name, "has its children:", word_obj.children)

        # if no words after letter removal are possible -> Esc
        if not word_obj.children:
            self.dict_chain_length[word_obj.name] = 1
            return
        else:
            for i in word_obj.children:
                print(" For this obj: ", word_obj.name, "child: ", i)
                if i not in self.dict_chain_length:
                    if len(i) == 1:
                        self.dict_chain_length[i] = 1
                        print("Len 1 of a child")
                        self.words.remove(i)
                    else:
                        print("recursion")
                        self.max_chain(i)

        print("Dict", self.dict_chain_length)
        # Here save the length of chains
        children_len_values = list(map(lambda a: self.dict_chain_length[a], word_obj.children))
        self.dict_chain_length[word_obj.name] = max(children_len_values)+1

        print(self.words)
        print("------------------------------\n")
        return

    def get_max_chain_length(self):
        max_length = max(list(self.dict_chain_length.values()))
        return max_length


def read_input():
    words = set()
    with open("./wchain.in", "r") as file:
        number_of_words = int(file.readline())

        while True:
            line = str(file.readline().rstrip('\n').strip(' '))
            if not line:
                break
            words.add(line)
        if len(words) != number_of_words:
            raise Exception("The input number_of_words isn't matching the number of given ones")

    print(number_of_words)
    print(words)
    return words


def create_output(output_result):
    f = open("./wchain.out", "w")
    f.write(f"{output_result}")
    f.close()


if __name__ == '__main__':
    words_inp = read_input()
    chain_search = WchainProcessing(words_inp)
    while chain_search.words:
        max_len_word = max(chain_search.words, key=len)
        print("From above we intervene ")
        chain_search.max_chain(max_len_word)
    result = chain_search.get_max_chain_length()
    create_output(result)
    print(result)
