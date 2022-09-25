# EDA Automation

#1 Pandas Profiling

import pandas as pd
import numpy as np

df = pd.read_csv("Travel.csv")
"""
from pandas_profiling import ProfileReport

profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("output.html")

"""
#2) Autoviz

from autoviz.AutoViz_Class import AutoViz_Class

AV = AutoViz_Class()
df1 = AV.AutoViz('Travel.csv')

#3 Sweet Viz
"""
import sweetviz as sv

my_report = sv.analyze(df)
my_report.show_html(dfsweetviz.html) # Default arguments will generate to "SWEETVIZ_REPORT.html"
"""
