
from tkinter import *
from tkinter.ttk import *
from time import strftime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mydb']
collection = db['OPENLAB_Data']

root = Tk()
root.title('AUTOMATIC TRAFFIC LIGHT CONTROLLER')
root.geometry('550x650')
root.resizable(False, False)
root['bg'] = 'gray20'

def time():


    EAST_C.config(text='Count :{}'.format(collection.find_one({"_id": 1})['count']))
    EAST_C2.config(background=collection.find_one({"_id": 1})['S'])
    WEST_C.config(text='Count :{}'.format(collection.find_one({"_id": 2})['count']))
    WEST_C2.config(background=collection.find_one({"_id": 2})['S'])
    NORTH_C.config(text='Count :{}'.format(collection.find_one({"_id": 3})['count']))
    NORTH_C2.config(background=collection.find_one({"_id": 3})['S'])
    SOUTH_C.config(text='Count :{}'.format(collection.find_one({"_id": 4})['count']))
    SOUTH_C2.config(background=collection.find_one({"_id": 4})['S'])
    if collection.find_one({"_id": 1})['S'] == "Green":
        EAST_C3.config(text='Green_TIMER :{}'.format(collection.find_one({"_id": 1})['Green']))
    elif collection.find_one({"_id": 1})['S'] == "Red":
        EAST_C3.config(text='Red_TIMER :{}'.format(collection.find_one({"_id": 1})['red']))
    if collection.find_one({"_id": 2})['S'] == "Green":
        WEST_C3.config(text='Green_TIMER :{}'.format(collection.find_one({"_id": 2})['Green']))
    elif collection.find_one({"_id": 2})['S'] == "Red":
        WEST_C3.config(text='Red_TIMER :{}'.format(collection.find_one({"_id": 2})['red']))
    if collection.find_one({"_id": 3})['S'] == "Green":
        NORTH_C3.config(text='Green_TIMER :{}'.format(collection.find_one({"_id": 3})['Green']))
    elif collection.find_one({"_id": 3})['S'] == "Red":
        NORTH_C3.config(text='Red_TIMER :{}'.format(collection.find_one({"_id": 3})['red']))
    if collection.find_one({"_id": 4})['S'] == "Green":
        SOUTH_C3.config(text='Green_TIMER :{}'.format(collection.find_one({"_id": 4})['Green']))
    elif collection.find_one({"_id": 4})['S'] == "Red":
        SOUTH_C3.config(text='Red_TIMER :{}'.format(collection.find_one({"_id": 4})['red']))


    if collection.find_one({"_id":1})['S']=="Green":
        CURRENT_label.configure(text="Green : Road East")
    if collection.find_one({"_id":2})['S']=="Green":
        CURRENT_label.configure(text="Green : Road West")
    if collection.find_one({"_id":3})['S']=="Green":
        CURRENT_label.configure(text="Green : Road North")
    if collection.find_one({"_id":4})['S']=="Green":
        CURRENT_label.configure(text="Green : Road South")
    string = strftime('%m/%d/%Y, %H:%M:%S ')
    lbl.config(text=string)

    lbl.after(1000, time)


img = PhotoImage(file='am.png')
Label(root, image=img).place(x=200, y=0)

img2 = PhotoImage(file='roads.png')
Label(root, image=img2).place(x=180, y=300)

lbl = Label(root, font=('Bahnschrift', 18, 'bold'), background='purple', foreground='white')
lbl.place(x=335, y=0)

lbl_intro = Label(root, text='OPEN LAB: GROUP 7', font=('calibri', 18), background='red', foreground='white')
lbl_intro.place(x=0, y=0)

CURRENT_label = Label(root, text='Green:', font=('Bahnschrift', 11), background='BLACK', foreground='white')
CURRENT_label.place(x=200, y=60)




r_l = Label(text='____________________________________________________'.format(10),
            font=('Bahnschrift', 11), background='BLACK', foreground='white')
r_l.place(x=100, y=100)

EAST_IN = Label(root, text='ROAD EAST', font=('Bahnschrift', 11), background='BLACK', foreground='white')
EAST_IN.place(x=410, y=310)
EAST_C = Label(root, text='Count : {}'.format(0), font=('Bahnschrift', 11), background='blue', foreground='white')
EAST_C.place(x=410, y=340)
EAST_C2 = Label(root, text='STATUS', font=('Bahnschrift', 11), background='GREEN', foreground='white')
EAST_C2.place(x=410, y=370)
EAST_C3 = Label(root, text='TIMER : {}'.format(250), font=('Bahnschrift', 11), background='BLUE', foreground='white')
EAST_C3.place(x=410, y=400)

WEST_IN = Label(root, text='ROAD WEST', font=('Bahnschrift', 11), background='BLACK', foreground='white')
WEST_IN.place(x=10, y=310)
WEST_C = Label(root, text='Count : {}'.format(0), font=('Bahnschrift', 11), background='blue', foreground='white')
WEST_C.place(x=10, y=340)
WEST_C2 = Label(root, text='STATUS ', font=('Bahnschrift', 11), background='RED', foreground='white')
WEST_C2.place(x=10, y=370)
WEST_C3 = Label(root, text='TIMER :{} '.format(750), font=('Bahnschrift', 11), background='BLUE', foreground='white')
WEST_C3.place(x=10, y=400)

NORTH_IN = Label(root, text='ROAD NORTH', font=('Bahnschrift', 11), background='BLACK', foreground='white')
NORTH_IN.place(x=230, y=150)
NORTH_C = Label(root, text='Count : {}'.format(0), font=('Bahnschrift', 11), background='blue', foreground='white')
NORTH_C.place(x=230, y=180)
NORTH_C2 = Label(root, text='STATUS', font=('Bahnschrift', 11), background='RED', foreground='white')
NORTH_C2.place(x=230, y=210)
NORTH_C3 = Label(root, text='TIMER :{}'.format(500), font=('Bahnschrift', 11), background='BLUE', foreground='white')
NORTH_C3.place(x=230, y=240)

SOUTH_IN = Label(root, text='ROAD SOUTH', font=('Bahnschrift', 11), background='BLACK', foreground='white')
SOUTH_IN.place(x=230, y=500)
SOUTH_C = Label(root, text='Count : {}'.format(0), font=('Bahnschrift', 11), background='blue', foreground='white')
SOUTH_C.place(x=230, y=530)
SOUTH_C2 = Label(root, text='STATUS'.format(0), font=('Bahnschrift', 11), background='RED', foreground='white')
SOUTH_C2.place(x=230, y=560)
SOUTH_C3 = Label(root, text='TIMER : {}'.format(1000), font=('Bahnschrift', 11), background='BLUE', foreground='white')
SOUTH_C3.place(x=230, y=590)

time()

mainloop()
