# 13. Вывести список отделов со средним налогом на сотрудников этого отдела.
# 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
# """






departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

def all_nalog_departments(departments, taxes):
    all_nalog ={}
    print('Cписок отделов со средним налогом на сотрудников этого отдела:')
    for department in departments:
        nalog_dep = 0
        for taxe in taxes:
            if str(taxe["department"]).lower() == str(department["title"]).lower() or taxe["department"] is None :
                nalog_dep += taxe['value_percents']
        print(department['title'], nalog_dep)
        all_nalog[department['title']] = nalog_dep
    print()
    return all_nalog




def salary_worker(departments, nalog):
    nalog_barden_depart_dict ={}
    nalog_bardtn_worker_dict = {}
    print('Cписок всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов:')
    for department in departments:
        nalog_barden = 0
        for worker in department["employers"]:
            nalog_bardtn_worker = 0
            print(worker["first_name"], worker['last_name'], worker["salary_rub"], int(worker['salary_rub']+(worker['salary_rub']*0.01*nalog[department['title']])))
            nalog_bardtn_worker = int(worker['salary_rub']+(worker['salary_rub']*0.01*nalog[department['title']])) - worker["salary_rub"]
            nalog_barden += nalog_bardtn_worker
            name = worker['last_name'] + ' ' + worker['first_name']
            nalog_bardtn_worker_dict[name] = nalog_bardtn_worker
        nalog_barden_depart_dict[department['title']] = nalog_barden
    print()
    return(nalog_barden_depart_dict, nalog_bardtn_worker_dict)



def sort_nalog_department(nalog_barden_dict):
    print('Cписок отделов, отсортированный по месячной налоговой нагрузки:')
    sort_nalog_barden_dict = dict(sorted(nalog_barden_dict.items(), key=lambda item: item[1], reverse=True))
    for key, value in sort_nalog_barden_dict.items():
        print(key, value)
    print()




def nalog_year(nalog_bardtn_worker):
    print('Все сотрудников, за которых компания платит больше 100к налогов в год:')
    for key, value in nalog_bardtn_worker.items():
        if value*12 >= 100000:
            print(key)
    print()


def min_nalog_worker(nalog_bardtn_worker):
    min_nalog_worker = list(nalog_bardtn_worker.values())[0]
    for key, value in nalog_bardtn_worker.items():
        if value <= min_nalog_worker:
            min_nalog_worker = value
            name_min_nalog_worker = key
    print(f'Сотрудник, за которого компания платит меньше всего налогов: {name_min_nalog_worker}')
    print()

        




# def sort_nalog_departments(departments, nalog):
#     nalog_dep_dict = {}
#     for department in departments:
#         nalog_dep = sum([for salary])



if __name__ == "__main__":
    nalog = all_nalog_departments(departments, taxes)
    nalog_bardth = salary_worker(departments, nalog)
    nalog_bardth_department = nalog_bardth[0]
    nalog_bardth_worker = nalog_bardth[1]
    sort_nalog_department(nalog_bardth_department)
    nalog_year(nalog_bardth_worker)
    min_nalog_worker(nalog_bardth_worker)
    