import os

def clusterbarchart(y1,y2):
    import matplotlib.pyplot as plt
    import numpy as np
    labels = ['AMG334', 'AMG162']
    x = np.arange(len(labels))
    width = 0.3
    fig = plt.figure()
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x-0.3, y1, width, label='High', color='blue')
    rects2 = ax.bar(x, y2, width, label='Low', color='lightpink')
    
    ax.set_ylabel('Quality')
    ax.set_title('ESQ Manufacturer Review')
    ax.set_xlabel('Material')
    ax.set_xticks(x, labels)
    ax.legend()
    
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    
    fig.tight_layout()
    plt.show
    fig.savefig("C:/Users/jtan15/py_Screenshot.png")
    plt.show
    
y1 = [57,66]
y2 = [7,8]
if __name__=="__main__":
    clusterbarchart(sys.argv[1],sys.argv[2])
