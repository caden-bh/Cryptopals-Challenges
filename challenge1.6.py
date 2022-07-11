"""
There's a file here (https://www.cryptopals.com/static/challenge-data/6.txt).
It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.
"""
import functions as fnc
import conversions as cnv
import requests


def get_text():
    # Save given text file contents as text
    text = requests.get('https://www.cryptopals.com/static/challenge-data/6.txt').text
    lines = text.split()                # Split into lines to avoid conversion mistakes
    total = ""
    for i in lines:
        binary = cnv.b64_to_bin(i)
        total = total + binary          # Save as single binary line for ease of use
    return total                        # Return content of the text file as a single binary line


def hamming_distance(bin_str1, bin_str2):
    distance = 0
    for i in range(0, len(bin_str1)):       # Loop through strings and determine if bits are equal
        if bin_str1[i] == bin_str2[i]:
            pass
        else:
            distance += 1                   # Add to the distance if they are not
    return distance


def find_key_length(text):
    hamming_dict = dict()

    for k in range(2, 41):
        kb = 8 * k                              # Multiply by eight to get length of key size block
        # Save first four blocks
        b1, b2, b3, b4 = text[:kb], text[kb:2*kb], text[2*kb:3*kb], text[3*kb:4*kb]

        # Find the hamming distance between each of the four blocks
        d1, d2, d3 = hamming_distance(b1, b2), hamming_distance(b1, b3), hamming_distance(b1, b4)
        d4, d5, d6 = hamming_distance(b2, b3), hamming_distance(b2, b4), hamming_distance(b3, b4)

        # Determine the average hamming distance by dividing by 6 and the key size
        avg_dist = (d1 + d2 + d3 + d4 + d5 + d6) / (6 * k)
        hamming_dict.update({avg_dist: k})

    l1 = hamming_dict[min(hamming_dict.keys())]
    hamming_dict.pop(min(hamming_dict.keys()))
    l2 = hamming_dict[min(hamming_dict.keys())]
    hamming_dict.pop(min(hamming_dict.keys()))
    l3 = hamming_dict[min(hamming_dict.keys())]
    return [l1, l2, l3]                         # Return the three smallest hamming distance key sizes


def transpose_blocks(text, length):
    block_dict = dict()
    # Initialize a dictionary to store blocks XORed by like characters
    for i in range(0, length):
        block_dict.update({i: ""})

    byte_list = [text[i:i+8] for i in range(0, len(text), 8)]       # Breaks string into bytes

    # Use modular arithmetic to update correct dictionary entries
    for i in range(0, len(byte_list)):
        block_dict.update({i % length: block_dict[i % length] + byte_list[i]})

    return block_dict


def main():
    text = get_text()                           # Get the text as binary string
    poss_lengths = find_key_length(text)        # Get 3 most likely key lengths
    score_dict = dict()                         # Initialize dictionary for keeping scores

    for i in poss_lengths:
        block_dict = transpose_blocks(text, i)  # Get transposed blocks
        ovr_score, key, flag = 0, '', False     # Initialize variables

        for j in block_dict.keys():
            score, char = fnc.single_char_frequency_analysis(block_dict[j])
            # If -1 is returned the XORed plaintext has an unrepresentable ascii character
            if score == -1:
                flag = True
            else:
                ovr_score += score          # Add score for each transposed block to get the total score
                key = key + chr(char)       # Add characters for each block to get the keyf

        # Update score dict if there are no unrepresentable characters, pass otherwise
        if flag is False:
            score_dict.update({ovr_score: key})
        else:
            pass
        block_dict.clear()

    # Get the binary representation for the key
    key_bin = cnv.asc_to_bin(score_dict[min(score_dict.keys())])

    # Get the corresponding plaintext for the key
    plain = cnv.bin_to_asc(fnc.xor(text, fnc.bin_string_concat(key_bin, len(text))))

    # Prints the key and plaintext
    print("The key is:", '\n', score_dict[min(score_dict.keys())], '\n')
    print("The plaintext is:")
    for i in plain.split(sep='\\n'):
        print(' '+i)


main()
