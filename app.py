# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:39:47 2020

@author: shahe
"""

#Import necessary libraries
from flask import Flask, render_template, request, url_for
from flask_cors import cross_origin
import sklearn
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
saved_model = pickle.load(open('flight_gbm_reg.pkl','rb'))

@app.route('/')
@cross_origin()

def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()

def predict():
    if request.method == 'POST':
        
        #Date_of_Journey
        dep_date = request.form['Dep_Time']
        Journey_Day = int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").day)
        Journey_Month = int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").month)
        
        #Departure
        Dep_hour = int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").hour)
        Dep_minute = int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").minute)
        
        #Arrival
        arr_date = request.form['Arrival_Time']
        Arr_hour = int(pd.to_datetime(arr_date,format="%Y-%m-%dT%H:%M").hour)
        Arr_minute = int(pd.to_datetime(arr_date,format="%Y-%m-%dT%H:%M").minute)
        
        #Duration
        Duration_hour = abs(Arr_hour - Dep_hour)
        Duration_minute = abs(Arr_minute - Dep_minute)
        
        #Total Stops
        
        Total_Stops = int(request.form['Total_Stops'])
        
        #Airline
        #Air Asia = 0
        airline = request.form['Airline']
        if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        elif(airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        elif(airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        elif(airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        elif(airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        elif(airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        elif(airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        elif(airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        elif(airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        elif(airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 1
            Trujet = 0
            
        elif(airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 1
            
        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy  = 0
            Trujet = 0
            
        
        #Source
        #Banglore = 0
        source = request.form['Source']
        if(source == 'Delhi'):
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
            
        elif(source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0
            
        elif(source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0
            
        elif(source == 'Chennai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1
            
        else:
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
            
        #Destination
        #Banglore = 0
        destination = request.form['Destination']
        if(destination == 'Cochin'):
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_Kolkata = 0
            Destination_Hyderabad = 0
            
        elif(destination == 'Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_Kolkata = 0
            Destination_Hyderabad = 0
        
        elif(destination == 'Kolkata'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Kolkata = 1
            Destination_Hyderabad = 0
            
        elif(destination == 'Hyderabad'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Kolkata = 0
            Destination_Hyderabad = 1
            
        else:
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Kolkata = 0
            Destination_Hyderabad = 0
            
            
        prediction = saved_model.predict([[
                Total_Stops,
                Air_India,
                GoAir,
                IndiGo,
                Jet_Airways,
                Jet_Airways_Business,
                Multiple_carriers,
                Multiple_carriers_Premium_economy,
                SpiceJet,
                Trujet,
                Vistara,
                Vistara_Premium_economy,
                Source_Chennai,
                Source_Delhi,
                Source_Kolkata,
                Source_Mumbai,
                Destination_Cochin,
                Destination_Delhi,
                Destination_Hyderabad,
                Destination_Kolkata,
                Journey_Day,
                Journey_Month,
                Dep_hour,
                Dep_minute,
                Arr_hour,
                Arr_minute,
                Duration_hour,
                Duration_minute
        ]])
        output = round(prediction[0],2)
        
        return render_template('home.html',prediction_text = "Estimated flight price is ₹{}".format(output))
    
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)

         
    
            
        
            
            






































































































