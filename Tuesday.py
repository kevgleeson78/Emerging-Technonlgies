# Tuesday checker with if statements

import datetime

today = datetime.date.today()

dayOfWeek = today.weekday()

if dayOfWeek == 1:
    print("It's Tuesday")
elif dayOfWeek == 0:
    print("Tomorrow is Tuesday")
elif dayOfWeek == 2:
    print("Yesterday was Tuesday")
else:
    print("It's not Tuesday")