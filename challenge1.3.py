"""
Set 1: Challenge 3
Single Byte XOR Cipher

The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.
"""
import conversions as cnv


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


def main():
    freq_table = create_freq_table()                    # Generate the frequency table
    enc_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"    # The given hex string

    bin_str = cnv.hex_to_bin(enc_str)                   # Convert the given string to binary
    ascii_str = xor_loop(bin_str)                       # XOR against all ascii values
    score = frequency_analysis(ascii_str, freq_table)   # Return the score of all resultant strings

    n = score[min(score.keys())]                        # Find the most likely string
    print("The decrypted message is:", ascii_str[n])    # Print the results
    print("It was XORed by:", chr(n))


main()
