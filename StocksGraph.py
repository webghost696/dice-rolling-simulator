import yfinance as yf
import datetime
from bokeh.plotting import figure,show,output_file

#Scraping the data of the stock from yfinance
start=datetime.datetime(2023,12,1) #change the range of date as you want
end=datetime.datetime(2023,12,30)
df=yf.download('AAPL',start=start, end=end) #here I have used 'AAPL' as an example stock token, you can choose anything


#Initiating the graph
p=figure(x_axis_type='datetime',width=1000, height=300, sizing_mode='scale_width')
p.title.text='Candlestick Chart'
p.grid.grid_line_alpha=0.3
hours_12=12*60*60*1000 #conversion of 12 hours into milli-seconds to use it in the plotting function

def inc_dec(c,o):
    if c>o:
        value="Increase"
    elif c<o:
        value="Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["Middle"]=(df.Close+df.Open)/2
df["Height"]=abs(df.Close-df.Open)


#plotting the high and low candles of red and green as per the scraped data
p.segment(df.index,df.High,df.index,df.Low, color="Black")
p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"],
         hours_12, df.Height[df.Status=="Increase"], fill_color="#00FF7F", line_color="Black")
p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"],
         hours_12, df.Height[df.Status=="Decrease"], fill_color="Red", line_color="Black")

output_file("CS.html")
show(p)
