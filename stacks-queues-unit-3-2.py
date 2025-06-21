# Problem 1: Manage Performance Stage Changes

def manage_stage_changes(changes):
    stack = []
    last_removed = ""
    for change in changes:
        change = change.split()
        if change[0] == "Schedule":
            stack.append(change[1])
        elif change[0] == "Cancel":
            last_removed = stack.pop()
        elif change[0] == "Reschedule":
            stack.append(last_removed)
    return stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
        