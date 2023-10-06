from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
    return render_template('adminhome.html')

@admin.route('/viewemployees',methods=['get','post'])
def viewemployees():
    data={}
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        id1=request.args['id1']
    else:
        action=None
    if action=='delete':
        q="delete from employee where employee_id='%s'"%(id)
        delete(q)
        q="delete from login where login_id='%s'"%(id1)
        delete(q)
        return redirect(url_for('admin.viewemployees'))
    q="select * from employee"
    res=select(q)
    data['emp']=res
    return render_template('adminviewemployees.html',data=data)

@admin.route('/viewemployers',methods=['get','post'])
def viewemployers():
    return render_template('adminviewemployers.html')

@admin.route('/viewfeedback',methods=['get','post'])
def viewfeedback():
    return render_template('adminviewfeedback.html')

@admin.route('/managejob',methods=['get','post'])
def managejob():
    return render_template('adminmanagejob.html')