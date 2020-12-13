import tkinter as tk  # 使用Tkinter前需要先导入

from tkinter import ttk


# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('测试系统')
window.resizable(1, 1) # 是否可以拉伸
# 第3步，设定窗口的大小(长 * 宽)
window.geometry()  # 这里的乘是小x

# 第4步，在图形界面上设定标签
# l = ttk.Label(window, text='你好！this is Tkinter', font=('Arial', 12), width=30)
LabelFrame0 = tk.LabelFrame(window, text='模块选择', fg = 'blue')
LabelFrame0.grid(row=0, rowspan = 1, columnspan = 1, column=0, padx=50, pady=20,sticky='W'+'E'+'N'+'S')  # Label内容content区域放置位置，自动调节尺寸


# style = ttk.Style()
# style.configure("BW.TLabel", font=("Times", "10",'bold'))
# ttk.Label(window, text="   社会主义核心价值观",style="BW.TLabel").grid(column=2, row=7,columnspan=2, sticky=tk.EW)


Label = ttk.Label(LabelFrame0, text='选择相应模块').grid(row = 0, column = 0, padx = 6, pady = 6)
entry = ttk.Entry(LabelFrame0).grid(row = 0, column = 1, padx = 6, pady = 6)
Label = ttk.Label(LabelFrame0, text='输入工作频率').grid(row = 1, column = 0, padx = 6, pady = 6)
entry = ttk.Entry(LabelFrame0).grid(row = 1, column = 1, padx = 6, pady = 6)
Label = ttk.Label(LabelFrame0, text='输入reg（16）').grid(row = 0, column = 2, padx = 6, pady = 6)
entry = ttk.Entry(LabelFrame0).grid(row = 0, column = 3, padx = 6, pady = 6, sticky='W'+'E'+'N'+'S')
Label = ttk.Label(LabelFrame0, text='输入reg（10）').grid(row = 1, column = 2, padx = 6, pady = 6)
entry = ttk.Entry(LabelFrame0).grid(row = 1, column = 3, padx = 6, pady = 6, sticky='W'+'E'+'N'+'S')

LabelFrame1 = ttk.LabelFrame(window, text='reg解析')
LabelFrame1.grid(row=1, rowspan = 1, columnspan = 1, column=0, padx=50, pady=20, sticky='W'+'E'+'N'+'S')  # Label内容content区域放置位置，自动调节尺寸

Label = ttk.Label(LabelFrame1, text='选择相应模块').grid(row = 0, column = 0, padx = 6, pady = 6)
entry = ttk.Entry(LabelFrame1).grid(row = 0, column = 1, padx = 6, pady = 6)
Label = ttk.Label(LabelFrame1, text='输入工作频率').grid(row = 1, column = 0, padx = 6, pady = 6)
entry = ttk.Entry(LabelFrame1).grid(row = 1, column = 1, padx = 6, pady = 6)
Label = ttk.Label(LabelFrame1, text='输入reg（16）').grid(row = 0, column = 2, padx = 6, pady = 6)
entry = ttk.Entry(LabelFrame1).grid(row = 0, column = 3, padx = 6, pady = 6)
Label = ttk.Label(LabelFrame1, text='输入reg（10）').grid(row = 1, column = 2, padx = 6, pady = 6,sticky='W'+'E'+'N'+'S')
entry = ttk.Entry(LabelFrame1).grid(row = 1, column = 3, padx = 6, pady = 6,sticky='W'+'E'+'N'+'S')

# 第6步，主窗口循环显示
window.mainloop()