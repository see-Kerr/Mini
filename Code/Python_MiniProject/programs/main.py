import tkinter as tk
from tkinter import filedialog
import numpy as np
import coordsData

image_path = "C:\\Users\\Piyush\\Desktop\\Code\\Python_MiniProject\\database\\alphabets_config\\alphabets1.jpg" 
coordinates = coordsData.getData(image_path)
end,pv=[0,0],[0,0]
pixels = {
    'a': coordinates[0],
    'b': coordinates[1],
    'c': coordinates[2],
    'd': np.add(coordinates[3],[0,10]),
    'e': coordinates[4],
    'f': np.add(coordinates[5],[-15,40]),
    'g': np.add(coordinates[6],[0,40]),
    'h': np.add(coordinates[7],[0,-20]),
    'i': coordinates[8],
    'j': np.add(coordinates[9],[0,40]),
    'k': np.add(coordinates[10],[0,0])*np.array([1.2,1.2]),
    'l': np.add(coordinates[11],[0,-20]),
    'm': np.add(coordinates[12],[0,-30]),
    'n': np.add(coordinates[13],[0,-30]),
    'o': np.add(coordinates[14],[0,-20])*np.array([0.8,0.8]),
    'p': np.add(coordinates[15],[0,10])*np.array([1.2,1.2]),
    'q': np.add(coordinates[16],[0,-8])*np.array([1.2,1.2]),
    'r': coordinates[17],
    's': coordinates[18],
    't': coordinates[19],
    'u': coordinates[20],
    'v': np.add(coordinates[21],[0,-40]),
    'w': np.add(coordinates[22],[0,-40]),
    'x': coordinates[23],
    'y': coordinates[24],
    'z': coordinates[25],
    '\x08':coordinates[26]
}

Y=0
def draw_coordinates(canvas, coordinates,sx=1, sy=1, end=[0,0],col='#383838'):
    global Y
    coordinate = coordinates*np.array([sx,sy])
    #print(coordinates[1])
    for (x, y) in coordinate:
        canvas.create_line(x+end[0]+100,y+35+Y, x+end[0]+100+0.5, y+35+Y, fill=col)
    return coordinate[len(coordinate)-1]

def draw_ruled_page(canvas):
    for i in range(80):
        canvas.create_line(100, 40 * i, 900, 40 * i, fill='gray')
        if i % 50 == 0:
            canvas.create_line(100, 40 * i, 900, 40 * i, fill='black', width=1)

def new_page(canvas):
    canvas.delete("all")
    draw_ruled_page(canvas)

def save_page(canvas):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = canvas.itemcget('all', 'text')
            file.write(content)
def on_key_press(event):
    global end,pv,Y
    #print(end[1])
    if(end[1]<-190):
        #print('greater')
        Y=Y+40
        end=[0,0]
    key = event.char
    if key==" ":
        end=[end[0]+10,end[1]]
    elif key == "\r":
        Y=Y+40
        end=[0,0]
        print(pixels['\x08'])
    elif key:
        pv=draw_coordinates(canvas, pixels[key],0.158,0.158,end)
        end=np.add(pv,end)

root = tk.Tk()
root.title("Notebook")

# Create canvas
canvas = tk.Canvas(root, bg='white', width=1000, height=630)
canvas.pack()

draw_ruled_page(canvas)

# Create file menu
menu = tk.Menu(root)
root.config(menu=menu)
canvas.pack()
root.bind('<KeyPress>', on_key_press)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: new_page(canvas))
file_menu.add_command(label="Save", command=lambda: save_page(canvas))

root.mainloop()