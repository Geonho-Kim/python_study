from tkinter import *

root = Tk()
root.title("Text&Entry")
root.geometry("640x480+100+100")

txt = Text(root, width=30, height=5)        # enter O
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)           #enter X
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))      # 1 = 첫번째 라인부터, 0 = 0번째 인덱스 ==> 처음부터 끝까지
    print(e.get())
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()