from fastapi import FastAPI
import mysql.connector
import json
import uvicorn
import os

if __name__ == '__main__':
    uvicorn.run("API:app", host="167.99.6.44", port=8004, reload=True)

jfile = open(os.path.dirname(os.path.abspath(__file__)) + '/Config.json')
data = json.load(jfile)

app = FastAPI()

spring2022 = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = 'Spring 2022')
spring2022cursor = spring2022.cursor()

spring2021 = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = 'Spring 2021')
spring2021cursor = spring2021.cursor()

fall2021 = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = 'Fall 2021')
fall2021cursor = fall2021.cursor()

summer12021 = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = 'Summer1 2021')
summer12021cursor = summer12021.cursor()

summer22021 = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = 'Summer2 2021')
summer22021cursor = summer22021.cursor()

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

def nosendsem(sem, sql):
    if sem == 'spring 2022':
        spring2022cursor.execute(sql)
        columns = spring2022cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2022cursor.fetchall()]
        return result
    elif sem == 'spring 2021':
        spring2021cursor.execute(sql)
        columns = spring2021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2021cursor.fetchall()]
        return result
    elif sem == 'fall 2021':
        fall2021cursor.execute(sql)
        columns = fall2021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in fall2021cursor.fetchall()]
        return result
    elif sem == 'summer1 2021':
        summer12021cursor.execute(sql)
        columns = summer12021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer12021cursor.fetchall()]
        return result
    elif sem == 'summer2 2021':
        summer22021cursor.execute(sql)
        columns = summer22021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer22021cursor.fetchall()]
        return result
    else:
        return{'result': 'ERROR NO SEMESTER BY THAT NAME TRY (spring 2022, spring 2021, fall 2021, summer1 2021, summer2 2021)'}

def sendsem(sem, sql, send):
    if sem == 'spring 2022':
        spring2022cursor.execute(sql, send)
        columns = spring2022cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2022cursor.fetchall()]
        return result
    elif sem == 'spring 2021':
        spring2021cursor.execute(sql, send)
        columns = spring2021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2021cursor.fetchall()]
        return result
    elif sem == 'fall 2021':
        fall2021cursor.execute(sql, send)
        columns = fall2021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in fall2021cursor.fetchall()]
        return result
    elif sem == 'summer1 2021':
        summer12021cursor.execute(sql, send)
        columns = summer12021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer12021cursor.fetchall()]
        return result
    elif sem == 'summer2 2021':
        summer22021cursor.execute(sql, send)
        columns = summer22021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer22021cursor.fetchall()]
        return result
    else:
        return{'result': 'ERROR NO SEMESTER BY THAT NAME TRY (spring 2022, spring 2021, fall 2021, summer1 2021, summer2 2021)'}

def formsfunc(sql):
        spring2022cursor.execute(sql)
        columns = spring2022cursor.description
        resultSP2022 = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2022cursor.fetchall()]
        
        spring2021cursor.execute(sql)
        columns = spring2021cursor.description
        resultSP2021 = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2021cursor.fetchall()]

        fall2021cursor.execute(sql)
        columns = fall2021cursor.description
        resultF2021 = [{columns[index][0]:column for index, column in enumerate(value)} for value in fall2021cursor.fetchall()]

        summer12021cursor.execute(sql)
        columns = summer12021cursor.description
        resultS12021 = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer12021cursor.fetchall()]

        summer22021cursor.execute(sql)
        columns = summer22021cursor.description
        resultS22021 = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer22021cursor.fetchall()]

        return{
            'Spring 2022': resultSP2022,
            'Fall 2021': resultF2021,
            'Summer 2 2021': resultS22021,
            'Summer 1 2021': resultS12021,
            'Spring 2021': resultSP2021
        }

def formsfuncsend(sql, send):
        spring2022cursor.execute(sql, send)
        columns = spring2022cursor.description
        resultSP2022 = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2022cursor.fetchall()]
        
        spring2021cursor.execute(sql, send)
        columns = spring2021cursor.description
        resultSP2021 = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2021cursor.fetchall()]

        fall2021cursor.execute(sql, send)
        columns = fall2021cursor.description
        resultF2021 = [{columns[index][0]:column for index, column in enumerate(value)} for value in fall2021cursor.fetchall()]

        summer12021cursor.execute(sql, send)
        columns = summer12021cursor.description
        resultS12021 = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer12021cursor.fetchall()]

        summer22021cursor.execute(sql, send)
        columns = summer22021cursor.description
        resultS22021 = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer22021cursor.fetchall()]

        return{
            'Spring 2022': resultSP2022,
            'Fall 2021': resultF2021,
            'Summer 2 2021': resultS22021,
            'Summer 1 2021': resultS12021,
            'Spring 2021': resultSP2021
        }

def formsem(sem, sql):
    if sem == 'spring 2022':
        spring2022cursor.execute(sql)
        columns = spring2022cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2022cursor.fetchall()]
        return result
    elif sem == 'spring 2021':
        spring2021cursor.execute(sql)
        columns = spring2021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2021cursor.fetchall()]
        return result
    elif sem == 'fall 2021':
        fall2021cursor.execute(sql)
        columns = fall2021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in fall2021cursor.fetchall()]
        return result
    elif sem == 'summer1 2021':
        summer12021cursor.execute(sql)
        columns = summer12021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer12021cursor.fetchall()]
        return result
    elif sem == 'summer2 2021':
        summer22021cursor.execute(sql)
        columns = summer22021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer22021cursor.fetchall()]
        return result
    else:
        return{'result': 'ERROR NO SEMESTER BY THAT NAME TRY (spring 2022, spring 2021, fall 2021, summer1 2021, summer2 2021)'}

def formyear(year, sql):
    if year == '2022':
        spring2022cursor.execute(sql)
        columns = spring2022cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2022cursor.fetchall()]
        return{'Spring 2022': result}
    elif year == '2021':
        spring2021cursor.execute(sql)
        columns = spring2021cursor.description
        SPresult = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2021cursor.fetchall()]


        fall2021cursor.execute(sql)
        columns = fall2021cursor.description
        Fresult = [{columns[index][0]:column for index, column in enumerate(value)} for value in fall2021cursor.fetchall()]

        summer12021cursor.execute(sql)
        columns = summer12021cursor.description
        S1result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer12021cursor.fetchall()]


        summer22021cursor.execute(sql)
        columns = summer22021cursor.description
        S2result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer22021cursor.fetchall()]
        
        return{
            'Fall 2021': Fresult,
            'Summer 2 2021': S2result,
            'Summer 1 2021': S1result,
            'Spring 2021': SPresult
        }
    else:
        return{'result': 'ERROR NO YEAR BY THAT NAME TRY (2022, 2021)'}

def formyearsend(year, sql, send):
    if year == '2022':
        spring2022cursor.execute(sql, send)
        columns = spring2022cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2022cursor.fetchall()]
        return{'Spring 2022': result}
    elif year == '2021':
        spring2021cursor.execute(sql, send)
        columns = spring2021cursor.description
        SPresult = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2021cursor.fetchall()]


        fall2021cursor.execute(sql, send)
        columns = fall2021cursor.description
        Fresult = [{columns[index][0]:column for index, column in enumerate(value)} for value in fall2021cursor.fetchall()]

        summer12021cursor.execute(sql, send)
        columns = summer12021cursor.description
        S1result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer12021cursor.fetchall()]


        summer22021cursor.execute(sql, send)
        columns = summer22021cursor.description
        S2result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer22021cursor.fetchall()]
        
        return{
            'Fall 2021': Fresult,
            'Summer 2 2021': S2result,
            'Summer 1 2021': S1result,
            'Spring 2021': SPresult
        }
    else:
        return{'result': 'ERROR NO YEAR BY THAT NAME TRY (2022, 2021)'}

def formsemsend(sem, sql, send):
    if sem == 'spring 2022':
        spring2022cursor.execute(sql, send)
        columns = spring2022cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2022cursor.fetchall()]
        return result
    elif sem == 'spring 2021':
        spring2021cursor.execute(sql, send)
        columns = spring2021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in spring2021cursor.fetchall()]
        return result
    elif sem == 'fall 2021':
        fall2021cursor.execute(sql, send)
        columns = fall2021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in fall2021cursor.fetchall()]
        return result
    elif sem == 'summer1 2021':
        summer12021cursor.execute(sql, send)
        columns = summer12021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer12021cursor.fetchall()]
        return result
    elif sem == 'summer2 2021':
        summer22021cursor.execute(sql, send)
        columns = summer22021cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in summer22021cursor.fetchall()]
        return result
    else:
        return{'result': 'ERROR NO SEMESTER BY THAT NAME TRY (spring 2022, spring 2021, fall 2021, summer1 2021, summer2 2021)'}

def postput(sql1, sql2, send1, send2, body):
    if body['Semester'] == 'spring 2022':
        spring2022cursor.execute(sql1, send1)
        spring2022.commit()
        spring2022cursor.execute(sql2, send2)
        spring2022.commit()
    elif body['Semester'] == 'spring 2021':
        spring2021cursor.execute(sql1, send1)
        spring2021.commit()
        spring2021cursor.execute(sql2, send2)
        spring2021.commit()
    elif body['Semester'] == 'fall 2021':
        fall2021cursor.execute(sql1, send1)
        fall2021.commit()
        fall2021cursor.execute(sql2, send2)
        fall2021.commit()
    elif body['Semester'] == 'summer1 2021':
        summer12021cursor.execute(sql1, send1)
        summer12021.commit()
        summer12021cursor.execute(sql2, send2)
        summer12021.commit()
    elif body['Semester'] == 'summer2 2021':
        summer22021cursor.execute(sql1, send1)
        summer22021.commit()
        summer22021cursor.execute(sql2, send2)
        summer22021.commit()
    else:
        return{'result': 'ERROR NO SEMESTER BY THAT NAME TRY (spring 2022, spring 2021, fall 2021, summer1 2021, summer2 2021)'}

    return{
        'Result': 'Success!',
        'body': body
    }

def postput3(sql1, sql2, sql3, send1, send2, send3, body):
    if body['Semester'] == 'spring 2022':
        spring2022cursor.execute(sql1, send1)
        spring2022.commit()
        spring2022cursor.execute(sql2, send2)
        spring2022.commit()
        spring2022cursor.execute(sql3, send3)
        spring2022.commit()
    elif body['Semester'] == 'spring 2021':
        spring2021cursor.execute(sql1, send1)
        spring2021.commit()
        spring2021cursor.execute(sql2, send2)
        spring2021.commit()
        spring2021cursor.execute(sql3, send3)
        spring2021.commit()
    elif body['Semester'] == 'fall 2021':
        fall2021cursor.execute(sql1, send1)
        fall2021.commit()
        fall2021cursor.execute(sql2, send2)
        fall2021.commit()
        fall2021cursor.execute(sql3, send3)
        fall2021.commit()
    elif body['Semester'] == 'summer1 2021':
        summer12021cursor.execute(sql1, send1)
        summer12021.commit()
        summer12021cursor.execute(sql2, send2)
        summer12021.commit()
        summer12021cursor.execute(sql3, send3)
        summer12021.commit()
    elif body['Semester'] == 'summer2 2021':
        summer22021cursor.execute(sql1, send1)
        summer22021.commit()
        summer22021cursor.execute(sql2, send2)
        summer22021.commit()
        summer22021cursor.execute(sql3, send3)
        summer22021.commit()
    else:
        return{'result': 'ERROR NO SEMESTER BY THAT NAME TRY (spring 2022, spring 2021, fall 2021, summer1 2021, summer2 2021)'}

    return{
        'Result': 'Success!',
        'body': body
    }

def postputform(sql, send, body):
    if body['Semester'] == 'spring 2022':
        spring2022cursor.execute(sql, send)
        spring2022.commit()
    elif body['Semester'] == 'spring 2021':
        spring2021cursor.execute(sql, send)
        spring2021.commit()
    elif body['Semester'] == 'fall 2021':
        fall2021cursor.execute(sql, send)
        fall2021.commit()
    elif body['Semester'] == 'summer1 2021':
        summer12021cursor.execute(sql, send)
        summer12021.commit()
    elif body['Semester'] == 'summer2 2021':
        summer22021cursor.execute(sql, send)
        summer22021.commit()
    else:
        return{'result': 'ERROR NO SEMESTER BY THAT NAME TRY (spring 2022, spring 2021, fall 2021, summer1 2021, summer2 2021)'}

    return{
        'Result': 'Success!',
        'body': body
    }

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.get('/')
async def root():
    ...

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.get('/courseid/{id}/{sem}')
async def courseid(id: int, sem: str):
    sql = "SELECT * FROM Course AS x JOIN AboutCourse AS y ON (x.Crn = y.Crn) JOIN Location as z ON (x.Crn = z.Crn) WHERE x.Crn = %s"
    send = [id]

    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}
    

@app.get('/coursesubject/{sub}/{sem}')
async def coursesubject(sub: str, sem: str):
    sql = "SELECT * FROM Course AS x JOIN AboutCourse AS y ON (x.Crn = y.Crn) JOIN Location as z ON (x.Crn = z.Crn) WHERE x.Subject = %s"
    send = [sub]

    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/coursenum/{num}/{sem}')
async def coursenum(num: str, sem: str):
    sql = "SELECT * FROM Course AS x JOIN AboutCourse AS y ON (x.Crn = y.Crn) JOIN Location as z ON (x.Crn = z.Crn) WHERE `Course#` = %s"
    send = [num]

    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/courseprofname/{name}/{sem}')
async def courseprofname(name: str, sem: str):
    sql = "SELECT * FROM Course AS x JOIN AboutCourse AS y ON (x.Crn = y.Crn) JOIN Location as z ON (x.Crn = z.Crn) WHERE Instructor = %s"
    send = [name]
    
    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/coursebuilding/{bldg}/{sem}')
async def coursebuilding(bldg: str, sem: str):
    sql = "SELECT * FROM Course AS x JOIN AboutCourse AS y ON (x.Crn = y.Crn) JOIN Location as z ON (x.Crn = z.Crn) WHERE Building = %s"
    send = [bldg]
    
    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/times/{start}/{end}/{sem}')
async def times(start: str, end: str, sem: str):
    sql = "SELECT * FROM Course AS x JOIN AboutCourse AS y ON (x.Crn = y.Crn) JOIN Location as z ON (x.Crn = z.Crn) WHERE Start <= %s AND End >= %s"
    send = [start, end]
    
    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/closed/{sem}')
async def closed(sem: str):
    sql = "SELECT * FROM Course AS x JOIN AboutCourse AS y ON (x.Crn = y.Crn) JOIN Location as z ON (x.Crn = z.Crn) WHERE Available = '0'"
    send = []
    
    result = nosendsem(sem, sql)
    return{'sql': sql, 'result': result}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.get('/forms')
async def forms():
    sql = "SELECT * FROM AdvisingForm"
    result = formsfunc(sql)
    return{'sql': sql, 'result': result}

@app.get('/formsstudent/{mnum}')
async def formsstudent(mnum: str):
    sql = "SELECT * FROM AdvisingForm WHERE `M#` = %s"
    send = [mnum]
    result = formsfuncsend(sql, send)
    return{'sql': sql, 'result': result}

@app.get('/formssemster/{sem}')
async def formssemster(sem: str):
    sql = "SELECT * FROM AdvisingForm"
    result = formsem(sem, sql)
    return{'sql': sql, 'result': result}

@app.get('/formsyear/{year}')
async def formsyear(year: str):
    sql = "SELECT * FROM AdvisingForm"
    result = formyear(year, sql)
    return{'sql': sql, 'result': result}

@app.get('/formsstudentyear/{mnum}/{year}')
async def formsstudentyear(mnum: str, year: str):
    sql = "SELECT * FROM AdvisingForm WHERE `M#` = %s"
    send = [mnum]
    result = formyearsend(year, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/formsstudentsemester/{mnum}/{sem}')
async def formsstudentsemester(mnum: str, sem: str):
    sql = "SELECT * FROM AdvisingForm WHERE `M#` = %s"
    send = [mnum]
    
    result = formsemsend(sem, sql, send)
    return{'sql': sql, 'result': result}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.get('/students/{sem}')
async def students(sem: str):
    sql = "SELECT * FROM Student as x JOIN AboutStudent AS y ON (x.`M#` = y.`M#`)"
    
    result = nosendsem(sem, sql)
    return{'sql': sql, 'result': result}

@app.get('/studentsname/{sem}/{name}')
async def studentsname(sem: str, name: str):
    send = name.split(' ')
    sql = "SELECT * FROM Student as x JOIN AboutStudent AS y ON (x.`M#` = y.`M#`) WHERE First = %s and Last = %s"
    
    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/studentsnum/{sem}/{num}')
async def studentsnum(sem: str, num: str):
    sql = "SELECT * FROM Student as x JOIN AboutStudent AS y ON (x.`M#` = y.`M#`) WHERE x.`M#` = %s"
    send = [num]
    
    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/studentsgpahigher/{sem}/{gpa}')
async def studentgpahigher(sem: str, gpa: float):
    sql = "SELECT * FROM Student as x JOIN AboutStudent AS y ON (x.`M#` = y.`M#`) WHERE GPA > %s"
    send = [gpa]
    
    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/studentsgpalower/{sem}/{gpa}')
async def studentgpalower(sem: str, gpa: float):
    sql = "SELECT * FROM Student as x JOIN AboutStudent AS y ON (x.`M#` = y.`M#`) WHERE GPA < %s"
    send = [gpa]
    
    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

@app.get('/studentsgpa/{sem}/{gpa}')
async def studentgpa(sem: str, gpa: float):
    sql = "SELECT * FROM Student as x JOIN AboutStudent AS y ON (x.`M#` = y.`M#`) WHERE GPA = %s"
    send = [gpa]
    
    result = sendsem(sem, sql, send)
    return{'sql': sql, 'result': result}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.post('/addcourse')
async def addcourse(body: dict):
    sql1 = "INSERT INTO Course (Crn, College, Subject, `Course#`) VALUES (%s, %s, %s, %s)"
    sql2 = "INSERT INTO AboutCourse (Crn, Section, Title, Instructor, Size, Current, Available, Days, Start, End) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql3 = "INSERT INTO Location (Crn, Building, Room) VALUES (%s, %s, %s)"
    send1 = [body['Crn'], body['College'], body['Subject'], body['Course#']]
    send2 = [body['Crn'], body['Section'], body['Title'], body['Instructor'], body['Size'], body['Current'], body['Available'], body['Days'], body['Start'], body['End']]
    send3 = [body['Crn'], body['Building'], body['Room']]

    result = postput3(sql1, sql2, sql3, send1, send2, send3, body)
    return{'sql1': sql1, 'sql2': sql2, 'sql3':sql3, 'result': result}
    

@app.post('/addstudent')
async def addstudent(body: dict):
    sql1 = "INSERT INTO Student (`M#`, First, Last) VALUES (%s, %s, %s)"
    sql2 = "INSERT INTO AboutStudent (`M#`, Classification, Email, GPA, Github) VALUES (%s, %s, %s, %s, %s)"
    send1 = [body['M#'], body['First'], body['Last']]
    send2 = [body['M#'], body['Classification'], body['Email'], body['GPA'], body['Github']]

    result = postput(sql1, sql2, send1, send2, body)
    return{'sql1': sql1, 'sql2': sql2, 'result': result}


@app.post('/addform')
async def addform(body: dict):
    sql = "INSERT INTO AdvisingForm (`M#`, First, Last, Courses, Date) VALUES (%s, %s, %s, %s, %s)"
    send = [body['M#'], body['First'], body['Last'], body['Courses'], body['Date']]

    result = postputform(sql, send, body)
    return{'sql': sql, 'result': result}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.put('/editcourse')
async def editcourse(body: dict):
    sql1 = "UPDATE Course SET College = %s, Subject = %s, `Course#` = %s WHERE Crn = %s"
    sql2 = "UPDATE AboutCourse SET Section = %s, Title = %s, Instructor = %s, Size = %s, Current = %s, Available = %s, Days = %s, Start = %s, End = %s WHERE Crn = %s"
    sql3 = "UPDATE Location SET Building = %s, Room = %s WHERE Crn = %s"
    send1 = [body['College'], body['Subject'], body['Course#'], body['Crn']]
    send2 = [body['Section'], body['Title'], body['Instructor'], body['Size'], body['Current'], body['Available'], body['Days'], body['Start'], body['End'], body['Crn']]
    send3 = [body['Building'], body['Room'], body['Crn']]

    result = postput3(sql1, sql2, sql3, send1, send2, send3, body)
    return{'sql1': sql1, 'sql2': sql2, 'sql3':sql3, 'result': result}

@app.put('/editstudent')
async def editstudent(body: dict):
    sql1 = "UPDATE Student SET First = %s, Last = %s WHERE `M#` = %s"#M# has to be string
    sql2 = "UPDATE AboutStudent SET Classification = %s, Email = %s, GPA = %s, Github = %s WHERE `M#` = %s"#M# has to be string
    send1 = [body['First'], body['Last'], body['M#']]
    send2 = [body['Classification'], body['Email'], body['GPA'], body['Github'], body['M#']]

    result = postput(sql1, sql2, send1, send2, body)
    return{'sql1': sql1, 'sql2': sql2, 'result': result}

@app.put('/editform')
async def editform(body: dict):
    sql = "UPDATE AdvisingForm SET First = %s, Last = %s, Courses = %s, Date = %s WHERE `M#` = %s"#M# has to be string
    send = [body['First'], body['Last'], body['Courses'], body['Date'], body['M#']]

    result = postputform(sql, send, body)
    return{'sql': sql, 'result': result}