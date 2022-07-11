"""
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
    1c0111001f010100061a024b53535009181c
after hex decoding, and when XOR'd against:
    686974207468652062756c6c277320657965
should produce:
    746865206b696420646f6e277420706c6179
"""

import conversions as cnv


def xor(bin_str1, bin_str2):
    xor_str = format(int(bin_str1, 2) ^ int(bin_str2, 2), 'b')
    return xor_str.zfill(len(bin_str1))


def main():
    str1 = "1c0111001f010100061a024b53535009181c"
    str2 = "686974207468652062756c6c277320657965"
    result = "746865206b696420646f6e277420706c6179"

    bin_str1, bin_str2 = cnv.hex_to_bin(str1), cnv.hex_to_bin(str2)
    xor_str = xor(bin_str1, bin_str2)
    print(cnv.bin_to_hex(xor_str))
    if cnv.bin_to_hex(xor_str) == result:
        print("The strings were XORed correctly")


main()
