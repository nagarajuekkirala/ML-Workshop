import streamlit as st
import pickle
import pandas as pd
st.title("Swiggy Delivery Time Prediction")
df = pd.read_csv(r'swiggy_cleaned.csv')
df.dropna(inplace=True)
X = df.copy()
col = ['age', 'ratings', 'weather', 'traffic', 'vehicle_condition',
       'type_of_order', 'type_of_vehicle', 'multiple_deliveries', 'festival',
       'city_type', 'city_name', 'order_day_of_week', 'is_weekend',
       'pickup_time_minutes', 'order_time_hour', 'order_time_of_day',
       'distance']
Age = st.number_input('Enter The Age:',min_value=1,max_value=50)
Rating = st.number_input('Enter The Rating:',min_value=1,max_value=5)
weather = st.selectbox('Wather',X['weather'].unique())
traffic = st.selectbox('traffic',X['traffic'].unique())
vehicle_condition  = st.selectbox('vehicle_condition',X['vehicle_condition'].unique())
type_of_order = st.selectbox('type_of_order',X['type_of_order'].unique())
type_of_vehicle = st.selectbox('type_of_vehicle',X['type_of_vehicle'].unique())
multiple_deliveries= st.number_input('Enter The no of deliveries:',min_value=1,max_value=3)
festival = st.selectbox('festival',X['festival'].unique())
city_type = st.selectbox('city_type',X['city_type'].unique())
city_name = st.selectbox('city_name',X['city_name'].unique())
order_day_of_week = st.selectbox('order_day_of_week',X['order_day_of_week'].unique())
is_weekend =  st.number_input('Is it Weekend:',min_value=1,max_value=3)
pickup_time_minutes =  st.number_input('pickup_time_minutes',min_value=1,max_value=100)
order_time_hour = st.number_input('order_time_hour',min_value=1,max_value=24)
order_time_of_day  = st.selectbox('order_time_of_day ',X['order_time_of_day'].unique())
distance =  st.number_input('distance ',min_value=1,max_value=100 )

with open(r'model.pkl','rb') as file:
    model = pickle.load(file)




data = pd.DataFrame([[Age, 
Rating,
weather,
traffic,
vehicle_condition,
type_of_order,
type_of_vehicle,
multiple_deliveries,
festival,
city_type,
city_name ,
order_day_of_week,
is_weekend,
pickup_time_minutes ,
order_time_hour ,
order_time_of_day,
distance]],columns=col)

result = model.predict(data)[0]

if st.button('Predict'):
    time = result
    st.write(f"The delivery Time is  {time} mins")