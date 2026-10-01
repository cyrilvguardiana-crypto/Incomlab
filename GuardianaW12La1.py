GuardianaSalary = {"E104":{
"EmpName": [8,9,8,5,10,8]
},
"E601": {
"EmpName": "Kane Clover",
"DailyHrs": [9,10,8,8,9]
}
}
emp_id = input("Enter employee name")
if emp_id not in GuardianaSalary:
    print("Not Found")
else:
    employee = GuardianaSalary[emp_id]
    emp_name = employee["EmpName"]
    daily_hrs = employee["DailyHrs"]

    print(f"Name: {emp_name}")
    print(f"DutyHour: {daily_hrs}")

    Guardianabasic = 9000
    Guardianaperhour = Guardianabasic / 40

    Guardiana_total = sum(daily_hrs)

    guardianatime = 0
    for hrs in daily_hrs:
        if hrs > 8:
            excess = hrs - 8
            guardianatime += excess * (1.5 * Guardianaperhour)


    Guardianagross = (40 * Guardianaperhour) + guardianatime

    print(f"Total Hour: {Guardiana_total}")
    print(f"Overtime:  {guardianatime}")
    print(f"Gross Pay: {Guardianagross}")
