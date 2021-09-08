from tkinter import *

root = Tk()
root.title("Button")
root.geometry("640x480+100+100")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")    # padx: 좌우 여백
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")    # pady: 상하 여백
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")     # 크기 고정
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="raining.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print('버튼을 눌렀어요.')

btn7 = Button(root, text="동작하는 버튼", command = btncmd)
btn7.pack()

root.mainloop()





