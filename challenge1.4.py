"""
Set 1: Challenge 4
Detect Single-Character XOR

One of the 60-character strings in this file (https://www.cryptopals.com/static/challenge-data/4.txt)
has been encrypted by single-character XOR.

Find it.
"""
import conversions as cnv
import requests


def create_freq_table():
    # Create the character frequency dictionary
    freq_dict = {}
    with open("char_freq_Crime_and_Punishment.txt") as file:
        for line in file:
            if line[0] != ' ':
                (key, value) = line.split(sep=' ')
                freq_dict[key] = int(value)
            else:
                k = ' '
                v = line[2:]
                freq_dict[k] = int(v)

    s = 0
    for i in freq_dict.values():
        s += i

    for i in freq_dict:
        freq_dict.update({i: round(freq_dict[i] / s, 10)})

    return freq_dict


def xor_loop(bin_str):
    concat_len = int(len(bin_str) / 8)
    ascii_str = list()

    for i in range(0, 256):
        char = str.join('', ['{:08b}'.format(i)]*concat_len)    # Concat equal length string to be XORed
        xor = format(int(bin_str, 2) ^ int(char, 2), 'b')       # XORs the two strings
        xor_str = xor.zfill(len(bin_str))                       # Add leading zeroes back to string
        ascii_str.append(cnv.bin_to_asc(xor_str))               # Converts ascii byte array to string

    return ascii_str


def frequency_analysis(ascii_str, freq_table):      # Can be improved to use bigrams and trigrams
    score = dict()                                  # Dictionary for keeping scores

    for i in range(len(ascii_str)):                     # Loop through each XORed string to determine the score
        count, s, string = dict(), 0, ascii_str[i]      # Initialize dictionary to keep track of characters in a string

        if "\\x" in string:                         # Continue if unrepresentable ascii character is in the string
            continue
        else:                                       # Otherwise, count each character
            for j in string[2:len(string)-1]:
                count[j] = count.get(j, 0) + 1

        for j in count.keys():
            if j in freq_table.keys():
                # If a character is in the frequency table then create a score based on its expected frequency
                s += (count[j] / (len(string) - 3) - freq_table[j]) / freq_table[j]
            else:
                # If character is representable but not in the table then give score it as the least likely frequency
                s += (count[j] / (len(string) - 3) - freq_table['%']) / freq_table['%']

        score.update({round(s, 2): i})

    return score


def get_hex_strings():
    text = requests.get('https://www.cryptopals.com/static/challenge-data/4.txt').text  # Given text document
    lines = text.split()        # Split string on whitespace
    return lines                # Return iterable of hex strings


def main():
    freq_table = create_freq_table()    # Get the frequency table
    lines = get_hex_strings()           # Get the given hex encoded strings
    min_scores = dict()                 # Initiate dictionary to keep track of the minimum score for each line

    for i in range(len(lines)):
        bin_str = cnv.hex_to_bin(lines[i])                  # Convert hex strings to binary
        ascii_str = xor_loop(bin_str)                       # Pass each string through ascii character xor loop
        score = frequency_analysis(ascii_str, freq_table)   # Determine score of resultant strings

        if score:
            best_score = ascii_str[score[min(score.keys())]]    # Determine best score for the given string
            # Save in a dictionary to compare with other string best scores
            min_scores.update({min(score.keys()): [best_score, score[min(score.keys())]]})
        else:
            pass

    # Print string with the best score and character used to encrypt it
    print("The decrypted string is:", min_scores[min(min_scores.keys())][0])
    print("It was XORed by:", chr(min_scores[min(min_scores.keys())][1]))


main()
