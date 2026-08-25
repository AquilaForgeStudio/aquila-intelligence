from ui import app
#나중에 firebase 연결할시 firebase 불러와서 json에 적용시키는 기능도 추가

def boot():
    Ui = app.MainUi()

    Ui.mainloop()