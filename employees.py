from flask import *
from database import *
employees=Blueprint('employees',__name__)

@employees.route('/employeeshome',methods=['get','post'])
def employeeshome():
    return render_template('employeeshome.html')

@employees.route('/viewmyprofile',methods=['get','post'])
def viewmyprofile():
    data={}
    ids=session['login_id']
    q="select * from employee where login_id='%s'"%(ids)
    res=select(q)
    data['my']=res
    return render_template('employviewprofile.html',data=data)

@employees.route('/updatejob',methods=['get','post'])
def updatejob():
    return render_template('employeesjobupdate.html')


@employees.route('/applyjob',methods=['get','post'])
def applyjob():
    return render_template('employeesjobapply.html')

@employees.route('/feedback',methods=['get','post'])
def feeback():
    return render_template('employeesfeedback.html')
