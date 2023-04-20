
import matplotlib.pyplot as plt
import numpy as np
def gen_normal(mean=10, sd=2):
    """Generate 20 points normally distributed
    Keyword arguments:
    mean -- the distribution average (default 10.0)
    sd   -- the distribution standard deviation (default 1.0)
    Return Value
    A triple incl (mean, sd, and data distribution)
    """
    assert sd>0, "Standard Deviation must be > 0"
    dat = np.random.normal(mean, sd, 20)
    return [mean, sd, dat]

def gen_normal2(mean=25, sd=5):
    """Generate 20 points normally distributed
    Keyword arguments:
    mean -- the distribution average (default 10.0)
    sd   -- the distribution standard deviation (default 1.0)
    Return Value
    A triple incl (mean, sd, and data distribution)
    """
    assert sd>0, "Standard Deviation must be > 0"
    dat = np.random.normal(mean, sd, 20)
    return [mean, sd, dat]

def gen_subplot(sp, d1, d2):
    """Generate one of 4 subplots as specified in Assignment #1
    Arguments:
    sp   -- a number representing the subplot
    d1   -- a triple (mean, sd, data)
    d2   -- a triple (mean, sd, data)
    """
    # this is for subplot 1 , dashed and dotted lines as requested
    if sp == 1:
        plt.subplot(2,2,1)
        plt.xlim([0,20])
        plt.ylim([0,45])
        plt.axhline(y = 25,linestyle = 'solid',color='aquamarine')
        plt.axhline(y = 10, linestyle = 'solid', color = 'b')
        plt.plot(d2, label="mean=25, sd=5",color='aquamarine' , linestyle = 'dotted' , linewidth = 2.25)
        plt.plot(d1 , label="mean=10, sd=2" , color = 'b' , linestyle = 'dashed' , linewidth = 2.25)
        plt.legend(loc=1)
        plt.xlabel("Array Index")
        plt.ylabel("Random Value")
        plt.title("Normal Distributions (line graph)")
    # this is for subplot 2 , the lines are wider as shown in the assignment
    if sp == 2:
        plt.subplot(2,2,2)
        plt.xlim([0,20])
        plt.ylim([0,45])
        plt.axhline(y = 25,linestyle = 'dotted',color='#cbcb33')
        plt.axhline(y = 10, linestyle = 'dotted', color = 'darkgreen' , )
        plt.plot(d2, label="mean=25, sd=5",color='#cbcb33' ,linewidth=3.5)
        plt.plot(d1 , label="mean=10, sd=2" , color = 'darkgreen' , linewidth=3.5)
        plt.legend(loc=1)
        plt.xlabel("Array Index")
        plt.ylabel("Random Value")
        plt.title("Normal Distributions (line graph)")
    #this is for subplot 3, i tried makin ghte width negative + aligning it to edge so the blue bars appear to the left
    if sp == 3:
        x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        plt.subplot(2,2,3)
        plt.xlim([0,20])
        plt.ylim([0,45])
        plt.axhline(y = 25,linestyle = 'dotted',color='lightseagreen')
        plt.axhline(y = 10, linestyle = 'dotted', color = 'b')
        plt.bar(x,d2, align = 'center', label="mean=25, sd=5" ,color='lightseagreen' , width = 0.75)
        plt.bar(x,d1 ,align = 'edge', label="mean=10, sd=2" , color = 'b' , width = -0.65 )
        plt.legend(loc=1)
        plt.xlabel("Array Index")
        plt.ylabel("Random Value")
        plt.title("Normal Distributions (Bar graph)")
    #this is for subplot 4 , i changed the width of the darkgreen bars and aligned the hazel bars to edge , so it can resemble the assignment
    if sp == 4:
        x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        plt.subplot(2,2,4)
        plt.xlim([0,20])
        plt.ylim([0,45])
        plt.axhline(y = 25,linestyle = 'solid',color='#cbcb33')
        plt.axhline(y = 10, linestyle = 'solid', color = 'darkgreen')
        plt.bar(x,d2, align = 'edge', label="mean=25, sd=5", color='#cbcb33' )
        plt.bar(x,d1 ,label="mean=10, sd=2", color = 'darkgreen' , width = 0.45)
        plt.legend(loc=1)
        plt.xlabel("Array Index")
        plt.ylabel("Random Value")
        plt.title("Normal Distributions (Bar graph)")
    #adjustment so the graphs arent crammed

        
    plt.subplots_adjust(hspace=.5)
    plt.subplots_adjust(wspace=.5)
    
   



    
    
        
          
#first call up for mean 10 and sd 2                    
var = gen_normal(10,2)
#second call up for mean 25 and sd 5
var2 = gen_normal2(25,10)

print(var)
print(var2)

plt.figure()
gen_subplot(1,var[2],var2[2])
gen_subplot(2,var[2], var2[2])
gen_subplot(3,var[2],var2[2])
gen_subplot(4,var[2],var2[2])
#this displays and calls up the subplot method

 #shows the graphs
plt.show()

    


