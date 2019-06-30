from zipline.api import order, record, symbol

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))

#from zipline.api import attach_pipeline, pipeline_output
#from quantopian.pipeline import Pipeline
#from quantopian.pipeline.data.builtin  import USEquityPricing 
#from quantopian.pipeline.factors import SimpleMovingAverage

# def initialize(context):
        
#     schedule_function(rebalance,date_rules.week_start(days_offset=0),time_rules.market_open(hours=0, minutes=30))
#     schedule_function(rebalance1,date_rules.week_end(days_offset=0),time_rules.market_open(hours=0, minutes=30))
    
    
#     pipe = Pipeline()
#     attach_pipeline(pipe, name='Tyler Pipeline')
   
#     sma_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
#     sma_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)
        
#     prices_under_5 = (sma_10 < 10)
    
#     pipe.add(sma_10, 'sma_10')
#     pipe.add(sma_30, 'sma_30')
    
#     pipe.set_screen(prices_under_5)
   
   
# def before_trading_start(context,data):
#     results = pipeline_output('Tyler Pipeline')
#     context.pipeline_results = results.sort_values('sma_10', ascending=False).iloc[:1].index
       
#     print results.head(1)

# def rebalance(context,data):   
#      for security in context.pipeline_results:
#             order_target_percent(security, 1.00)
            
# def rebalance1(context,data):   
#      for security in data:
#             order_target_percent(security, 0.00)