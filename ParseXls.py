import pandas as pd  # pip install pandas

df = pd.read_excel(r'tst.xlsx')
# print(df.columns)
logins_eksId = df[['логин пользователя', 'EKS_ID']].replace('\n', '', regex=True) #парсит колонки по названиям

sqlBase = open("SqlScript.txt", "r") #шаблон
sql = sqlBase.read()

sqlBase.close()

file = open("result.txt", "w")

lst_login = logins_eksId.iloc[0][0]
eks_in_many = []

for i in range(len(logins_eksId)):
    current_login = logins_eksId.iloc[i][0]
    if current_login == lst_login:
        eks_in_many.append("\n'" + str(logins_eksId.iloc[i][1]) + "'")
    else:
        eksID = ','.join(eks_in_many)
        result = sql.replace("#SetLogin#", "UPPER('" + str(lst_login) + "')").replace("#SetEksId#", "in (" + eksID + ")")
        file.write(result + "\n")
        eks_in_many = ["\n'" + str(logins_eksId.iloc[i][1]) + "'"]
    lst_login = current_login
file.write(sql.replace("#SetLogin#", "UPPER('" + str(lst_login) + "')").replace("#SetEksId#", "in(" + ','.join(eks_in_many) + ")"))

file.close()
