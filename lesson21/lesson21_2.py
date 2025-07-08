import tkinter as tk

def on_button_click():
    print("Hello, Tkinter!")

def create_main_window():
    window = tk.Tk()
    window.title("簡單Tkinter範例")
    window.geometry("300x200")

    # 建立按鈕並綁定事件處理函式
    btn = tk.Button(window, text="點我", command=on_button_click)
    btn.pack(pady=50)

    return window

def main():
    window = create_main_window()
    window.mainloop()

if __name__ == "__main__":
    main()
