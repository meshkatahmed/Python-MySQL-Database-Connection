from django.shortcuts import render
from .models import HighestMonthlyGrossIncome
import pymysql
# Create your views here.

def home(request):
    connection = pymysql.connections.Connection(host='localhost',
                             user='root',
                             password='',
                             database='bizdata_insights_database',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql = "SELECT MONTHNAME(Date) AS month,MAX(`gross income`) AS highest_gross_income FROM bizdata_backend_testdata GROUP BY month"
    cursor.execute(sql)
    result = cursor.fetchall()
    model = HighestMonthlyGrossIncome()
    for item in result:
        model.month = item['month']
        model.highest_gross_income = item['highest_gross_income']
        model.save()
    diction = {'results':result}
    return render(request,'gross_income\home.html',context=diction)
