import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("ComboBox")      # 여러개 중 하나를 선택
root.geometry("640x480+100+100")

values = [str(i) + "일" for i in range(1, 32)]   # 1~31까지
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정(버튼 입력을 통한 값 설정도 가능)

readonly_combobox = ttk.Combobox(root, height=10, values=values, stat="readonly")    # 읽기 전용
# height = 목록이 한번에 보이는 수 지정
readonly_combobox.current(0)    # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())   # 선택한 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()