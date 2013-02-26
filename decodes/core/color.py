import colorsys

class Color():
    """
    a simple color class
    """
    
    def __init__(self, a=None, b=None, c=None):
        """Color constructor
        
            :param a: First color value (between 0.0 and 1.0). Defaults to 0.5
            :type a: float
            :param b: Second color value (between 0.0 and 1.0). Defaults to 0.5
            :type b: float
            :param c: Third color value (between 0.0 and 1.0). Defaults to 0.5
            :type c: float
            :result: Color object.
            :rtype: Color
        """
        if a is None : self.r,self.g,self.b = 0.5,0.5,0.5
        elif b is None or c is None : 
            try: 
                self.r,self.g,self.b = a.r,a.g,a.b
            except:
                try: 
                    self.r,self.g,self.b = a.R/255.0,a.G/255.0,a.B/255.0
                except:
                    self.r,self.g,self.b = a,a,a
        else :
            self.r = a
            self.g = b
            self.b = c
        
    @staticmethod
    def RGB(r,g,b):
        """Creates a color object from RGB values.
        
            :param r: R color value (between 0.0 and 1.0). 
            :type r: float
            :param g: G color value (between 0.0 and 1.0). 
            :type g: float
            :param b: B color value (between 0.0 and 1.0). 
            :type b: float
            :result: Color object.
            :rtype: Color
        """
        return Color(r,g,b)
    
    @staticmethod
    def HSB(h,s=1,b=1):
        """Creates a color object from HSB values.
        
            :param h: H color value (between 0.0 and 1.0). 
            :type h: float
            :param s: S color value (between 0.0 and 1.0). Defaults to 1
            :type s: float
            :param b: B color value (between 0.0 and 1.0). Defaults to 1
            :type b: float
            :result: Color object.
            :rtype: Color
        """
        clr = colorsys.hsv_to_rgb(h,s,b)
        #print clr[0],clr[1],clr[2]
        return Color(clr[0],clr[1],clr[2])
        
    @staticmethod
    def interpolate(c0,c1,t=0.5):
        """Returns a new color interpolated from two Color objects.
        
            :param c0: First Color object
            :type c0: Color
            :param c1: Second Color object
            :type c1: Color
            :param t: Interpolation value (between 0.0 and 1.0). Defaults to 0.5
            :type t: float
            :result: Interpolated Color object.
            :rtype: Color
        """
        r = (1-t) * c0.r + t * c1.r
        g = (1-t) * c0.g + t * c1.g
        b = (1-t) * c0.b + t * c1.b
        return Color(r,g,b)
        
    def __repr__(self):
        return "color[{0},{1},{2}]".format(self.r,self.g,self.b)