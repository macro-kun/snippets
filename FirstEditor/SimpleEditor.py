# 簡易的なメモ帳アプリ
# テキストの入力を受け付けて、文字コードutf-8で保存する
# デフォルトのサイズは450x450
# Xボタンを押したときに、ファイルを保存できるようにする
# テキストが空の場合は、「保存するテキストがありません」という
# メッセージを表示する
# tkinter を使用する

import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.scrolledtext import ScrolledText


class SimpleEditor:
    def __init__(self, root):
        root.title(self.__class__.__name__)
        self.text = ScrolledText()
        self.text.pack(expand=1, fill=tk.BOTH)

        # ウィンドウサイズはデフォルトで 450x450
        root.geometry("450x450")
        # ウィンドウを閉じるときに、ファイルを保存する
        root.protocol('WM_DELETE_WINDOW', self.saveFile)

    # ファイルを保存するためのメソッド
    def saveFile(self):
        s = self.text.get('1.0', 'end')
        if len(s) == 1:
            messagebox.showwarning(
                self.__class__.__name__,
                '保存するテキストがありません'
            )
            return

        # ファイル名を入力するダイアログを表示する
        filename = filedialog.asksaveasfilename()
        if not filename:
            return

        f = open(filename, 'w', encoding='UTF-8')
        f.write(s[:-1])
        f.close()
        root.destroy()


root = tk.Tk()
SimpleEditor(root)
root.mainloop()
