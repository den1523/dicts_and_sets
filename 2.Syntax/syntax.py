def make_user(name, age):
    dict = {name: age}
    return dict
    
def format_user(phil):
    for k, v in phil.items():
        return f'{k}, {v}'
