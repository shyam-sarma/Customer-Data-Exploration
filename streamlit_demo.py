from datetime import datetime
from turtle import color
import streamlit as st
import pandas as pd
import altair as alt
import datetime

header= st.container()
dataset = st.container()
visuals  = st.container()

with header:
    st.title("Welcome To My First Streamlit App")
    st.write("This is my First Streamlit App And I am absolutely loving it so far. The intention of this project is to document my learnings as I go, so that I will always have an App that I can go back to and quickly recap what I learnt about Streamlit")



with dataset:
    st.header("Customer Data Explorer")
    st.write("Let us view the data we are dealing with")
    data1 = pd.read_csv("data/customers.csv")
    st.dataframe(data1)
    data1["free_account_created_at"] = pd.to_datetime(data1["free_account_created_at"])
    

    


with visuals: 
    st.header( "Lets explore some awesome streamlit charting ")

    st.subheader("Customer Distribution Across Segments")
    st.bar_chart(data1["segment"].value_counts(),use_container_width=True)
    st.markdown("This chart tell's us how the customers are distributed across Marketing Segments")

    # create datetime objects for min_date and max_date for date input selector
    min_date = datetime.datetime(2017,1,30)
    max_date = datetime.datetime(2019,4,28)
    #Inputs for date range selector     
    date_range= st.date_input("Select a date range to view account session activity across marketing segments for that date range",(min_date, max_date),min_value= min_date,max_value=max_date)
    
    #date selector returns tuple with ints based on users input, we have to change it into date time to filter out data frame
    start= pd.to_datetime(date_range[0])
    end= pd.to_datetime(date_range[1])

    #filter out the dataframe based on input dates selected
    data2 = data1[(data1["free_account_created_at"]>=start) & (data1["free_account_created_at"]<=end)]
    
    #pass the data to an altair chart for plotting
    c = alt.Chart(data2).mark_line().encode(x= 'free_account_created_at',y='session_count',color='segment')
    st.altair_chart(c,use_container_width=True)