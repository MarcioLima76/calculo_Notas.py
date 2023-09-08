#Tela 3: Estudando o Label e Photoimage
#DAta:08/05/2021
#Dev: MNL
#---------------------------------------------------------------
from tkinter import *
#--------------------------------------------------------------
tela1 = Tk()
tela1.title("MNL Teaching")
tela1.iconbitmap(default='tela1.ico')
tela1.geometry("500x200+0+0")
# tela1.wm_resizable(width=FALSE, height=FALSE)







#-------------------------------------------------------------
def mouseBtnEsquerdo(evento):
    tela1.title("MNL" + "x:" + str(evento.x) + "y:" + str(evento.y))
    print(tela1.geometry())

#----------------------------------------------------------------




#-------------------------------
tela1.bind('Button-1>', mouseBtnEsquerdo)
tela1.mainloop()




