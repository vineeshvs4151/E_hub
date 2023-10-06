from flask import *
employer=Blueprint('employer',__name__)
@employer.route('/employerhome',methods=['get','post'])
def employerhome():
    return render_template('employerhome.html')
