"""
Convert Hex to Base64

The string:
 "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
should produce:
 "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
"""
import binascii


def hex_to_b64(string):
    bin_str = binascii.a2b_hex(string)                      # Turn the string into bytes
    b64_enc = binascii.b2a_base64(bin_str, newline=False)   # Convert bytes into base64
    return str(b64_enc)[2:len(b64_enc)+2]                   # Return base64 encrypted string


def main():
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    b64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    answer = hex_to_b64(hex_str)
    print(answer)                   # Print the resultant string
    if answer == b64_str:
        print("The string was converted correctly.")


main()
