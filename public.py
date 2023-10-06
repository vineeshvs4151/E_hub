from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
    return render_template('index.html')

@public.route('/register',methods=['get','post'])
def register():
    if 'submit' in request.form:
        first=request.form['fname']
        second = request.form['lname']
        dob = request.form['DOB']
        gender = request.form['gender']
        qualification =request.form['qual']
        phone =request.form['phone']
        emailid =request.form['email']
        username = request.form['uname']
        password = request.form['password']
        q="select username,password from login where username ='%s' and password='%s'" %(username,password)
        print(q)
        result=select(q)

        if len(result)>0:
            flash("That username and password already exist")
        else:
            q="insert into login values(null,'%s','%s','employee')"%(username,password)
            res=insert(q)
            q="insert into employee values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,first,second,dob,gender,qualification,phone,emailid)
            insert(q)
            flash("Successfully Registered")

    return render_template('employee_register.html')

@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
         username = request.form['uname']
         password = request.form['password']
         q="select * from login where username='%s' and password ='%s'"%(username, password)
         res=select(q)

         if res:
            session['login_id']=res[0]['login_id']
            if res[0]['usertype']=="admin":
                flash("login successfully")
                return redirect(url_for('admin.adminhome'))
            if res[0]['usertype'] == "employee":
                flash("login successfully")
                return redirect(url_for('employees.employeeshome'))
    return render_template('login.html')