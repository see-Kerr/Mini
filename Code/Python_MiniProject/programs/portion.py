from PIL import Image

def select_portion(image_path, left, top, right, bottom, output_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Define the coordinates for the portion to be selected
        box = (left, top, right, bottom)
        # Crop the image using the defined box
        cropped_image = img.crop(box)
        # Save the cropped image
        cropped_image.save(output_path)
        print(f'Cropped image saved to {output_path}')


def getData(image_path):
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","bl","bl","bl","bl"]
    image_path = "C:\\Users\\piyus\\OneDrive\\Desktop\\MiniProject\\database\\alphabets_config\\alphabets.jpg"
    w,h = 60,55
    left,top=w,h
    right,bottom=310,340
    coordinates=[]
    l=0
    for j in range (1,4):
        #print(top,bottom)
        for i in range(1,11):
            output_path = "C:\\Users\\piyus\\OneDrive\\Desktop\\MiniProject\\database\\alphabets_config\\{}.jpg".format(alpha[l])
            print(i)
            #print(left,right)
            select_portion(image_path,left,top,right,bottom,output_path)
            l=l+1
            left=right+w
            right=right+300+8
        top=bottom+h
        bottom=bottom+330
        left,right=50,300
    return coordinates

getData("")