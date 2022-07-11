"""
Here is the opening stanza of an important work of the English language:
    Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.
It should come out to:
    0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
    a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
"""
import functions as fnc
import conversions as cnv


def main():
    # Given plaintext and key
    plain = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124" \
             "333a653e2b2027630c692b20283165286326302e27282f"

    full_key = fnc.repeat_key_concat(key, len(plain))   # Concat key to be equal length as plaintext
    plain_bin = cnv.asc_to_bin(plain)                   # Convert plaintext to binary
    key_bin = cnv.asc_to_bin(full_key)                  # Convert key to binary

    result = fnc.xor(plain_bin, key_bin)                # Get resultant XORed string
    hex_str = cnv.bin_to_hex(result)                    # Encode with HEX to check if it is correct

    if hex_str == answer:
        print("The string was encrypted correctly")


main()
