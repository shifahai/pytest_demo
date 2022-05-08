import  unittest
import os
from BeautifulReport import BeautifulReport
from Common.handle_path import cases_dir,reports_dir,debug_dir

# 收集用例
s = unittest.TestLoader().discover(cases_dir)
#生成报告
br = BeautifulReport(s)
br.report("自动化脚本","report_.html",reports_dir)