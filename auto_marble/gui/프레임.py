from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+100+100")    # 가로 x 세로 + 초기화면위치 x좌표 + 초기회면위치 y좌표
root.resizable(False, False)    # 창 크기 변경 불가

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 메뉴 프레임
frame_buger = Frame(root, relief="solid", bd=1)
frame_buger.pack(side="left", fill="both", expand=True)

Button(frame_buger, text="햄버거").pack()
Button(frame_buger, text="치즈버거").pack()
Button(frame_buger, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()


root.mainloop()





