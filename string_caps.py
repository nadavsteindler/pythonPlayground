
# Given a string, write a function to capitalize each word's second letter.(Don't forget lots of small dynamic allocations is much more expensive than one large one)
# Now the Nth letter.
# Now as a stream one char at a time.
# How would you test it--what to focus on?


import sys


def capitalize(arg: str) -> str:
    result = list(arg)
    pos_in_word = 0
    for i, ch in enumerate(result):
        if ch == ' ':
            pos_in_word = 0
        else:
            if pos_in_word == 1:
                result[i] = ch.upper()
            pos_in_word += 1
    return ''.join(result)


if __name__ == "__main__":
    print(capitalize(sys.argv[1]))
