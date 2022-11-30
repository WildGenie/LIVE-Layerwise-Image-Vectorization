import os
import os.path as osp

def get_experiment_id(debug=False):
    if debug:
        return 999999999999
    import time
    time.sleep(0.5)
    return int(time.time()*100)

def get_path_schedule(type, **kwargs):
    if type == 'exp':
        import math
        base = kwargs['base']
        max_path = kwargs['max_path']
        max_path_per_iter = kwargs['max_path_per_iter']
        schedule = []
        cnt = 0
        while sum(schedule) < max_path:
            proposed_step = min(
                max_path - sum(schedule), 
                base**cnt, 
                max_path_per_iter)
            cnt += 1
            schedule += [proposed_step]
        return schedule
    elif type == 'list':
        return kwargs['schedule']
    elif type == 'repeat':
        return [kwargs['schedule_each']] * kwargs['max_path']
    else:
        raise ValueError

def edict_2_dict(x):
    if isinstance(x, dict):
        return {k: edict_2_dict(x[k]) for k in x}
    elif isinstance(x, list):
        return [edict_2_dict(x[i]) for i in range(len(x))]
    else:
        return x

def check_and_create_dir(path):
    pathdir = osp.split(path)[0]
    if not osp.isdir(pathdir):
        os.makedirs(pathdir)
