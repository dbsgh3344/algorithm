import operator

def solution(tables, langs, prefer) :
    dicts = {i:j for i,j, in zip(langs,prefer)}
    job_score = {table.split()[0] : 0 for table in sorted(tables)}
    
    for i in range(len(tables)) :
        job_lang = tables[i].split()
        
        score = 0
        for lang in langs :
            if lang in job_lang:
                lang_score=5- (job_lang.index(lang))+1
                score += dicts[lang]*lang_score

        
        job_score[tables[i].split()[0]] = score
        score=0

    return  max(job_score.items(),key=operator.itemgetter(1))[0]  


if __name__ == "__main__":
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]


    langs =  ["JAVA", "JAVASCRIPT"]
    prefer =  [7, 5]

    print(solution(table,langs,prefer))

    solution2 = lambda t, l, p: sorted((sum(p[l.index(u)] * (i - 5) if u in l else 0 for i, u in enumerate(v)), k) for k, *v in (b.split() for b in t))[0][1]
    print(solution2)