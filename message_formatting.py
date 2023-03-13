import field_formatting as f
import optional_appendage_formatting as oa

# Inbound Messages
def enter_order(bytes: list):
    msg_end = 47 + f.toShort(bytes[45:47])
    msg = [f.toAlpha(bytes[:1]),
            f.toUserRefNum(bytes[1:5]),
            f.toAlpha(bytes[5:6]),
            f.toInt(bytes[6:10]),
            f.toAlpha(bytes[10:18]),
            f.toPrice(bytes[18:26]),
            f.toAlpha(bytes[26:27]),
            f.toAlpha(bytes[27:28]),
            f.toAlpha(bytes[28:29]),
            f.toAlpha(bytes[29:30]),
            f.toAlpha(bytes[30:31]),
            f.toAlpha(bytes[31:45]),
            f.toShort(bytes[45:47]),
            oa.getOptionalAppendage(bytes[45:msg_end])]
    del bytes[:msg_end]
    return msg

def replace_order_request(bytes: list):
    msg_end = 40 + f.toShort(bytes[38:40])
    msg = [f.toAlpha(bytes[:1]),
            f.toUserRefNum(bytes[1:5]),
            f.toUserRefNum(bytes[5:9]),
            f.toInt(bytes[9:13]),
            f.toPrice(bytes[13:21]),
            f.toAlpha(bytes[21:22]),
            f.toAlpha(bytes[22:23]),
            f.toAlpha(bytes[23:24]),
            f.toAlpha(bytes[24:38]),
            f.toShort(bytes[38:40]),
            oa.getOptionalAppendage(bytes[38:msg_end])]
    del bytes[:msg_end]
    return msg

def cancel_order_request(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toUserRefNum(bytes[1:5]),
            f.toInt(bytes[5:9])]
    del bytes[:9]
    return msg
     
def modify_order_request(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toUserRefNum(bytes[1:5]),
            f.toAlpha(bytes[5:6]),
            f.toInt(bytes[6:10])]
    del bytes[:10]
    return msg

def account_query_request(bytes: list):
    msg = [f.toAlpha(bytes[:1])]
    del bytes[:1]
    return msg

# Outbound messages
def system_event(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toAlpha(bytes[9:10])]
    del bytes[:10]
    return msg

def order_accepted(bytes: list):
    msg_end = 64 + f.toShort(bytes[62:64])
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toAlpha(bytes[13:14]),
            f.toInt(bytes[14:18]),
            f.toAlpha(bytes[18:26]),
            f.toPrice(bytes[26:34]),
            f.toAlpha(bytes[34:35]),
            f.toAlpha(bytes[35:36]),
            f.toLong(bytes[36:44]),
            f.toAlpha(bytes[44:45]),
            f.toAlpha(bytes[45:46]),
            f.toAlpha(bytes[46:47]),
            f.toAlpha(bytes[47:48]),
            f.toAlpha(bytes[48:62]),
            f.toShort(bytes[62:64]),
            oa.toOptionalAppendage(bytes[62:msg_end])]
    del bytes[:msg_end]
    return msg

def order_replaced(bytes: list):
    msg_end = 68 + f.toShort(bytes[66:68])
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toUserRefNum(bytes[13:17]),
            f.toAlpha(bytes[17:18]),
            f.toInt(bytes[18:22]),
            f.toAlpha(bytes[22:30]),
            f.toPrice(bytes[30:38]),
            f.toAlpha(bytes[38:39]),
            f.toAlpha(bytes[39:40]),
            f.toLong(bytes[40:48]),
            f.toAlpha(bytes[49:49]),
            f.toAlpha(bytes[49:50]),
            f.toAlpha(bytes[50:51]),
            f.toAlpha(bytes[51:52]),
            f.toAlpha(bytes[52:66]),
            f.toShort(bytes[66:68]),
            oa.toOptionalAppendage(bytes[66:msg_end])]
    del bytes[:msg_end]
    return msg

def order_canceled(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toInt(bytes[13:17]),
            f.toByte(bytes[17:18])]
    del bytes[:18]
    return msg

def aiq_canceled(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toInt(bytes[13:17]),
            f.toByte(bytes[17:18]),
            f.toInt(bytes[18:22]),
            f.toPrice(bytes[22:30]),
            f.toAlpha(bytes[30:31])] 
    del bytes[:31]
    return msg

def order_executed(bytes: list):
    msg_end = 36 + f.toShort(bytes[34:36])
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toInt(bytes[13:17]),
            f.toPrice(bytes[17:25]),
            f.toAlpha(bytes[25:26]),
            f.toLong(bytes[26:34]),
            f.toShort(bytes[34:36]),
            oa.toOptionalAppendage(bytes[34:msg_end])]
    del bytes[:msg_end]
    return msg

def broken_trade(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toLong(bytes[13:21]),
            f.toAlpha(bytes[21:22]),
            f.toAlpha(bytes[22:36])]
    del bytes[:36]
    return msg

def trade_correction(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toInt(bytes[13:17]),
            f.toPrice(bytes[17:25]),
            f.toAlpha(bytes[25:26]),
            f.toLong(bytes[26:34]),
            f.toAlpha(bytes[34:35]),
            f.toAlpha(bytes[35:49])]
    del bytes[:49]
    return msg

def rejected(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toShort(bytes[13:15]),
            f.toAlpha(bytes[15:29])]
    del bytes[:29]
    return msg

def cancel_pending(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13])]
    del bytes[:13]
    return msg

def cancel_reject(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13])]
    del bytes[:13]
    return msg

def order_priority_update(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toAlpha(bytes[13:21]),
            f.toAlpha(bytes[21:22]),
            f.toLong(bytes[22:30])]
    del bytes[:30]
    return msg

def order_modified(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toAlpha(bytes[13:12]),
            f.toInt(bytes[14:18])]
    del bytes[:18]
    return msg

def order_restated(bytes: list):
    msg_end =  16 + f.toShort(bytes[14:16])
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13]),
            f.toAlpha(bytes[13:14]),
            f.toShort(bytes[14:16]),
            oa.toOptionalAppendage(bytes[14:msg_end])]
    del bytes[:msg_end]
    return msg
            

def account_query_response(bytes: list):
    msg = [f.toAlpha(bytes[:1]),
            f.toTimestamp(bytes[1:9]),
            f.toUserRefNum(bytes[9:13])]
    del bytes[:13]
    return msg