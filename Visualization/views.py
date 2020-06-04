from django.shortcuts import render
import pandas as pd
# Create your views here.

def indexPage(request):
    data = pd.read_csv("german_credit_data.csv")

    TotalRows=data[data.columns[0]].count()
    TotalCredit = data[data.columns[7]].sum()

    n_credits = data.groupby("Purpose")["Age"].count().rename("Count").reset_index()
    n_credits.sort_values(by=["Count"], ascending=False, inplace=True)
    x=n_credits['Purpose'].values.tolist()
    y=n_credits['Count'].values.tolist()

    credits = data.groupby("Sex")["CreditAmount"].sum().reset_index()
    x1=credits['Sex'].values.tolist()
    y1=credits['CreditAmount'].values.tolist()


    context={'TotalRows':TotalRows , 'TotalCredit':TotalCredit , 'x':x , 'y':y , 'x1':x1 , 'y1':y1 }
    return render(request,'index.html',context)
