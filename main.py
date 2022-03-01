import os, sys

def read_files():
    """
        read_files.

        no input data.

        Returns a string concatenating the content of the .txt files
    """
    files = os.listdir('./')
    text =''
    for filename in files:
        if filename.split('.')[-1] == 'txt':
            with open(f'./{filename}', 'r', encoding='utf-8') as f:
                text += str(f.read()) + '\n'
    return text


def write_file():
    """
        write_files.

        no input data.

        it does not return data, it just saves all the text in a single .txt file
    """
    text = read_files()
    with open('./all.txt', 'w', encoding='utf-8') as f:
        f.write(text)


def run():
    write_file()


if __name__ == '__main__':
    run()