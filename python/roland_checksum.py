# Also used on the Yamaha Reface CS?
def compute_checksum(data):
    """Compute checksum from a list of byte values.

    This is appended to the data of the sysex message.
    """
    return (128 - (sum(data) & 0x7F)) & 0x7F
