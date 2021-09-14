from tkinter import *

root = Tk()
root.title("Radio Button")      # 여러개 중 하나를 선택
root.geometry("640x480+100+100")

Label(root, text="메뉴를 선택하세요").pack()

buger_var = IntVar()    # 여기에 int형으로 값을 저장한다
btn_buger1 = Radiobutton(root, text="햄버거", value=1, variable=buger_var)
btn_buger1.select()     # 기본 선택
btn_buger2 = Radiobutton(root, text="치즈버거", value=2, variable=buger_var)
btn_buger3 = Radiobutton(root, text="치킨버거", value=3, variable=buger_var)

btn_buger1.pack()
btn_buger2.pack()
btn_buger3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(buger_var.get())  # 햄버거 중 선택된 라디오 항목의 값 반환(value)
    print(drink_var.get())  # 음료 중 선택된 라디오 항목의 값 반환

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()