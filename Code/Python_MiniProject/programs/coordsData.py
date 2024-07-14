import getPixel
from PIL import Image
def getData(image_path):
    #alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","bl","bl","bl","bl
    w,h = 60,55
    left,top=w,h
    right,bottom=310,340
    coordinates=[]
    l,u=0,1
    for j in range (1,4):
        #print(top,bottom)
        for i in range(1,11):
            #output_path = "C:\\Users\\piyus\\OneDrive\\Desktop\\MiniProject\\database\\alphabets_config\\{}.jpg".format(alpha[l])
            #print(i)
            #print(left,right)
            #select_portion(image_path,left,top,right,bottom,output_path)
            coordinates.append(getPixel.get_black_pixels_in_portion(image_path,left,top,right,bottom))
            l=l+1
            u=u+1
            left=right+w
            right=right+300+8
        top=bottom+h
        bottom=bottom+330
        left,right=50,300
    #print(coordinates)
    return coordinates
    
    