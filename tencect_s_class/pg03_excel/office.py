#!/usr/bin/python3

# *_*coding:utf8 *_*
# @Time : 2020/4/28 12:57
# @Author : FengLin
# @Email : damon__dong@163.com
# @File : office.py

# Excel  办公自动化
# pycharm + python
# 先听思路   VIP 老师  录制  0基础视频   安装   基本语法

import xlrd
file_path = "成绩.xls"
# xlrd  工具包 别人写好  工具
workbook = xlrd.open_workbook(file_path)
# 成绩表格
sheet = workbook.sheet_by_name("1001班")

while True:
    # 输入查询的姓名和科目 pip isntall
    name = input("请输入学生的姓名:")
    subject = input("请输入查询科目:")
    # print(name)

    # 数据区域的行数和列数
    rows = sheet.nrows
    cols = sheet.ncols
    print(rows, cols)

    # 姓名  科目
    names = sheet.col_values(0)
    subjects = sheet.row_values(0)
    print(names, subjects)

    # 查找姓名在第几行
    if name in names:
        name_row = [names.index(name), ]
    else:
        name_row = range(0, rows)

    # 查找科目在第几列
    if subject in subjects:
        subject_col = [subjects.index(subject), ]
    else:
        subject_col = range(0, cols)

    # print(name_row,subject_col)
    # value = sheet.cell(name_row[0],subject_col[0]).value
    # print(name,subject,value)
    #  逐行逐列扫描数据  位置
    for row in name_row:
        for col in subject_col:
            print(row, col)
            name = sheet.cell(row, 0).value
            subject = sheet.cell(0, col).value
            value = sheet.cell(row, col).value
            print(name, subject, value)

        print("\n")









