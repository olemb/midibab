"""
Bytepack format used by Dave Smith Intruments and Korg.

* Korg Minilogue
* Korg Triton LE
* DSI OB6

From Korg Triton LE MIDI implementation manual (TRITON_Le_MIDIimp.txt):

*5 DATA CONVERT METHOD(INTERNAL DATA<-->MIDI DATA)

+------------------------------------------------------------------------+
|  Internal 7byte data <--convert--> MIDI 8 byte data                    |
|  example) Internal data(bit image) MIDI data(bit image)                |
|                Aaaaaaaa            0GFEDCBA                            |
|                Bbbbbbbb            0aaaaaaa                            |
|                Cccccccc            0bbbbbbb                            |
|                Dddddddd            0ccccccc                            |
|                Eeeeeeee            0ddddddd                            |
|                Ffffffff            0eeeeeee                            |
|                Gggggggg            0fffffff                            |
|                Hhhhhhhh            0ggggggg                            |
|                Iiiiiiii            0NMLKJIH                            |
|                   :                0hhhhhhh                            |
|                   :                   :                                |
|                Vvvvvvvv            000000WV                            |
|                Wwwwwwww            0vvvvvvv                            |
|                                    0wwwwwww                            |
|                                    11110111 (EOX=F7H)                  |
+------------------------------------------------------------------------+
"""

def pack_data(data):
    data = list(data)
    packed_data = []
 
    while data:
        msbits = 0
        chunk, data = data[:7], data[7:]
        packed_chunk = []

        for i, byte in enumerate(chunk):
            if byte >= 0x80:
                msbits |= (1 << i)
            packed_chunk.append(byte & 0x7f)

        packed_data.append(msbits)
        packed_data.extend(packed_chunk)

    return packed_data


def unpack_data(data):
    data = list(data)
    unpacked = []

    while data:
        msbits, chunk, data = data[0], data[1:8], data[8:]
        
        for i, byte in enumerate(chunk):
            if msbits & (1 << i):
                byte |= 0x80
            unpacked.append(byte)

    return unpacked


def print_byte(byte):
    print('  {:08b}'.format(byte))


def print_data(data, heading):
    print(heading)
    for byte in data:
        print_byte(byte)
    print()


if __name__ == '__main__':
    data = [0xff, 0x01, 0xff, 0x03]
    print_data(data, 'Input')
    
    packed = pack_data(data)
    print_data(packed, 'Packed')
    
    unpacked = unpack_data(packed)
    print_data(unpacked, 'Unpacked')
