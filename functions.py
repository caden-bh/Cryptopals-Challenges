"""
A collection of functions that will be or are likely to be reused for future challenges.
Some functions may be copied or slightly adapted from previously completed challenges.
"""
import conversions as cnv


# Using code found here (https://opendata.stackexchange.com/a/7043)
freq_table = {}
with open("char_freq_Crime_and_Punishment.txt") as file:
    for line in file:
        if line[0] != ' ':
            (dict_key, value) = line.split(sep=' ')
            freq_table[dict_key] = int(value)
        else:
            k = ' '
            v = line[2:]
            freq_table[k] = int(v)

c = 0
for n in freq_table.values():
    c += n

for n in freq_table:
    freq_table.update({n: round(freq_table[n] / c, 10)})


asc_list = list()
for n in range(0, 256):
    asc_list.append('{:08b}'.format(n))


def bin_string_concat(bin_str, length):
    string = ""
    while len(string) < length:
        string += bin_str
    return string[:length]


def repeat_key_concat(key, length):
    result = str.join('', [key] * length)
    return result[:length]


def xor(bin_str1, bin_str2):
    xor_str = format(int(bin_str1, 2) ^ int(bin_str2, 2), 'b')
    return xor_str.zfill(len(bin_str1))


def hamming_distance(bin_str1, bin_str2):
    distance = 0
    for i in range(0, len(bin_str1)):       # Loop through strings and determine if bits are equal
        if bin_str1[i] == bin_str2[i]:
            pass
        else:
            distance += 1                   # Add to distance if they are not
    return distance


def single_char_frequency_analysis(bin_str):
    score = dict()
    for i in range(0, 256):
        count, s = dict(), 0                                # Initialize a dictionary to count characters in the string
        bin_str2 = bin_string_concat('{:08b}'.format(i), len(bin_str))
        xor_str = xor(bin_str, bin_str2)                    # XOR the two strings together
        asc_str = cnv.bin_to_asc(xor_str)                   # Convert the resultant string to ascii to be analyzed

        if "\\x" in asc_str:                                # Proceed if there is a non-representable ascii character
            continue
        else:
            for j in asc_str:
                count[j] = count.get(j, 0) + 1              # Get count of each character in the string

        for j in count.keys():
            if j in freq_table.keys():                      # Add to score of string based on expected frequency
                s += (count[j] / (len(asc_str)) - freq_table[j]) / freq_table[j]
            else:
                # If a character does not appear in frequency table the lowest possible frequency is used
                s += (count[j] / (len(asc_str)) - freq_table['%']) / freq_table['%']

        # Update a dictionary of the scores to be able to find the smallest
        score.update({round(s, 2): [i, asc_str]})

    if score:
        # Return the score, corresponding character XORed against, and the corresponding plaintext
        return min(score.keys()), score[min(score.keys())][0]  # , score[min(score.keys())][1]
    else:
        return -1, -1
