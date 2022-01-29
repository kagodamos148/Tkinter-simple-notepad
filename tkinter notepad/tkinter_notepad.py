# TKINTER 
import tkinter as tk
from tkinter import font
import  tkinter.filedialog as tkfile # for file saving and opening
import ctypes # for screen adjustments
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from PIL import Image, ImageTk
# save as text from the text file

def saveas_txt():
   #use filedialog to open asksaveasfile
   file = tkfile.asksaveasfilename(filetypes=[('text file' '*.txt')], defaultextension='.txt')
   # stringdummy = labeldummy1.get()
   textfile = open(file, 'w')
   textfile.write(textspace.get(1.0, tk.END))
   textfile.close()

# save  text from the text file
def savetxt():
   #use filedialog to open asksaveasfile
   # file = tkfile.asksaveasfilename(filetypes=[('text file' '*.txt')], defaultextension='.txt')
   if textentry.get() != 'Untitled Page':
      stringdummy = textentry.get()
      if not stringdummy.endswith('.txt'):
         stringdummy+= '.txt'
      textfile = open(stringdummy, 'w')
      textfile.write(textspace.get(1.0, tk.END))
      textfile.close()
   else:
      saveas_txt()

# open text from folder
def opentxt():
   # print('hi')
   file = tkfile.askopenfilename()
   # stringdummy = labeldummy.get()
   textfile = open(file, 'r')
   textspace.delete("1.0", tk.END)
   textspace.insert("1.0", textfile.read())
   textentry.delete(0, tk.END)
   textentry.insert(0, file)
   textfile.close()

def status():
   return  'not saved'

#start of program
# rakesh jinka 27-01-2001


#other widgets

# labeltext = tk.Label(text = "Notepad")
# labeltext.pack()

# labeldummy1 = tk.Entry(frame1)
# labeldummy1.pack()

#root features
root = tk.Tk()
root.title('Notepad for windows 10')
root.geometry('1200x750')
root.configure(background='#9adefe')
# root.overrideredirect(True)



# frames used
frame1 = tk.Frame(master=root, width= 200, bg = '#9adefe')
frame1.pack(fill = tk.Y, side = tk.LEFT, pady = 100)
frame1.configure(background= '#9adefe')

frame2 = tk.Frame(master=root)
frame2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
frame2.configure(background= '#9adefe')

# widgets used
#frame2
textentry = tk.Entry(frame2, font= ('calibri', '18'), bd =0)
textentry.insert(0, 'Untitled Page') 
textentry.pack(fill = tk.BOTH, side = tk.TOP, expand=False, ipady = 10,  ipadx = 20, padx = 15) 
textentry.configure( background= '#9adefe')

textspace = tk.Text(frame2, font= ('calibri', '12'), )
textspace.insert("1.0", 'Hi there, Enter your text.') 
textspace.pack(fill= tk.BOTH, side = tk.TOP, expand = True, padx = (10, 20), pady= (0, 5))

#frame1
open_file = Image.open('open_image.png')
image2= open_file.resize((30,30),Image.ANTIALIAS)
open_photoimage = ImageTk.PhotoImage(image2)
buttonopen = tk.Button(frame1, image = open_photoimage,command= lambda: opentxt(), bg='#9adefe' , bd = 0)
buttonopen.pack( ipadx = 10,  ipady = 10,)

save_file = Image.open('save_button.png')
image2= save_file.resize((35,35),Image.ANTIALIAS)
save_photoimage = ImageTk.PhotoImage(image2)
buttonsave = tk.Button(frame1, image = save_photoimage,command= lambda: savetxt(),bg='#9adefe', bd=0) #bd = border width
buttonsave.pack( ipadx = 10, ipady = 10)

save_as_file = Image.open('save_as_button.png')
image2= save_as_file.resize((35,35),Image.ANTIALIAS)
save_as_photoimage = ImageTk.PhotoImage(image2)
buttonsave = tk.Button(frame1, image = save_as_photoimage,command= lambda: saveas_txt(),bg='#9adefe', bd=0) #bd = border width
buttonsave.pack( ipadx = 10, ipady = 10)

exit_file = Image.open('exit_button.png')
image2= exit_file.resize((35,35),Image.ANTIALIAS)
exit_photoimage = ImageTk.PhotoImage(image2)
buttonprint = tk.Button(frame1, image = exit_photoimage, command= root.destroy,bg='#9adefe', bd = 0)
buttonprint.pack( ipadx = 10, ipady = 10)


# image = Image.open('digital_art_nature.jpg')
# photo = ImageTk.PhotoImage(image)
labelstatus = tk.Label(frame2, text = 'By kago', font = ('calibri' , '12'))
labelstatus.pack(fill = tk.X, side = tk.RIGHT, pady = 15, padx = (0,15))

root.mainloop()







