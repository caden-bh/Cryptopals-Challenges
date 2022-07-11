import binascii


def bin_to_hex(binary):
    hex_str = hex(int(binary, 2))[2:]
    return hex_str.zfill(int(len(binary) / 4))


def bin_to_b64(binary):
    hex_str = bin_to_hex(binary)
    bin_str = binascii.a2b_hex(hex_str)
    b64_enc = binascii.b2a_base64(bin_str, newline=False)
    return str(b64_enc)[2:len(b64_enc)+2]


def hex_to_bin(hex_str):
    hex_int = int(hex_str, 16)
    binary = bin(hex_int)[2:]
    return binary.zfill(len(hex_str) * 4)


def b64_to_bin(b64_str):
    dec = binascii.a2b_base64(b64_str)
    bin_str = "".join(["{:08b}".format(i) for i in dec])
    return bin_str.zfill(len(b64_str) * 6)


def asc_to_bin(asc_str):
    enc_str = asc_str.encode('ascii')
    bin_str = "".join(["{:08b}".format(i) for i in enc_str])
    return bin_str


def bin_to_asc(binary):
    hex_str = bin_to_hex(binary)
    asc_str = binascii.a2b_hex(hex_str)
    return str(asc_str)[2:len(asc_str)+2]


def hex_to_asc(hex_str):
    asc_str = binascii.a2b_hex(hex_str)
    return str(asc_str)[2:len(asc_str)+2]


def b64_to_asc(b64_str):
    asc_str = binascii.a2b_base64(b64_str)
    return str(asc_str)[2:len(asc_str)+2]
