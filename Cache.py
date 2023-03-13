class Cache:
    # Inbound Messages
    enter_orders = [['Type','UserRefNum','Side','Quantity','Symbol','Price',
    'Time In Force','Display','Capacity','InterMarket Sweep Eligibility',
    'CrossType','ClOrdID','Appendage Length','Optional Appendage']]
    replace_order_requests = [['Type','OrigUserRefNum','UserRefNum','Quantity',
    'Price','Time In Force','Display','InterMarket Sweep Eligibility',
    'ClOrdID','Appendage Length','Optional Appendage']]
    cancel_order_requests = [['Type','UserRefNum','Quantity']]
    modify_order_requests = [['Type','UserRefNum','Side','Quantity']]
    account_query_requests = [['Type']]

    # Outbound Messages
    system_events = [['Type','Timestamp','Event Code']]
    order_accepteds = [['Type','Timestamp','UesrRefNum','Side','Quantity',
    'Symbol','Price','Time In Force','Display','Order Reference Number',
    'Capacity','InterMarket Sweep Eligibility','CrossType','Order State',
    'ClOrdID','Appendage Length','Optional Appendage']]
    order_replaceds = [['Type','Timestamp','OrigUserRefNum','UserRefNum','Side',
    'Quantity','Symbol','Price','Time In Force','Display',
    'Order Reference Number','Capacity','InterMarket Sweep Eligibility',
    'CrossType','Order State','ClOrdID','Appendage Length',
    'Optional Appendage']]
    order_canceleds = [['Type','Timestamp','UserRefNum','Quantity','Reason']]
    aiq_canceleds = [['Type','Timestamp','UserRefNum','Decrement Shares',
    'Reason','Quantity prevented from trading','Execution Price',
    'Liquidity Flag']]
    order_executeds = [['Type','Timestamp','UserRefNum','Quantity','Price',
    'Liquidity Flag','Match Number','Appendage Length','Optional Appendage']]
    broken_trades = [['Type','Timestamp','UserRefNum','Match Number','Reason',
    'ClOrdID']]
    trade_corrections = [['Type','Timestamp','UserRefNum','Quantity','Price',
    'Liquidity Flag','Match Number','Reason','ClOrdID']]
    rejecteds = [['Type','Timestamp','UserRefNum','Reason','ClOrdID']]
    cancel_pendings = [['Type','Timestamp','UserRefNum']]
    cancel_rejects = [['Type','Timestamp','UserRefNum']]
    order_priority_updates = [['Type','Timestamp','UserRefNum','Price',
    'Display', 'Order Reference Number']]
    order_modifieds = [['Type','Timestamp','UserRefNum','Side','Quantity']]
    order_restateds = [['Type','Timestamp','UserRefNum','Reason', 
    'Appendage Length','Optional Appendage']]
    account_query_responses = [['Type','Timestamp','NextUserRefNum']]

    # ToDo: Add getter and setter functions with assertions?
    def addEnterOrder(self, message):
        self.enter_orders.append(message)
    
    def addReplaceOrderRequest(self, message):
        self.replace_order_requests.append(message)
    
    def addCancelOrderRequest(self, message):
        self.cancel_order_requests.append(message)

    def addModifyOrderRequest(self, message):
        self.modify_order_requests.append(message)

    def addAccountQueryRequest(self, message):
        self.account_query_requests.append(message)

    def addSystemEvent(self, message):
        self.system_events.append(message)

    def addOrderAccepted(self, message):
        self.order_accepteds.append(message)

    def addOrderReplaced(self, message):
        self.order_replaceds.append(message)

    def addAiqCanceled(self, message):
        self.aiq_canceleds.append(message)

    def addOrderExecuted(self, message):
        self.order_executeds.append(message)

    def addBrokenTrade(self, message):
        self.broken_trades.append(message)

    def addTradeCorrection(self, message):
        self.trade_corrections.append(message)

    def addRejected(self, message):
        self.rejecteds.append(message)

    def addCancelPending(self, message):
        self.cancel_pendings.append(message)

    def addCancelReject(self, message):
        self.cancel_rejects.append(message)

    def addOrderPriorityUpdate(self, message):
        self.order_priority_updates.append(message)

    def addOrderModified(self, message):
        self.order_modifieds.append(message)

    def addOrderRestated(self, message):
        self.order_restateds.append(message)

    def addAccountQueryResponse(self, message):
        self.account_query_responses.append(message)

    def toDict(self):
        contents = dict()
        contents["Enter Order"] = self.enter_orders
        contents["Replace Order Request"] = self.replace_order_requests
        contents["Cancel Order Request"] = self.cancel_order_requests
        contents["Modify Order Request"] = self.modify_order_requests
        contents["Account Query Request"] = self.account_query_requests
        contents["System Event"] = self.system_events
        contents["Order Accepted"] = self.order_accepteds
        contents["Order Replaced"] = self.order_replaceds
        contents["Order Canceled"] = self.order_canceleds
        contents["AIQ Canceled"] = self.aiq_canceleds
        contents["Order Executed"] = self.order_executeds
        contents["Broken Trade"] = self.broken_trades
        contents["Trade Correction"] = self.trade_corrections
        contents["Rejected"] = self.rejecteds
        contents["Cancel Pending"] = self.cancel_pendings
        contents["Cancel Reject"] = self.cancel_rejects
        contents["Order Priority Update"] = self.order_priority_updates
        contents["Order Modified"] = self.order_modifieds
        contents["Order Restated"] = self.order_restateds
        contents["Account Query Response"] = self.account_query_responses
        
        return contents