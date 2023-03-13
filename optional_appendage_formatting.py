import field_formatting as f

def toOptionalAppendage(message):
    assert type(message[0]) == bytes
    msg_len = f.toShort(message[:2])
    i = 2
    fields = []
    while msg_len > 0:
        assert i < len(message), "Invalid input in optional appendage"
        field_type = f.toByte(message[i:i+1])
        field_len = getFieldLength(field_type)
        field = getField(message, i, field_type, field_len)
        fields.append(field)
        i += field_len
        msg_len -= field_len
    return fields

def getField(message, i: int, field_type: int, field_len: int):
        if field_type == 1:
            return ("SecondaryOrdRefNum",f.toLong(message[i:i+field_len]))
        elif field_type == 2:
            return ("Firm",f.toAlpha(message[i:i+field_len]))
        elif field_type == 3:
            return ("MinQty",f.toInt(message[i:i+field_len]))
        elif field_type == 4:
            return ("CustomerType", f.toAlpha(message[i:i+field_len]))
        elif field_type == 5:
            return ("MaxFloor",f.toInt(message[i:i+field_len]))
        elif field_type == 6:
            return ("PriceType",f.toAlpha(message[i:i+field_len]))
        elif field_type == 7:
            return ("PegOffset",f.toSignedPrice(message[i:i+field_len]))
        elif field_type == 9:
            return ("DiscretionPrice",f.toPrice(message[i:i+field_len]))
        elif field_type == 10:
            return ("DiscretionPriceType",f.toAlpha(message[i:i+field_len]))
        elif field_type == 11:
            return ("DiscretionPegOffset",f.toSignedPrice(message[i:i+field_len]))
        elif field_type == 12:
            return ("PostOnly",f.toAlpha(message[i:i+field_len]))
        elif field_type == 13:
            return ("RandomReserves",f.toInt(message[i:i+field_len]))
        elif field_type == 14:
            return ("Route",f.toAlpha(message[i:i+field_len]))
        elif field_type == 15:
            return ("ExpireTime",f.toInt(message[i:i+field_len]))
        elif field_type == 16:
            return ("TradeNow",f.toAlpha(message[i:i+field_len]))
        elif field_type == 17:
            return ("HandleInst",f.toAlpha(message[i:i+field_len]))
        elif field_type == 18:
            return ("BBO Weight Indicator",f.toAlpha(message[i:i+field_len]))
        elif field_type == 19:
            return ("Reference Price",f.toPrice(message[i:i+field_len]))
        elif field_type == 20:
            return ("Reference Price Type",f.toAlpha(message[i:i+field_len]))
        elif field_type == 22:
            return ("Display Quantity",f.toInt(message[i:i+field_len]))
        elif field_type == 23:
            return ("Display Price",f.toPrice(message[i:i+field_len]))
        elif field_type == 24:
            return ("Group ID",f.toShort(message[i:i+field_len]))
        elif field_type == 25:
            return ("Shares Located",f.toAlpha(message[i:i+field_len]))
        else:
            raise ValueError("Optional field contains invalid field type") 

def getFieldLength(field_type: int):
        if field_type == 1:
            return 16
        elif field_type == 2:
            return 8
        elif field_type == 3:
            return 8
        elif field_type == 4:
            return 2
        elif field_type == 5:
            return 8
        elif field_type == 6:
            return 2
        elif field_type == 7:
            return 8
        elif field_type == 9:
            return 16
        elif field_type == 10:
            return 2
        elif field_type == 11:
            return 8
        elif field_type == 12:
            return 2
        elif field_type == 13:
            return 8
        elif field_type == 14:
            return 8
        elif field_type == 15:
            return 8
        elif field_type == 16:
            return 2
        elif field_type == 17:
            return 2
        elif field_type == 18:
            return 2
        elif field_type == 19:
            return 16
        elif field_type == 20:
            return 2
        elif field_type == 22:
            return 8
        elif field_type == 23:
            return 16
        elif field_type == 24:
            return 4
        elif field_type == 25:
            return 2
        else:
            raise ValueError("Optional field contains invalid field type")