# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:50:19 2020

@author: adiministrator


在工作中，经常会遇到合并pdf文件的需求，这时候你会发现不是一件很容易完成的任务。
包括WPS、福昕阅读器在内的很多软件都有合并pdf文件的功能，但是只有交钱变成会员之后
才能使用，否则只能合并3页。有不少网站提供了在线合并pdf文件的功能，但也是必须交钱
才能用。还有的显示合并成功，但就是无法下载。如果你会一点Python，就会发现这是一件
很容易的事，并且不用花一分钱。
功能描述：
使用Python合并任意多个PDF文件。
详细步骤：
1、安装扩展库PyPDF2。
2、编写代码。
3、把代码中pdf_files的内容改成自己要合并pdf文件名，运行代码，一眨眼，合并完成。

"""
from PyPDF2  import PdfFileReader,PdfFileMerger

#要合并的多个pdf文件
pdf_files = ('pdf130.pdf','pdf131.pdf','pdf132.pdf')

result_pdf = PdfFileMerger()
#依次读取每个文件的内容，并进行合并
for pdf in pdf_files:
    with open(pdf,'rb') as fp:
        pdf_reader = PdfFileReader(fp)
        if pdf_reader.isEncrypted:
            print(f'忽略加密文件：{pdf}')
            continue
        result_pdf.append(pdf_reader,import_bookmarks=True)
        
#保存合并的PDF文件
result_pdf.write('result.pdf')
result_pdf.close()
