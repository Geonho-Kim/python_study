import os
from tkinter import *

root = Tk()
root.title("제목 없음 - windows 메모장")
root.geometry("640x480+100+100")    # 가로 x 세로 + 초기화면위치 x좌표 + 초기회면위치 y좌표

menu = Menu(root)

# 열기, 저장, 파일 이름
filename="mynote.txt"
def open_file():
    if os.path.isfile(filename):    # 파일이 있으면 True
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)  # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read())    # 파일 내용을 본문에 입력

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

def close_file():
    root.quit()
# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="열기", command=close_file)
menu.add_cascade(label="파일", menu=menu_file)
# 편집, 서식, 보기, 도움말 메뉴
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True)
scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()
