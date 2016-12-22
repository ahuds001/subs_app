from flask import Flask,render_template,request
from subs import *
app = Flask(__name__)
##app.vars={}

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('userinfo.html')
    if request.method=='POST':
        nbr_of_players = request.form['nbr_of_players']
        nbr_on_field = request.form['nbr_on_field']
        time_in_half = request.form['time_in_half']
        nbr_subs_at_a_time = request.form['nbr_subs_at_a_time']

        ##app.vars['nbr_of_players'] = request.form['nbr_of_players']
        ##app.vars['nbr_on_field'] = request.form['nbr_on_field']
        ##app.vars['time_in_half'] = request.form['time_in_half']
        ##app.vars['nbr_subs_at_a_time'] = request.form['nbr_subs_at_a_time']

        value_list = [0,1]
        sub_in_pop={}
        sub_out_pop={}
        sub_out= 0
        sub_in = 0
        counter=0

        ##nbr_of_players = app.vars['nbr_of_players']
        ##nbr_on_field = app.vars['nbr_on_field']
        ##time_in_half = app.vars['time_in_half']
        ##nbr_subs_at_a_time = app.vars['nbr_subs_at_a_time']
        bad_input_error=""
        ## Input Errors
        try:
            nbr_of_players=int(nbr_of_players)
        except:
            bad_input_error = "Nbr of Players must be an Integer"
        try:
            nbr_on_field=int(nbr_on_field)
        except:
            bad_input_error = "Nbr on Field must be an Integer"
        try:
            time_in_half=float(time_in_half)
        except:
            bad_input_error = "Time in Half must be an Float"
        try:
            nbr_subs_at_a_time=int(nbr_subs_at_a_time)
        except:
            bad_input_error = "Nbr of Subs must be an Integer"
        if bad_input_error=="":
            ## Other Errors
            if nbr_on_field>nbr_of_players:
                bad_input_error = "Error, you need more players"
                return render_template('error.html',
                                    error = bad_input_error)
            elif time_in_half<5:
                bad_input_error = "Time in half is too short"
                return render_template('error.html',
                                    error = bad_input_error)
            elif nbr_subs_at_a_time>2:
                bad_input_error = "Don't have that functionality yet"
                return render_template('error.html',
                                    error = bad_input_error)
            elif (nbr_of_players%nbr_subs_at_a_time)+(nbr_on_field%nbr_subs_at_a_time)!=0:
                bad_input_error = "You can't do two subs at a time when you have odd subs"
                return render_template('error.html',
                                    error = bad_input_error)
            ## All errors account for I think
            else:
                people = dict(zip([x+1 for x in range(nbr_of_players)],[0]*nbr_of_players))
                on_field = [x+1 for x in range(nbr_on_field)]
                if nbr_subs_at_a_time==1:
                    output = one_sub_calcuations(value_list,people,on_field,counter,time_in_half)
                elif nbr_subs_at_a_time==2:
                    output = two_sub_calcuations(value_list,people,on_field,counter,time_in_half)
                print(output)
                return render_template('layout.html',
                                        counter=output['counter'],
                                        people=output['people'],
                                        person_time=output['person_time'],
                                        sub_time=output['sub_time'])
        else:
            return render_template('error.html',
                                error = bad_input_error)
if __name__ == "__main__":
    app.run(debug=True)
