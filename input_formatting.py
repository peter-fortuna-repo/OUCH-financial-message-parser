def toBytes(input, input_type):
    valid_input_types = {'detect','bytes','hex_str','binary_str','decimal_str',
                         'byte_list','hex_str_list','binary_str_list',
                         'decimal_str_list','int_list'}
    assert input_type in valid_input_types
    if input_type == 'detect':
        input_type = detectInputType(input)
    
    if input_type == 'bytes': return bytesToByteList(input)
    elif input_type == 'hex_str': return hexStrToByteList(input)
    elif input_type == 'binary_str': return binaryStrToByteList(input)
    elif input_type == 'byte_list': return formatByteList(input)
    elif input_type == 'hex_str_list': return hexStrListToByteList(input)
    elif input_type == 'binary_str_list': return binaryStrListToByteList(input)
    elif input_type == 'int_list': return intListToByteList(input)
    else: raise TypeError("Invalid input. Must be of type bytes, str,"
                          "List[bytes], List[str], or List[int]")
    
    

def detectInputType(input):
    # Check input type
    input_type = type(input)
    if input_type == bytes:
        return 'bytes'

    if input_type != str and input_type != list:
        return "error"

    type_first_value = type(input[0])
    if type_first_value == bytes:
        return 'byte_list'
    elif type_first_value == int:
        return 'int_list'

    if type_first_value != str:
        return "error"

    # Check v
    sample = input[:1000].replace('\n','').replace(' ','').replace('\t','')

    values = set()
    for val in sample:
        values.add(val)
    
    if values.issubset({'0', '1'}):
        if input_type != list:
            return 'binary_str'
        else:
            return 'binary_str_list'
    
    elif values.issubset({'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}):
        if input_type != list:
            return 'hex_str'
        else:
            return 'hex_str_list'

    else:
        return 'error'

def bytesToByteList(input):
    return [byte.to_bytes(1,byteorder='big') for byte in input]

def hexStrToByteList(input):
    byte_list = []
    input = input.replace(' ','').replace('\n','').replace('\t','')
    for i in range(0,len(input),2):
        byte_list.append(int(input[i:i+2],base=16).to_bytes(1,byteorder='big'))
    return byte_list

def binaryStrToByteList(input):
    byte_list = []
    for i in range(0,len(input),8):
        byte_list.append(int(input[i:i+8],base=2).to_bytes(1,byteorder='big'))
    return byte_list

def formatByteList(input):
    for byte in input:
        assert len(byte == 1), "Byte list must contain bytes of len 1"
    return input

def hexStrListToByteList(input):
    assert len(input[0]) == 2
    return [int(val,base=16).to_bytes(1,byteorder='big') for val in input]

def binaryStrListToByteList(input):
    return [int(val,base=2).to_bytes(1,byteorder='big') for val in input]

def intListToByteList(input):
    return [val.to_bytes(1,byteorder='big') for val in input]