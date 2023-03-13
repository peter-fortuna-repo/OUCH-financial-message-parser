from Cache import Cache
import input_formatting as inf
import field_formatting as f
import message_formatting as mf

class Parser:
    cache = Cache()

    def parse(self, input, input_type='detect'):
        """"""
        byte_list = inf.toBytes(input, input_type)
        while len(byte_list) > 0:
            type = chr(byte_list[0][0])
            if type == 'O':  
                message = mf.enter_order(byte_list)
                self.cache.addEnterOrder(message)
            elif type == 'U': 
                message = mf.replace_order_request(byte_list)
                self.cache.addReplaceOrderRequest(message)
            elif type == 'X': 
                message = mf.cancel_order_request(byte_list)
                self.cache.addCancelOrderRequest(message)
            elif type == 'M': 
                message = mf.modify_order_request(byte_list)
                self.cache.addModifyOrderRequest(message)
            elif type == 'Q': 
                message = mf.account_query_request(byte_list)
                self.cache.addAccountQueryRequest(message)
            elif type == 'S': 
                message = mf.system_event(byte_list)
                self.cache.addSystemEvent(message)
            elif type == 'A': 
                message = mf.order_accepted(byte_list)
                self.cache.addOrderAccepted(message)
            elif type == 'U': 
                message = mf.order_replaced(byte_list)
                self.cache.addOrderReplaced(message)
            elif type == 'C': 
                message = mf.order_canceled(byte_list)
                self.cache.addOrderCanceled(message)
            elif type == 'D': 
                message = mf.aiq_canceled(byte_list)
                self.cache.addAiqCanceled(message)
            elif type == 'E': 
                message = mf.order_executed(byte_list)
                self.cache.addOrderExecuted(message)
            elif type == 'B': 
                message = mf.broken_trade(byte_list)
                self.cache.addBrokenTrade(message)
            elif type == 'F': 
                message = mf.trade_correction(byte_list)
                self.cache.addTradeCorrection(message)
            elif type == 'J': 
                message = mf.rejected(byte_list)
                self.cache.addRejected(message)
            elif type == 'P': 
                message = mf.cancel_pending(byte_list)
                self.cache.addCancelPending(message)
            elif type == 'I': 
                message = mf.cancel_reject(byte_list)
                self.cache.addCancelReject(message)
            elif type == 'T': 
                message = mf.order_priority_update(byte_list)
                self.cache.addOrderPriorityUpdate(message)
            elif type == 'M': 
                message = mf.order_modified(byte_list)
                self.cache.addOrderModified(message)
            elif type == 'R': 
                message = mf.order_restated(byte_list)
                self.cache.addOrderRestated(message)
            elif type == 'Q': 
                message = mf.account_query_response(byte_list)
                self.cache.addAccountQueryResponse(message)
            else:
                del byte_list[0]

    def reset(self):
        """Delete all messages"""
        self.cache = Cache()

    def getMessages(self):
        """Return all messages in python dictionary"""
        return self.cache.toDict()