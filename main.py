def read_files():
    """
        read_files.

        no input data.

        Returns a string concatenating the content of the .txt files
    """
    archivo = '2.txt'
    with open(f'./{archivo}', 'r', encoding='utf-8') as f:
        text = f.read()
    return text



def write_file():
    pass


if __name__ == '__main__':
    print(read_files())