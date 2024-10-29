def func(x):
  f=x * x * x - x * x + 2
  return f


def root(a,b,iterations):
  if func(a)*func(b)>=0:
    print("No roots")
    return
  else:
    c=a
    for i in range(iterations):
      c=(a+b)/2
      if func(c)==0 or (b-a)/2 <= 0.00001:
        print('root is ',c)
        return c
        break
      elif func(c)*func(a)<0:
        b=c
      elif func(c)*func(b)<0:
        a=c
      else:
        print('not follow our assumption')
        break
  
    
a=int(input('enter one extreme point of the function'))
b=int(input('enter another extreme point of the function'))
iter=int(input('enter number of iterations '))
root(a,b,iter)