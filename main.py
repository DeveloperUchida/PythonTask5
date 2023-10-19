import PySimpleGUI as Sg
import datetime

Sg.theme("DarkBrown3")

layout = [[Sg.Text("AM 00:00:00", font=("Arial", 40), key="txt1", size=(20, 1), justification="center")]]
win = Sg.Window("時計", layout, size=(400, 80), keep_on_top=True)

while True:
    event, values = win.read(timeout=1000)  # 時計を1秒ごとに更新するためにタイムアウト値を使用

    if event == Sg.WIN_CLOSED:
        break

    now = datetime.datetime.now()
    win["txt1"].update(f"{now:%H:%M:%S}")

win.close()
