"""
====================
Author:释法海
Time：2022/6/1 21:52
Porject：Pytest_demo
Address:shanghai
====================
"""
import os
import pytest
from common.handle_path import reports_dir


if __name__ == '__main__':

    report_path = reports_dir+os.sep+"result"
    report_html_path = reports_dir+os.sep+"html"
    pytest.main(["-s","--alluredir",report_path])
    #Base.send_mail()




