# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 12:20:29 2022

@author: Archana
"""
#def linear_regression_wrapper(d={}):


from linear_regression_model import linear_regression

import pandas as pd
import json
import os
import pickle
from matplotlib import pyplot as plt
import seaborn as sns


def linear_regression_outer(json_input_file = [] #json input path
                            ):
    
    try:
               
        #Load json
        with open(json_input_file) as f:
            json_input = json.load(f)
        
        #read csv
        input_file_path = json_input['input_file_path']
        data = pd.read_csv(input_file_path[0])
        
        #loading parameters
        num_cols = json_input['numeric_cols']
        cat_cols = json_input['cat_cols']
        target = json_input['target']
        
        #call linear_regression_model
        output = linear_regression(data,
                                   num_cols,
                                   cat_cols,
                                   target)
        
       
        #generate output folder 
        output_file_path = json_input['output_file_path'][0]
        path = os.getcwd() + output_file_path[0]
        os.mkdir(path)        
        
        
        #generate csv with y_actual and y_pred
        temp = {'Y_actual': output['y_actual'], 'Y_predicted': output['y_predict']}
        df = pd.DataFrame(data=temp).reset_index(drop=True)
        df = df.assign(Index=range(len(df))).set_index('Index')
        df.to_csv(path+'/actual Vs predicted.csv')
        
        #generate performance metrics of model
        df1 = pd.DataFrame([output['model_performance']]).T.reset_index()
        df1 = df1.set_index('index').rename_axis('Metrices')
        df1.columns=['Scores']
        df1.to_csv(path+'/model_performance.csv')
        
        #generate model in pkl format
        with open(path+'/model.pkl', 'wb') as files:
            pickle.dump(output['model'], files)
        
        
        #Dist Plot
        plt.figure(figsize = (10,10))
        sns.distplot(output['y_actual']- output['y_predict'],
                     kde=True, color="g", )
       # plt.rcParams["font.size"] = "45"
        plt.rc('axes', labelsize=50)
        plt.savefig(path+'/dist_plot.png')
        plt.show()
        
        #Parity plot - Scatter plot
        plt.figure(figsize = (10,10))
        lineStart = output['y_actual'].min() 
        lineEnd = output['y_predict'].max()  
        plt.scatter(output['y_actual'], output['y_predict'], alpha = 0.5, color = "red")
        plt.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
        plt.title("Actual vs Pred (Testing set)")
        plt.xlabel("Y_Actual")
        plt.ylabel("Y_Predicted")
        plt.rc('axes', labelsize=50)
        plt.savefig(path+'/scatter_plot.png')
        plt.show()

        #Trend Plot
        randomlist = []
        for i in range(0,len(output['y_actual'])):
            randomlist.append(i)
        plt.figure(figsize = (10,10))
        plt.plot(randomlist,output['y_actual'],'r')
        plt.plot(randomlist,output['y_predict'],'g')
        plt.savefig(path+'/trend_plot.png')
        plt.show()

        #Correlation heatmap
        plt.figure(figsize = (30,24))
        sns.heatmap(data.corr(), annot = True, cmap = "RdYlGn")
        plt.savefig(path+'/corr_heatmap.png')
        plt.show()
        
        
    except:
        print("No idea what comes here")  
        
    
    
