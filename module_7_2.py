def custom_write(file_name, strings):
    # f = open(file_name, 'w', encoding='utf-8')
    with open(file_name, 'w', encoding='utf-8') as f:
        strings_positions = {}
        for number_of_line, line in enumerate(strings):
            strings_positions[(number_of_line+1, f.tell())] = line
            f.write(f'{line}\n')
    # f.close()

    return strings_positions


def main():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


if __name__ == "__main__":
    main()
