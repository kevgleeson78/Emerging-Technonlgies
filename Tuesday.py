# Tuesday checker with if statements

import datetime

today = datetime.date.today()

dayOfWeek = today.weekday()

if dayOfWeek == 1:
    print("It's Tuesday")
else:
    print("It's not Tuesday")