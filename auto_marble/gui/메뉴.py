from tkinter import *

root = Tk()
root.title("Menu")      # 맥에서 작동하지 않음
root.geometry("640x480+100+100")


def create_new_file():
    print("새 파일을 만듭니다.")


menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")    # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

root.config(menu=menu)
root.mainloop()
