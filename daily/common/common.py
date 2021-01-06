def get_main(item):
    return {
        'id': item.id,
        'date': item.date,
        'evaluation': item.evaluation.evaluation,
    }

def get_all(item):
    return {
        'id': item.id,
        'date': item.date,
        'univ': item.univ,
        'study': item.study,
        'other': item.other,
        'first_meet': item.first_meet,
        'wanna_do': item.wanna_do,
        'summary': item.summary,
    }

def get_univ(item):
    return {
        'date': item.date, 
        'univ': item.univ, 
        'is_open': item.isOpen, 
    }

def get_study(item):
    return {
        'date': item.date, 
        'study': item.study, 
        'is_open': item.isOpen, 
    }

def get_other(item):
    return {
        'date': item.date, 
        'other': item.other, 
        'is_open': item.isOpen, 
    }

def get_first_meet(item):
    return {
        'date': item.date, 
        'first_meet': item.first_meet, 
        'is_open': item.isOpen, 
    }

def get_wanna_do(item):
    return {
        'date': item.date, 
        'wanna_do': item.wanna_do, 
        'is_open': item.isOpen, 
    }

def get_summary(item):
    return {
        'date': item.date, 
        'summary': item.summary, 
        'is_open': item.isOpen, 
    }

category_dict = {
    'univ': get_univ,
    'study': get_study,
    'other': get_other, 
    'first_meet': get_first_meet, 
    'wanna_do': get_wanna_do, 
    'summary': get_summary,
}