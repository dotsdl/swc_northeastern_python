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
