import pandas_profiling as pp
import pandas as pd
import ydata_profiling as yp
import skimpy as skim
import seaborn as sns
iris=sns.load_dataset('iris')
profile = pp.ProfileReport(iris)
profile=profile.to_file("iris.html")
skim_report = skim(profile)
skim_report.to_file("iris_skim.html")