'''
Takes one command line argument viz, source-file
input data is taken form source-file
output data is written in console
Ex: py convert_code_to_md.py <src-file>

Takes two command line arguments viz, source-file and destination-file
input data is taken from source-file
output data is written in destination-file
Ex: py convert_code_to_md.py <src-file> <dest-file>

Converts a text/code into it's markdown
This allows you to display your code in online forums with it's actual representation
useful link - https://help.disqus.com/en/articles/1717235-what-html-tags-are-allowed-within-comments
'''

import sys
import os

if __name__ == '__main__':
    try:
        src = sys.argv[1]
    except IndexError:
        src = None
        print('Insufficient Parameters.')
        print(__doc__)
        exit(-1)

    try:
        dest = sys.argv[2]
    except IndexError:
        dest = None

    if not os.path.isfile(src):
        print("Source file doesn't exist.")
        exit(-1)

    if dest is not None and os.path.isfile(dest):
        choice = input("Destination file already exists. Do you want to overwrite it? (Y/N). ")
        if not choice.strip().upper() == 'Y':
            exit(0)

    code = input("Enter the type of data (Code-1/Text-2). ")
    if int(code) == 1:
        code = True
    elif int(code) == 2:
        code = False
    else:
        print('Incorrect choice')
        exit(-1)

    special_chars = {'"': '&quot;', '&': '&amp;', '\'': '&apos;', '<': '&lt;', '>': '&gt;'}

    with open(src, 'r') as src_file:
        if dest:
            with open(dest, 'w') as dest_file:
                if code:
                    dest_file.write('<pre><code>\n')

                for line in src_file.readlines():
                    for char, value in special_chars.items():
                        line = line.replace(char, value)
                    dest_file.write(line)

                if code:
                    dest_file.write('\n</code></pre>')

                print('Copying successful')
        else:
            if code:
                print('<pre><code>\n', end='')

            for line in src_file.readlines():
                for char, value in special_chars.items():
                    line = line.replace(char, value)
                print(line, end='')

            if code:
                print('\n</code></pre>', end='')





