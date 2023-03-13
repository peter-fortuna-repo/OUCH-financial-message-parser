def stripNulls(data):
    # Several data types are padded to the right with \x00
    while data[-1] == b'\x00':
        data = data[:-1]
    return data

def joinBytes(data):
    joined_data = b''
    for val in data:
        joined_data += val 
    return joined_data

def toLong(data) -> int:
    assert type(data[0]) == bytes
    assert len(data) == 8
    return int.from_bytes(joinBytes(data), byteorder='big')

def toInt(data) -> int:
    assert(type(data[0]) == bytes)
    assert(len(data) == 4)
    return int.from_bytes(joinBytes(data), byteorder='big')

def toShort(data) -> int:
    assert type(data[0]) == bytes
    assert len(data) == 2
    return int.from_bytes(joinBytes(data), byteorder='big')

def toByte(data) -> int:
    assert type(data[0]) == bytes
    assert len(data) == 1
    return int.from_bytes(joinBytes(data), byteorder='big')

def toPrice(data) -> float:
    assert type(data[0]) == bytes
    return float(int.from_bytes(joinBytes(data), byteorder='big'))/1000

def toSignedPrice(data) -> float:
    assert type(data[0]) == bytes
    assert len(data) == 4
    return float(int.from_bytes(joinBytes(data), byteorder='big'))/1000

def toTimestamp(data) -> int:
    # Nanoseconds since midnight
    assert type(data[0]) == bytes
    assert len(data) == 8
    return toLong(data)

def toAlpha(data) -> str:
    assert type(data[0]) == bytes
    data = stripNulls(data)
    return ''.join([chr(byte[0]) for byte in data])

def toUserRefNum(data):
    assert type(data[0]) == bytes
    assert(len(data) == 4)
    return toAlpha(data)