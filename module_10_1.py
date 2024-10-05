from time import sleep

def write_words(word_count:int, file_name:str):
    with open(file_name, 'w') as f:
        for i in range(1, word_count+1):
            word = f'Какое то слово # {i}\n'
            f.write(word)
            sleep(0.1)
            print('word', i)
            
            
print(write_words(3, 'example.txt'))