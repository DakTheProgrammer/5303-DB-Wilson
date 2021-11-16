import json
import mysql.connector

filename = 'Fall_2021.json'
file = open(filename)

config = open('Config.json')
data = json.load(config)

db = filename.split('_')
db = db[0] + ' ' + db[1][:-5]

cnx = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = db)
cursor = cnx.cursor()

data = json.load(file)

Course = 'INSERT INTO Course (`Crn`, `College`, `Subject`, `Course#`) VALUES (%s, %s, %s, %s)'
AboutCourse = 'INSERT INTO AboutCourse (`Crn`, `Section`, `Title`, `Instructor`, `Size`, `Current`, `Available`, `Days`, `Start`, `End`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
Location = 'INSERT INTO Location (`Crn`, `Building`, `Room`) VALUES (%s, %s, %s)'
temp = 0

for i in data:
    keys = i.keys()

    if 'Crn' in keys:
        C = [None, None, None, None]
        A = [None, None, None, None, None, None, None, None, None, None]
        L = [None, None, None]
        try:
            if i['Crn'] == '4033' or i['Crn'] == '4053':
                C[0] = int(temp)
                temp += 1
            else:
                C[0] = int(i['Crn'])
        except:
            C[0] = int(temp)
            temp += 1
        A[0] = C[0]
        L[0] = C[0]

        if 'Col' in keys:
            C[1] = i['Col']
        if 'Sect' in keys:
            A[1] = i['Sect']
        if 'Bldg' in keys:
            L[1] = i['Bldg']

        if 'Subj' in keys:
            C[2] = i['Subj']
        if 'Title' in keys:
            A[2] = i['Title']
        if 'Room' in keys:
            L[2] = i['Room']

        if 'Crse' in keys:
            C[3] = i['Crse']
        if 'PrimaryInstructor' in keys:
            A[3] = i['PrimaryInstructor']

        if 'Max' in keys:
            A[4] = i['Max']
        if 'Curr' in keys:
            A[5] = i['Curr']
        if 'Aval' in keys:
            A[6] = i['Aval']
        if 'Days' in keys:
            A[7] = i['Days']
        if 'Begin' in keys:
            A[8] = i['Begin']
        if 'End' in keys:
            A[9] = i['End']

        cursor.execute(Course, C)
        cnx.commit()

        cursor.execute(AboutCourse, A)
        cnx.commit()
        
        cursor.execute(Location, L)
        cnx.commit()
        print(C)
        print(A)
        print(L)