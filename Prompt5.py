### Collection of Logic Programming Prompts
### Author: Viveka Cheekati
### Date: 11/21/2024

## Prompt 5.
## Design a program to allocate resources to projects based on skill match and availability. 
## The program should:
resources_data = [
    {"resource_id": "R001", "name": "Alice", "skills": ["Python", "SQL"], "availability": 2},
    {"resource_id": "R002", "name": "Bob", "skills": ["Java", "Cloud"], "availability": 1},
    {"resource_id": "R003", "name": "Charlie", "skills": ["Python", "Java"], "availability": 1},
]

projects_data = [
    {"project_id": "P001", "name": "Data Analysis", "required_skills": ["Python", "SQL"], "urgency": 5, "budget": 10000},
    {"project_id": "P002", "name": "Web App", "required_skills": ["Java", "Cloud"], "urgency": 4, "budget": 15000},
    {"project_id": "P003", "name": "ML Pipeline", "required_skills": ["Python"], "urgency": 3, "budget": 20000},
]


# Match resources to projects where their skills are required.
# Ensure no resource is assigned to more than 2 projects at a time.
print("_____________________________________________")
def match_res_proj(resources, projects):
    matched = dict() # project: resources
    for p in projects:
        keys_p = list(p.keys())
        name_p = p[keys_p[0]] + "_" + p[keys_p[1]]
        matched[name_p] = []
        req_skills = p[keys_p[2]]
        for r in resources:
            keys_r = list(r.keys())
            name_r = r[keys_r[0]] + "_" + r[keys_r[1]]
            skills = r[keys_r[2]]
            avail = r[keys_r[3]]
            assign = False
            count = 0
            a = 0
            for s in skills:
                if(s in list(req_skills)):
                    count += 1
                    if(count == len(req_skills)):
                        a += 1
                        if(a <= avail):
                            assign = True
                            matched[name_p].append(name_r)
                            count = 0
                            break
                    continue
                else:
                    continue
    return matched
assigned = match_res_proj(resources_data, projects_data)
for proj in list(assigned.keys()):
    print(f"{proj} --------", end = ' ')
    for res in assigned[proj]:
        print(res, end = '\t')
    print('\n')



# projects_data = [
#     {"project_id": "P005", "name": "ML Pipeline", "required_skills": ["Python"], "urgency": 5, "budget": 5000},
#     {"project_id": "P003", "name": "ML", "required_skills": ["Python"], "urgency": 5, "budget": 50000},
#     {"project_id": "P001", "name": "Data Analysis", "required_skills": ["Python", "SQL"], "urgency": 3, "budget": 1000},
#     {"project_id": "P002", "name": "Web App", "required_skills": ["Java", "Cloud"], "urgency": 4, "budget": 15000},
#     {"project_id": "P004", "name": "Web Development", "required_skills": ["Java", "Cloud"], "urgency": 3, "budget": 15000},
#     {"project_id": "P006", "name": "Web App", "required_skills": ["Java", "Cloud"], "urgency": 4, "budget": 1500}
# ]

# Prioritize projects based on urgency and budget.
print("_____________________________________________")
def prioritize(projects):
    name = list()
    urgent = list()
    budget = list()
    for p in projects:
        keys = list(p.keys())
        name.append(p[keys[0]] + "_" + p[keys[1]])
        urgent.append(p[keys[3]])
        budget.append(p[keys[4]])
    proj = dict(zip(name, list(zip(urgent, budget))))
    urg = []
    for i in urgent:
        if i not in urg:
            urg.append(i)
    urg.sort(reverse=True)
    urgent = urg
    bud = []
    for i in budget:
        if i not in bud:
            bud.append(i)
    bud.sort(reverse=True)
    budget = bud
    sort = []
    sorted = []
    for j in urgent:
        for b in budget:
            for i in proj:
                info = (i, proj[i])
                if(proj[i][0] == j) and (proj[i][1] == b):
                    sort.append(info)
        sorted.append(sort)
        sort = []
    prioritized = {j[0]:(j[1][0], j[1][1]) for i in sorted for j in i}
    return prioritized
p = prioritize(projects_data)
for proj in p:
    print(f"{proj}: {p[proj][0]} ${p[proj][1]}")

# Generate a final allocation report.
print("_____________________________________________")
def final_rep(resources, projects):
    report = dict()
    match = match_res_proj(resources, projects)
    priority = prioritize(projects)
    for proj in priority:
        report[proj] = (match[proj], priority[proj])
    return report
rep = final_rep(resources_data, projects_data)
for i in rep:
    print(f"{i}", end = '')
    for info in rep[i][1]:
        print(f"\t{info}", end = '\t')
    print()
    for res in rep[i][0]:
        print(res)
    print()