# Enter your code here. Read input from STDIN. Print output to STDOUT

accounts = [
  {"accountId": "org_1", "parent": None},
  {"accountId": "wksp_1", "parent": "org_1"},
  {"accountId": "sbx_1", "parent": "wksp_1"},
  {"accountId": "sbx_2", "parent": "org_1"},
  {"accountId": "wksp_2", "parent": None},
]

user_role_assignments = [
  {"userId": "usr_1", "accountId": "org_1", "role": "admin"},
  {"userId": "usr_1", "accountId": "wksp_1", "role": "developer"},
  {"userId": "usr_1", "accountId": "wksp_1", "role": "analyst"},
  {"userId": "usr_1", "accountId": "sbx_1", "role": "analyst"},
  {"userId": "usr_2", "accountId": "org_1", "role": "developer"},
  {"userId": "usr_3", "accountId": "wksp_1", "role": "analyst"},
  {"userId": "usr_3", "accountId": "wksp_1", "role": "admin"},
  {"userId": "usr_4", "accountId": "wksp_2", "role": "admin"},
]

def getRolesForUserInAccount(userId, accountId):
    # your code goes here
    found_roles=[]
    
    current_account_id = accountId
    while current_account_id is not None:
        for  a in user_role_assignments:
            if a["userId"]== userId and a["accountId"]== current_account_id:
                found_roles.append(a["role"])
            
        parent_node=None
        for i in accounts:
            if i["accountId"] == current_account_id:
                parent_node= i["parent"]
                break     
        current_account_id = parent_node
        return list(found_roles)
    
    pass

# print(getRolesForUserInAccount("usr_1", "wksp_1"))
# # ["admin", "developer", "analyst"]

# print(getRolesForUserInAccount("usr_1", "sbx_1"))
# # ["admin", "developer", "analyst"]

# print(getRolesForUserInAccount("usr_1", "org_1"))
# # ["admin"]

# print(getRolesForUserInAccount("usr_2", "org_1"))
# # ["developer"]

# print(getRolesForUserInAccount("usr_2", "wksp_1"))
# # ["developer"]

# print(getRolesForUserInAccount("usr_2", "sbx_1"))
# # ["developer"]

# print(getRolesForUserInAccount("usr_3", "org_1"))
# # []

# print(getRolesForUserInAccount("usr_3", "wksp_1"))
# # ["analyst", "admin"]

print(getRolesForUserInAccount("usr_3", "sbx_1"))
# ["analyst", "admin"]

# print(getRolesForUserInAccount("usr_4", "wksp_2"))
# # ["admin"]