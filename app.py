import streamlit as st
import datetime
import pickle 

date_time = datetime.datetime.now() 

with open('Car Price Predictor Model.pkl','rb') as pkl:
    train_model = pickle.load(pkl)

def predict(present_price,km_driven,fuel_type,seller_type,transmission_type,car_owner,year):
    presentprice = present_price
    km = km_driven
    fuel = 0 if fuel_type == 'CNG' else 1 if fuel_type == 'Diesel' else 2
    seller = 0 if seller_type == 'Dealer' else 1
    trans = 0 if transmission_type == 'Automatic' else 1
    owner = car_owner
    years = date_time.year - year
    
    prediction = train_model.predict([[presentprice,km,fuel,seller,trans,owner,years]])
    return prediction
    

def main():
    html_temp = """
    <div style = "background-color:black">
    <h1 style = "color:white;text-align:center">Car Price Predictor</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    present_price = st.number_input("What is the present price of the car in lakh?",2.5,25.0,step = 1.0)
    km_driven = st.number_input("How much distance completed by car in kilometer?",500,5000000,step=100)
    fuel_type = st.selectbox('What is the fuel type of the car?',('Diesel','Petrol','CNG'))
    seller_type = st.selectbox('Are you Dealer or Individual?',('Individual','Dealer'))
    transmission_type = st.selectbox('What is the transmission type?',('Manual','Automatic'))
    car_owner = st.slider('No of owner that car previously had?',0,3)
    year = st.slider("In which year car was purchased?",2003,date_time.year)
    button = st.button('Predict')
    
    if button:
        result = predict(present_price,km_driven,fuel_type,seller_type,transmission_type,car_owner,year)
        st.success(f'You can sell your car for {result} lakh')
    
if __name__ == '__main__':
    main()    