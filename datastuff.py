import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt

def fahrenheit_to_celsius(temp):
    """Convert temperature in fahrenheit to temperature in celsius.
    
    Parameters
    ----------
    temp : float or array_like
        Temperature(s) in fahrenheit.
    
    Returns
    -------
    float or array_like
        Temperature(s) in celsius.
    
    """
    return (temp - 32) * 5/9


def analyze(data):
    """Return panel plot of mosquito population vs. temperature, rainfall.
    
    Also prints t-values for temperature and rainfall.
    
    Panel plot gives:
        1. comparison of modeled values of mosquito population
           vs. measured values
        2. mosquito population vs. average temperature
        3. mosquito population vs. total rainfall
        
    Parameters
    ----------
    data : DataFrame
        DataFrame giving columns for `temperature`, `rainfall`, 
        and `mosquitos`
        
    Returns
    -------
    Figure
        :mod:`matplotlib.figure.Figure` object giving panel plot.
    
    """
    # perform fit
    regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    print(regr_results.tvalues)
    
    fig = plt.figure(figsize=(6, 9))

    # plot predicted vs. measured mosquito populations from fitted model 
    ax0 = fig.add_subplot(3, 1, 1)

    parameters = regr_results.params
    predicted = (parameters['Intercept'] + 
                 parameters['temperature'] * data['temperature'] + 
                 parameters['rainfall'] * data['rainfall'])

    ax0.plot(predicted, data['mosquitos'], 'gd')

    ax0.set_xlabel('predicted mosquito population')
    ax0.set_ylabel('measured mosquito population')
    
    # plot mosquitos vs. temperature
    ax1 = fig.add_subplot(3, 1, 2)

    ax1.plot(data['temperature'], data['mosquitos'], 'ro')
    ax1.set_xlabel('temperature')
    ax1.set_ylabel('mosquitos')

    # plot mosquitos vs. rainfall
    ax2 = fig.add_subplot(3, 1, 3)

    ax2.plot(data['rainfall'], data['mosquitos'], 'bs')
    ax2.set_xlabel('rainfall')
    ax2.set_ylabel('mosquitos')
    
    # adjust layout of axes according to label placement
    plt.tight_layout()
    
    return fig
