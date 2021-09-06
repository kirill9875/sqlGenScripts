import pandas as pd  # pip install pandas

df = pd.read_excel(r'pins.xlsx')
logins_crm = df[['LastDISTR_HISTORY_AR', 'CRM_ID']].replace('\n', '', regex=True) #парсит колонки по названиям

sqlBase = open("method.txt", "r") #шаблон
sql = sqlBase.read()

sqlBase.close()

file = open("resultMethod.txt", "w")

for i in range(len(logins_crm)):
    current_login = logins_crm.iloc[i][0]
    crm_id = logins_crm.iloc[i][1]

    result = sql.replace("#CRM_ID#", "'" + str(crm_id) + "'" ).replace("#LOGIN#", "'" + str(current_login) + "'")
    file.write(result + "\n")

file.close()
