from urllib.parse import MAX_CACHE_SIZE
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('LaptopPricePred','rb'))
df = pickle.load(open('Data','rb'))

st.title("""Refurbished Laptop Price Predictor""")
company = st.selectbox('Brand',df['Company'].unique())

type = st.selectbox('Type',df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
ips = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
Cpu_Speed = st.slider('CPU Speed',min_value=1.00,max_value=4.00,step=0.01)
Cpu_Vender = st.selectbox('Cpu Vender',df['Cpu_Vender'].unique())
Cpu_Type = st.selectbox('Cpu Type',df['Cpu_Type'].unique())
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

flash_storage = st.selectbox('Flash Storage(in GB)',[0,16,32,64,128,256,512,])

gpu_brand = st.selectbox('Gpu brand',df['Gpu_brand'].unique())
gpu_type = st.selectbox('Gpu Type',df['Gpu_Type'].unique())
os = st.selectbox('OS',df['OpSys'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([ram,weight,touchscreen,ips,ppi,hdd,ssd,flash_storage])

    query = query.reshape(1,8)
    st.title("The predicted price of this configuration is " + str(int(np.exp(model.predict(query)[0]))*81.48)+ "  rupees !!")