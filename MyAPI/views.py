from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from . forms import ApprovalForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from . models import approvals
from . serializers import approvalsSerializers
import pickle
from keras import backend as K
import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter



class ApprovalsView(viewsets.ModelViewSet):
	queryset = approvals.objects.all()
	serializer_class = approvalsSerializers

"""def ohevalue(df):
	ohe_col=joblib.load("/Users/USER/Desktop/allcol.pkl")
	cat_columns=['Gender','Married','Education','Self_Employed','Property_Area']
	df_processed = pd.get_dummies(df, columns=cat_columns)
	newdict={}
	for i in ohe_col:
		if i in df_processed.columns:
			newdict[i]=df_processed[i].values
		else:
			newdict[i]=0
	newdf=pd.DataFrame(newdict)
	return newdf
"""




def approvereject(unit):
	try:
		mdl=joblib.load("MyAPI/Customer_Segmentation_Model.pkl")
		scalers=joblib.load("MyAPI/Cluster1.pkl")
		X=scalers.transform(unit)
		y_pred=mdl.predict(X)
		#y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Cluster'])
		newdf=newdf.replace({0:'Cluster (0) lower mean of credit amount, short duration, older customers', 1:'Cluster (1) high mean of credit amount, long duration, middle-aged customers',2:'Cluster (2) lower mean of credit amount, short duration, young customers'})
		K.clear_session()
		return (newdf.values[0][0])
	except ValueError as e:
		return (e.args[0])

def cxcontact(request):
	if request.method=='POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
				Age = form.cleaned_data['Age']
				CreditAmount = form.cleaned_data['CreditAmount']
				Duration = form.cleaned_data['Duration']
				myDict = (request.POST).dict()
				del myDict["csrfmiddlewaretoken"]
				del myDict["Firstname"]
				del myDict["Lastame"]
				del myDict["Gender"]
				del myDict["Housing"]
				del myDict["SavingAccount"]
				del myDict["CheckingAccount"]
				del myDict["Purpose"]

				df=pd.DataFrame(myDict, index=[0])
				#print(df)
				#answer=approvereject(ohevalue(df)) # OHE ==> One Hot Encoder
				answer=approvereject(df)
				messages.success(request,'Customer Categorie: \n {}'.format(answer))

	form=ApprovalForm()

	return render(request, 'MyForm/cxform.html', {'form':form})
