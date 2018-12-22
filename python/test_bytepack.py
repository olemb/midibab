from patchbox.bytepack import pack_data, unpack_data

def test_something():
    data = list(range(256))

    assert unpack_data(pack_data(data)) == data

