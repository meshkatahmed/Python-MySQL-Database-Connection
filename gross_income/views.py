from django.shortcuts import render
from .models import HighestMonthlyGrossIncome
from django.http import HttpResponse
import pymysql
# Create your views here.
connection = pymysql.connections.Connection(host='localhost',
                         user='root',
                         password='',
                         database='bizdata_insights_database',
                         cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
sql = "SELECT MONTHNAME(Date) AS month,MAX(`gross income`) AS highest_gross_income FROM bizdata_backend_testdata GROUP BY month"
cursor.execute(sql)
result = cursor.fetchall()
def home(request):
    diction = {'results':result}
    return render(request,'gross_income\home.html',context=diction)
def highest_monthly_gross_income(request):
    model = HighestMonthlyGrossIncome()
    for item in result:
        print(item['month'],item['highest_gross_income'])
        model.month = item['month']
        model.highest_gross_income = item['highest_gross_income']
        model.save()
    return HttpResponse('Data saved successfully')
