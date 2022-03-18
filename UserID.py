import base64


#example token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIxMDExOSIsImRlcGFydG1lbnQiOiIyMCIsImV4cCI6IjIwMjEtMDktMDggMjA6NTc6MTMifQ==.ODZjMGFmMTBjYWMxMTJjN2Q5YWQyNzE3NzY2NmYxYmQyNWU5NmE0NDU1NWNkMzhhODkyOWI3OGJlNGI3YzRmMGU1ZWRmNGFlNzU5OGJiYTMwYjlhZjdiYTYwODBiODdjYjEyZTIxZjE1YmI3ZmM0NjUzZjdlMWFkYTQ3YWNhYjk=

def getUserID(token):
    counter=0
    numOfDots=0
    firstIndex=0
    secondIndex=0
    userID=''
    for sign in token:
        if sign!='.':
            counter+=1
        else:
            numOfDots += 1
            if numOfDots==1:
                firstIndex = counter+1
            elif numOfDots==2:
                secondIndex = counter+1
                break
    userID = token[firstIndex:secondIndex]
    return base64.b64decode(userID)
    #return userID


IDDictionary = {}