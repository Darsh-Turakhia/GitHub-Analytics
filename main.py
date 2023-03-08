import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

issue = pd.read_csv("Issues Y-O-Y.csv",delimiter=",")
pr = pd.read_csv("PRs Y-O-Y.csv",delimiter=",")
repo = pd.read_csv("Repos Y-O-Y.csv",delimiter=",")
total = pd.read_csv("Year Total.csv",delimiter=",")

yr = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

issue_count = total['Issues']
pr_count = total['PRs']
ilang_count = total['I Lang']
prlang_count = total['PR Lang']

#year issues per year
def issue_per_year():
    plt.bar(yr,issue_count)
    plt.ylabel("Number of Issues")
    plt.xlabel("Year Number")
    plt.title("Issues per Year")
    for index, value in enumerate(issue_count):
        plt.text(index, value, str(value))
    plt.show()

#year prs per year
def prs_per_year():
    plt.bar(yr,pr_count)
    plt.ylabel("Number of Pull Requests")
    plt.xlabel("Year Number")
    plt.title("Pull Requests per Year")
    for index, value in enumerate(pr_count):
        plt.text(index, value, str(value))
    plt.show()

#year issue language per year
def issue_language_per_year():
    plt.bar(yr,ilang_count)
    plt.ylabel("Number of Issues")
    plt.xlabel("Year Number")
    plt.title("Languages in which issue were raised per Year")
    for index, value in enumerate(ilang_count):
        plt.text(index, value, str(value))
    plt.show()

#year pr language per year
def pr_language_per_year():
    plt.bar(yr,prlang_count)
    plt.ylabel("Number of Issues")
    plt.xlabel("Year Number")
    plt.title("Languages in PRs were created per Year")
    for index, value in enumerate(prlang_count):
        plt.text(index, value, str(value))
    plt.show()

#print count of all unique languages in which PR were created
def find_unique_pr_language():
    yr = int(input("\n Enter year number (YYYY) : "))
    if yr == 2011:
        print("\n The number of unique languages in 2011 is :",pr['YR-2011'][pr['YR-2011'] != 0].count())
    elif yr == 2012:
        print("\n The number of unique languages in 2012 is :",pr['YR-2012'][pr['YR-2012'] != 0].count())
    elif yr == 2013:
        print("\n The number of unique languages in 2013 is :",pr['YR-2013'][pr['YR-2013'] != 0].count())
    elif yr == 2014:
        print("\n The number of unique languages in 2014 is :",pr['YR-2014'][pr['YR-2014'] != 0].count())
    elif yr == 2015:
        print("\n The number of unique languages in 2015 is :",pr['YR-2015'][pr['YR-2015'] != 0].count())
    elif yr == 2016:
        print("\n The number of unique languages in 2016 is :",pr['YR-2016'][pr['YR-2016'] != 0].count())
    elif yr == 2017:
        print("\n The number of unique languages in 2017 is :",pr['YR-2017'][pr['YR-2017'] != 0].count())
    elif yr == 2018:
        print("\n The number of unique languages in 2018 is :",pr['YR-2018'][pr['YR-2018'] != 0].count())
    elif yr == 2019:
        print("\n The number of unique languages in 2019 is :",pr['YR-2019'][pr['YR-2019'] != 0].count())
    elif yr == 2020:
        print("\n The number of unique languages in 2020 is :",pr['YR-2020'][pr['YR-2020'] != 0].count())
    elif yr == 2021:
        print("\n The number of unique languages in 2021 is :",pr['YR-2021'][pr['YR-2021'] != 0].count())
    else:
        print("\n The number of unique languages used in time-frame is :",pr['Language'].count())

#print count of all unique languages in which issues were created
def find_unique_issues_language():
    yr = int(input("\n Enter year number (YYYY) : "))
    if yr == 2011:
        print("\n The number of unique languages in 2011 is :",issue['YR-2011'][issue['YR-2011'] != 0].count())
    elif yr == 2012:
        print("\n The number of unique languages in 2012 is :",issue['YR-2012'][issue['YR-2012'] != 0].count())
    elif yr == 2013:
        print("\n The number of unique languages in 2013 is :",issue['YR-2013'][issue['YR-2013'] != 0].count())
    elif yr == 2014:
        print("\n The number of unique languages in 2014 is :",issue['YR-2014'][issue['YR-2014'] != 0].count())
    elif yr == 2015:
        print("\n The number of unique languages in 2015 is :",issue['YR-2015'][issue['YR-2015'] != 0].count())
    elif yr == 2016:
        print("\n The number of unique languages in 2016 is :",issue['YR-2016'][issue['YR-2016'] != 0].count())
    elif yr == 2017:
        print("\n The number of unique languages in 2017 is :",issue['YR-2017'][issue['YR-2017'] != 0].count())
    elif yr == 2018:
        print("\n The number of unique languages in 2018 is :",issue['YR-2018'][issue['YR-2018'] != 0].count())
    elif yr == 2019:
        print("\n The number of unique languages in 2019 is :",issue['YR-2019'][issue['YR-2019'] != 0].count())
    elif yr == 2020:
        print("\n The number of unique languages in 2020 is :",issue['YR-2020'][issue['YR-2020'] != 0].count())
    elif yr == 2021:
        print("\n The number of unique languages in 2021 is :",issue['YR-2021'][issue['YR-2021'] != 0].count())
    else:
        print("\n The number of unique languages used in time-frame is :",issue['Language'].count())

#print list of all unique languages in which PR were created
def print_unique_pr_language():
    yr = int(input("\n Enter year number (YYYY) : "))
    if yr == 2011:
        print("\n The number of unique languages in 2011 are :\n",pr[pr['YR-2011'] != 0]['Language'])
    elif yr == 2012:
        print("\n The number of unique languages in 2012 are :\n",pr[pr['YR-2012'] != 0]['Language'])
    elif yr == 2013:
        print("\n The number of unique languages in 2013 are :\n",pr[pr['YR-2013'] != 0]['Language'])
    elif yr == 2014:
        print("\n The number of unique languages in 2014 are :\n",pr[pr['YR-2014'] != 0]['Language'])
    elif yr == 2015:
        print("\n The number of unique languages in 2015 are :\n",pr[pr['YR-2015'] != 0]['Language'])
    elif yr == 2016:
        print("\n The number of unique languages in 2016 are :\n",pr[pr['YR-2016'] != 0]['Language'])
    elif yr == 2017:
        print("\n The number of unique languages in 2017 are :\n",pr[pr['YR-2017'] != 0]['Language'])
    elif yr == 2018:
        print("\n The number of unique languages in 2018 are :\n",pr[pr['YR-2018'] != 0]['Language'])
    elif yr == 2019:
        print("\n The number of unique languages in 2019 are :\n",pr[pr['YR-2019'] != 0]['Language'])
    elif yr == 2020:
        print("\n The number of unique languages in 2020 are :\n",pr[pr['YR-2020'] != 0]['Language'])
    elif yr == 2021:
        print("\n The number of unique languages in 2021 are :\n",pr[pr['YR-2021'] != 0]['Language'])
    else:
        print("\n The number of unique languages used in time-frame are :\n",pr['Language'])

#print list of all unique languages in which issues were created
def print_unique_issues_language():
    yr = int(input("\n Enter year number (YYYY) : "))
    if yr == 2011:
        print("\n The number of unique languages in 2011 are :\n",issue[issue['YR-2011'] != 0]['Language'])
    elif yr == 2012:
        print("\n The number of unique languages in 2012 are :\n",issue[issue['YR-2012'] != 0]['Language'])
    elif yr == 2013:
        print("\n The number of unique languages in 2013 are :\n",issue[issue['YR-2013'] != 0]['Language'])
    elif yr == 2014:
        print("\n The number of unique languages in 2014 are :\n",issue[issue['YR-2014'] != 0]['Language'])
    elif yr == 2015:
        print("\n The number of unique languages in 2015 are :\n",issue[issue['YR-2015'] != 0]['Language'])
    elif yr == 2016:
        print("\n The number of unique languages in 2016 are :\n",issue[issue['YR-2016'] != 0]['Language'])
    elif yr == 2017:
        print("\n The number of unique languages in 2017 are :\n",issue[issue['YR-2017'] != 0]['Language'])
    elif yr == 2018:
        print("\n The number of unique languages in 2018 are :\n",issue[issue['YR-2018'] != 0]['Language'])
    elif yr == 2019:
        print("\n The number of unique languages in 2019 are :\n",issue[issue['YR-2019'] != 0]['Language'])
    elif yr == 2020:
        print("\n The number of unique languages in 2020 are :\n",issue[issue['YR-2020'] != 0]['Language'])
    elif yr == 2021:
        print("\n The number of unique languages in 2021 are :\n",issue[issue['YR-2021'] != 0]['Language'])
    else:
        print("\n The number of unique languages used in time-frame are :\n",issue['Language']['Language'])

#menu to display options
def menu():
    while 1:
        print("\n")
        print("1) Graph for Issues per year")
        print("2) Graph for PRs per year")
        print("3) Graph for Issues language per year")
        print("4) Graph for PRs language per year")
        print("5) Count of Unique Languages in PR as per year")
        print("6) Count of Unique Languages in Issue as per year")
        print("7) List of Unique Languages in PR as per year")
        print("8) List of Unique Languages in Issue as per year")
        print("0) Exit")
        choice = int(input(" Enter your choice : "))
        if choice == 1:
            issue_per_year()
        elif choice == 2:
            prs_per_year()
        elif choice == 3:
            issue_language_per_year()
        elif choice == 4:
            pr_language_per_year()
        elif choice == 5:
            find_unique_pr_language()
        elif choice == 6:
            find_unique_issues_language()
        elif choice == 7:
            print_unique_pr_language()
        elif choice == 8:
            print_unique_issues_language()
        elif choice == 0:
            break
        else:
            print(" Invalid Choice !!! ")

#main function
menu()