def update_field(people,on_field):
    sub_in_pop={}
    sub_out_pop={}
    for key in people.keys():
        if key in on_field:
            people[key]=people[key]+1
            sub_out_pop[key]=people[key]
        else:
            sub_in_pop[key]=people[key]
    return people,sub_out_pop,sub_in_pop

def pick_sub(people,sub_in_pop,sub_out_pop):
    sub_out= 0
    sub_in = 0
    for key in people.keys():
        if key in sub_out_pop.keys():
            ## return key of max dict value
            if sub_out==0:
                sub_out = key
            elif sub_out_pop[key]>sub_out_pop[sub_out]:
                sub_out = key
        if key in sub_in_pop.keys():
            ## return key of min dict value
            if sub_in==0:
                sub_in = key
            elif sub_in_pop[key]<sub_in_pop[sub_in]:
                sub_in = key
    return sub_out, sub_in

def pick_two_subs(people,sub_in_pop,sub_out_pop):
    sub_out= [0,0]
    sub_in = [0,0]
    for key in people.keys():
        if key in sub_out_pop.keys():
            ## return key of max dict value
            if 0 in sub_out:
                sub_out.pop(0)
                sub_out.append(key)
            elif sub_out_pop[key]>sub_out_pop[sub_out[0]]:
                sub_out[0] = key
            elif sub_out_pop[key]>sub_out_pop[sub_out[1]]:
                sub_out[1] = key
        if key in sub_in_pop.keys():
            ## return key of min dict value
            if 0 in sub_in:
                sub_in.pop(0)
                sub_in.append(key)
            elif sub_in_pop[key]<sub_in_pop[sub_in[0]]:
                sub_in[0] = key
            elif sub_in_pop[key]<sub_in_pop[sub_in[1]]:
                sub_in[1] = key
    return sub_out, sub_in

def substitution(on_field,sub_out,sub_in):
    if type(sub_in)==list:
        on_field = [person for person in on_field if person not in sub_out]
        on_field = on_field + sub_in
    else:
        on_field = [person for person in on_field if person!=sub_out]
        on_field.append(sub_in)
    return on_field

## One substitution system. Is mathematically trivial
def one_sub_calcuations(value_list,people,on_field,counter,time_in_half):
    while max(value_list)!=min(value_list):
        people,sub_out_pop,sub_in_pop = update_field(people,on_field)
        sub_out,sub_in = pick_sub(people,sub_in_pop,sub_out_pop)
        on_field = substitution(on_field,sub_out,sub_in)
        value_list = [value for value in people.values()]
        counter+=1
        if counter==25:
            break
    if counter==25:
        print("The values entered do not allow the function to converge. Try again!")
    else:
        half = time_in_half
        minutes_available = people[1]*half
        sub_mins = str(divmod(half,counter)[0])
        sub_secs = str(divmod(half,counter)[1])
        if len(sub_secs)==3:
            sub_secs="0"+sub_secs
        person_mins = str(divmod(minutes_available,counter)[0])
        person_secs = str(divmod(minutes_available,counter)[1])
        if len(person_secs)==3:
            person_secs="0"+person_secs
        ##print("The number of rotations is: {}".format(counter))
        ##print("The number of times each player will play is: {}".format(people[1]))
        ##print("The number of minutes each player will play is: {}:{}".format(person_mins,person_secs))
        ##print("The amount of time for a substitution is: {}:{}".format(sub_mins,sub_secs))
        person_mins = person_mins[0:person_mins.find(".")]
        person_secs = person_secs[0:person_secs.find(".")]
        sub_mins = sub_mins[0:sub_mins.find(".")]
        sub_secs = sub_secs[0:sub_secs.find(".")]
        output = {'counter':counter,
                'people':people[1],
                'person_time':person_mins+":"+person_secs,
                'sub_time':sub_mins+":"+sub_secs}
        return output
## Two substitutions, doesn't converge unless all evens
def two_sub_calcuations(value_list,people,on_field,counter,time_in_half):
    while max(value_list)!=min(value_list):
        people,sub_out_pop,sub_in_pop = update_field(people,on_field)
        sub_out,sub_in = pick_two_subs(people,sub_in_pop,sub_out_pop)
        on_field = substitution(on_field,sub_out,sub_in)
        value_list = [value for value in people.values()]
        counter+=1
        if counter==50:
            break
    if counter==50:
        print("The values entered do not allow the function to converge. Try again!")
    else:
        half = time_in_half
        minutes_available = people[1]*half
        sub_mins = str(divmod(half,counter)[0])
        sub_secs = str(divmod(half,counter)[1])
        if len(sub_secs)==3:
            sub_secs="0"+sub_secs
        person_mins = str(divmod(minutes_available,counter)[0])
        person_secs = str(divmod(minutes_available,counter)[1])
        if len(person_secs)==3:
            person_secs="0"+person_secs
        ##print("The number of rotations is: {}".format(counter))
        ##print("The number of times each player will play is: {}".format(people[1]))
        ##print("The number of minutes each player will play is: {}:{}".format(person_mins,person_secs))
        ##print("The amount of time for a substitution is: {}:{}".format(sub_mins,sub_secs))
        person_mins = person_mins[0:person_mins.find(".")]
        person_secs = person_secs[0:person_secs.find(".")]
        sub_mins = sub_mins[0:sub_mins.find(".")]
        sub_secs = sub_secs[0:sub_secs.find(".")]
        output = {'counter':counter,
                'people':people[1],
                'person_time':person_mins+":"+person_secs,
                'sub_time':sub_mins+":"+sub_secs}
        return output
