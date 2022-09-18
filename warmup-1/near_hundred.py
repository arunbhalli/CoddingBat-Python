'''

Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False

'''

def near_hundred(n):
  if ((n <=100) and (100-n <=10)):
    return True 
  elif ((n > 100) and (n-100 <= 10)):
    return True
  elif ((n <100) and (100-n > 10)):
    return False
  elif ((n <= 200) and (200-n <=10)):
    return True
  elif ((n <200) and (200-n > 10)):
    return False
  elif ((n > 200) and (n-200 <= 10)):
    return True
  else:
      return False
