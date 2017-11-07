#Expected Return Calculator
def expret(a,b,w):
  w = 1- w
  print((a[0]*w) + (b[0]*w))

#Volatility of Portfolio Calculator  
def vol(y,x,corr):
  a = (y[2]**2) * (y[1] ** 2)
  b = (x[2] **2) * (x[1] ** 2)
  var = a + b  + (2 *(y[2] * x[2]) * corr * y[1] * x[1])
  print(var ** 0.5)
