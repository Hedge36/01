#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/12 10:11
# @Author : Hedge
# @File : Project1 Simple_Calculate.py
# @Software: PyCharm
import tkinter as tk
from tkinter import scrolledtext as st

mwindow = tk.Tk()
mwindow.title("简易计算器")
mwindow.geometry("400x400")
history = []
vartext = tk.StringVar()
text_display = st.ScrolledText(mwindow, bg="white", width=28,
                               height=3, font="Arial 18")
text_display.grid(row=0, columnspan=4, padx=10, pady=10)


def change(x):
    """向文本框输入数字"""
    text_display.insert("insert", x)


def text_delete_sing():
    """删除上一个字符串"""
    text_display.delete("insert-1c")
    # “ -2c”部分表示“减两个字符”。负一个字符将索引移动到不可见的尾随换行符之前，用于删除结尾
    # “insert”表示当前光标位置


def text_delete_all():
    """删除全部字符串"""
    text_display.delete(1.0, tk.END)


def equal():
    """现有结果计算"""
    try:
        # express表达式的处理
        express = text_display.get(0.1, "end").replace("\n", "")
        # 现仅支持乘除
        keys_check = {'x': "*"}, {"÷": "/"}
        for keys in keys_check:
            for key, value in keys.items():
                express = express.replace(key, value)
        if len(history) != 0:
            print("".join(history))
            express = express.replace("".join(history), '')
        # 避免结果超过显示屏，结果取前18位
        outcome = str(eval(express))[:19]
        # print(express)
        history.append(express + '=' + outcome)
        # print(history)
        text_display.insert("end", "\n=%s\n" % outcome)
        # 滚动条聚焦于光标
        text_display.see("insert")
    except SyntaxError:
        text_delete_all()
        change("Error!The input does not conform to the syntax specification!\n")
    except NameError:
        text_delete_all()
        change("Error!Any letter exists!\n")
    except:
        text_delete_all()
        change(
            "Error!Some unexpected errors have occurred, please contact the administrator for repair as soon as "
            "possible.\n")


def init_button():
    """按钮控件初始化"""
    # Button_Number
    times = 0
    col, row = divmod(times, 3)
    for i in range(9):
        times += 1
        text_button = "tk.Button(mwindow, text=%d, font=('Arial 18'), width=4," \
                      "command=lambda : change(%d)).grid(row=%d,column=%d," \
                      "ipadx=1, pady=5)" % (times, times, row + 2, col)
        exec(text_button)
        row, col = divmod(times, 3)
    # button_0 数字0
    tk.Button(mwindow, text=0, font='Arial 18', width=4,
              command=lambda: change(0)).grid(row=5, column=1,
                                              ipadx=1, pady=5)

    # Operator 操作符
    # button_clear 清除符
    tk.Button(mwindow, text='C', font='Arial 18', width=4,
              command=text_delete_all).grid(row=1, column=0,
                                            ipadx=1, pady=5)
    # button_pare_left 左侧括号
    tk.Button(mwindow, text='(', font='Arial 18', width=4,
              command=lambda: change('(')).grid(row=1, column=1,
                                                ipadx=1, pady=5)
    # button_pare_right 右侧括号
    tk.Button(mwindow, text=')', font='Arial 18', width=4,
              command=lambda: change(')')).grid(row=1, column=2,
                                                ipadx=1, pady=5)
    # button_bask  删除回退符
    tk.Button(mwindow, text='⬅', font='Arial 18', width=4,
              command=text_delete_sing).grid(row=1, column=3,
                                             ipadx=1, pady=5)
    # button_plus  加号
    tk.Button(mwindow, text='+', font='Arial 18', width=4,
              command=lambda: change('+')).grid(row=2, column=3,
                                                ipadx=1, pady=5)
    # button_subt 减号
    tk.Button(mwindow, text='-', font='Arial 18', width=4,
              command=lambda: change('-')).grid(row=3, column=3,
                                                ipadx=1, pady=5)
    # button_mult 乘号
    tk.Button(mwindow, text='÷', font='Arial 18', width=4,
              command=lambda: change('÷')).grid(row=4, column=3,
                                                ipadx=1, pady=5)
    # button_divi 除号
    tk.Button(mwindow, text='×', font='Arial 18', width=4,
              command=lambda: change('x')).grid(row=5, column=3,
                                                ipadx=1, pady=5)
    # button_equa 等号
    tk.Button(mwindow, text='=', font='Arial 18', width=4,
              command=equal).grid(row=5, column=2,
                                  ipadx=1, pady=5)
    # button_poin 小数点
    tk.Button(mwindow, text=".", font='Arial 18', width=4,
              command=lambda: change('.')).grid(row=5, column=0,
                                                ipadx=1, pady=5)


init_button()
mwindow.mainloop()
