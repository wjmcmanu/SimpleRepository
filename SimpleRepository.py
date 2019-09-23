"""
SimpleRepository.py

this program prompts the user for a line of text and then prints it out
"""

def body():
    """Returns a string of Hello World"""

    val = input('Please type in some text: ')
    print(f'You Text Was: {val}')

if __name__ == '__main__':
    body()
