import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    t_dict = {i.split()[0]:i.split()[1] for i in terms}

    for i in range(len(privacies)):
        t_type=privacies[i].split()[1]
        dt=datetime.datetime.strptime(privacies[i].split()[0],'%Y.%m.%d')
        td=relativedelta(months=+int(t_dict[t_type]))
        if today >=datetime.datetime.strftime(dt+td,'%Y.%m.%d'):
            answer.append(i+1)

    return answer



td= "2022.05.19"
terms =["A 6", "B 12", "C 3"]	
pr= ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
solution(td,terms,pr)