x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def one(x, students, sports_directory, z):
    x[1][0]=15
    students[0]["last_name"]="Bryant"
    sports_directory["soccer"][0]="Andres"
    z[0]["y"]=30
    print(x)
    print(students)
    print(sports_directory)
    print(z)

# one(x, students, sports_directory, z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in students:
        a=[]
        for key in i:
            a.append(f"{key} - {i[key]}")
        print(a[0] + ',', a[1])
        
# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, students):
    for i in students:
        for key, value in i.items():
            if key==key_name:
                print(value)

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in dojo:
        print(f"\n{len(i)} {i}")
        for x in dojo[i]:
            print(x)

printInfo(dojo)