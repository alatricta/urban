def single_root_words(root_word: str, *other_words):
    same_words = [a for a in other_words if ((root_word in a) or (a in root_word))]
    print(same_words)
    
    
if __name__ == '__main__':
    single_root_words('asd', 'vreg', 'asdfg', 'vfd', 'as')