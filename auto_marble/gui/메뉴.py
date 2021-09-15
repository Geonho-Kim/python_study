from tkinter import *

root = Tk()
root.title("Menu")      # 맥에서 작동하지 않음
root.geometry("640x480+100+100")


def create_new_file():
    print("새 파일을 만듭니다.")


menu = Menu(root)


# File 메뉴
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

# Edit 메뉴(빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 추가 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="c++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴
manu_view = Menu(menu, tearoff=0)
manu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=manu_view)


root.config(menu=menu)
root.mainloop()
