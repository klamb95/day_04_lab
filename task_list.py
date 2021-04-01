#import pdb

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def umcompleted_tasks(list):
    #pdb.set_trace()
    uncompleted_task = []
    for task in list:
        if task["completed"] == False:
            uncompleted_task.append(task)
    return uncompleted_task
    
