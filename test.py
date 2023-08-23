from singltions.path_formulator import LinearPathForm


lpf = LinearPathForm([0,0] , [50,100] , 0.5 , lambda p: print(p) , loop=True)


prop = vars(lpf)
word= 'ca'

