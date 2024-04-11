import pandas as pd 
import matplotlib.pyplot as plt
import os
import numpy as np
pd.set_option("display.max.columns", None)
os.getcwd()
os.chdir('./data_folder/')
os.getcwd()
##################################
##DATA FROM CWED
cwed= pd.read_excel("./datasets/CWEP.Global_2022.xlsx")  #data from Comparative Welfare Entitlements Project (CWEP) at https://www.cwep.us/
type(cwed)
cwed.plot()
cwed.head()
dc=pd.DataFrame(cwed)
print(dc)
countries = dc.groupby(dc.COUNTRY)
dc_italy=countries.get_group('Italy')
dc_sweden=countries.get_group('Sweden')
dc_denmark=countries.get_group('Denmark')
dc_spain=countries.get_group('Spain')
dc_spain.head()
dc_italy.head()
##plot life expectancy of retired people at 65 or more
dc_italy.plot(x='YEAR', y='LEXP65',kind='line', figsize= (80,60), fontsize=60, lw=10,legend=False)
plt.xlabel('Time', fontsize=120)
plt.ylabel('Life expectancy of retired people', fontsize=120)
plt.show()
##
dc_italy.plot(x='YEAR', y=['LEXP65', 'PEN_DUR'],kind='line', figsize= (80,60), fontsize=60, lw=10,legend=False)
plt.xlabel('Time', fontsize=120)
plt.ylabel('Years', fontsize=120)
plt.legend(['Life expectancy of retired people','Expected duration of pension benefits'],loc='best', fontsize=50)
plt.show()
##Retirememnt age and life expectancy at retirment
dc_italy.plot.line(x='YEAR', y=['MRET','FRET'],figsize= (80,60), fontsize=60, lw=10)
plt.xlabel('Time', fontsize=120)
plt.ylabel('Retirement age', fontsize=120)
plt.legend(['Male','Female'],fontsize=120)
plt.show()
##define index column as time
dc.set_index('YEAR', inplace=True)



dc.groupby('COUNTRY')['SP_QUAL'].plot(figsize=(80,60), fontsize=60, lw=5.5)
plt.legend(bbox_to_anchor=(1,1), loc="best", fontsize=50)


dc_italy.plot(x='YEAR', y='PENCOV')
dc_spain.plot(x='YEAR', y='PENCOV')
dc_sweden.plot(x='YEAR', y='PENCOV')
dc_denmark.plot(x='YEAR', y='PENCOV')


dc_italy.plot(x='YEAR', y='SP_QUAL')


plt.show()
####
fig, it_exp= dc_italy(x='YEARS', y='LEXP65',figsize= (40,30), fontsize=20)
it_exp.plot.area(ax)
dc_italy.set_xlabel("Years", fontsize=30)
dc_italy.set_ylabel("Life expectancy for retired people", fontsize=30)

dc_italy.head()
dc_sweden.plot.line(x='YEAR', y='PFUND')
dc_denmark.plot.line(x='YEAR', y='PFUND')
dc_spain.plot.line(x='YEAR', y='PFUND')
####
dc_italy.plot(x='YEAR', y=['MRET','FRET'])
####
dc_italy.plot(x='YEAR', y=['LEXP65', 'MRET','FRET'])
dc_sweden.plot(x='YEAR', y=['LEXP65', 'MRET','FRET'])
dc_denmark.plot(x='YEAR', y=['LEXP65', 'MRET','FRET'])
dc_spain.plot(x='YEAR', y=['LEXP65', 'MRET','FRET'])
####
cwed.plot(x="YEAR", y="PQUAL", kind='scatter')

#################################################
##DATA FROM OECD ON PUBLIC DEBT
oecd= pd.read_csv("./general_gov_debt_OECD.csv")
oecd.head()
do=pd.DataFrame(oecd)
print(do)
location= do.groupby(do.LOCATION)
do_italy=location.get_group('ITA')
do_italy.plot.line(x='TIME', y='Value', figsize=(80, 60), fontsize=70,lw=5)
plt.xlabel("Years", fontsize=120)
plt.ylabel("Public debt", fontsize=120)
#public debt of italy
debt_italy.show()
##Spain debt
do_spain= location.get_group('ESP')
debt_spain= do_spain.plot.line(x='TIME', y='Value', figsize=(20, 16), fontsize=15,)
debt_spain.legend(["Spain"], fontsize=20);
debt_spain.set_xlabel("Years", fontsize=30)
debt_spain.set_ylabel("Debt as % GDP", fontsize=30)
debt_spain.show()
####public pensions
p_p= pd.read_csv("/home/emilio/Desktop/py_research_notes/datasets/long_public_pensions_OECD.csv")
print(p_p)
p_p.head()
location=do.groupby(p_p.LOCATION)
print(location)

pe_italy= location.get_group('ITA')
pens_italy= pe_italy.plot.line(x='TIME', y='Value', figsize=(20, 16), fontsize=15,)
pens_italy.legend(["Italy"], fontsize=20);
pens_italy.set_xlabel("Years", fontsize=30)
pens_italy.set_ylabel("Public pensions spending for average retired person", fontsize=30)
pens_italy.show()

print(pe_italy)

#########################à
##private pensions
private = pd.read_csv('./private_pensions_OECD.csv')
private.head()
location=private.groupby(private.LOCATION)
pr_ita=location.get_group('ITA')
pr_ita.plot(x='TIME', y='Value')
########################################
##EUROSTAT - pension expenditure as % of GrossDomesticProduct
##########################################
os.getcwd()
eurostat = pd.read_excel('.\eurostata_pension.xlsx')
print(eurostat)
eurostat.head()
eurostat.plot(x = 'Time', y= ['Italy','Spain', 'Sweden', 'Denmark'], figsize=(80, 60),lw=6, fontsize=60,) 
plt.xlabel('Time',fontsize=120)
plt.ylabel('Pension expenditure',fontsize=120)
plt.legend(fontsize=75)

####PAMPEL INDEX with eurostat data from 2010 to 2020
pampel =pd.read_excel('./pampel_index.xlsx')
pampel.head()
pampel.plot(x='TIME', y=['Italy','Sweden','Spain','Denmark','Netherlands','Switzerland', 'European Union'],figsize=(80,60), lw=7, fontsize=60)
plt.xlabel('Time', fontsize=120)
plt.ylabel('Average pension', fontsize=120)
plt.legend(fontsize=85)




