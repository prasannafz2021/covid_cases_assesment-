import pandas as pd
# convert csv data into dataframe by using pandas
df=pd.read_csv(r'C:\Users\kanna\Downloads\worldometer_coronavirus_daily_data.csv')
#get max values group by country 
da=(df.groupby('country').apply(lambda x: x[x['active_cases'] == x['active_cases'].max()]))
# locking wanted columns 
df=da.loc[:,['date','country','active_cases']]

df['date'] = pd.to_datetime(df['date'])
df['peak_month']=df['date'].dt.month_name(locale = 'English')
df['peak_year']=df['date'].dt.year
del df['date']

# convert dataframe into csv data 
df.to_csv(r'C:\Users\kanna\Downloads\new_data.csv', index=False)
