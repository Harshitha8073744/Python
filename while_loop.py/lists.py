employees=[{"eid":1,"first_name":"Ellynn","gender":"Female"},
{"eid":2,"first_name":"Lorry","gender":"Non-binary"},
{"eid":3,"first_name":"Grace","gender":"Female"},
{"eid":4,"first_name":"Garek","gender":"Male"},
{"eid":5,"first_name":"Felike","gender":"Male"},
{"eid":6,"first_name":"Chilton","gender":"Male"},
{"eid":7,"first_name":"Eva","gender":"Female"},
{"eid":8,"first_name":"Marge","gender":"Genderfluid"},
{"eid":9,"first_name":"Salvador","gender":"Male"},
{"eid":10,"first_name":"Wilek","gender":"Male"},
{"eid":11,"first_name":"Fayth","gender":"Female"},
{"eid":12,"first_name":"Gage","gender":"Male"},
{"eid":13,"first_name":"Devonna","gender":"Female"},
{"eid":14,"first_name":"Devora","gender":"Female"},
{"eid":15,"first_name":"Lovell","gender":"Male"},
{"eid":16,"first_name":"Elga","gender":"Female"},
{"eid":17,"first_name":"Noah","gender":"Male"},
{"eid":18,"first_name":"Samuel","gender":"Male"},
{"eid":19,"first_name":"Brit","gender":"Male"},
{"eid":20,"first_name":"Myriam","gender":"Agender"},
{"eid":21,"first_name":"Dyan","gender":"Female"},
{"eid":22,"first_name":"Stoddard","gender":"Bigender"},
{"eid":23,"first_name":"Mandel","gender":"Male"},
{"eid":24,"first_name":"Mireille","gender":"Female"},
{"eid":25,"first_name":"Jen","gender":"Female"},
{"eid":26,"first_name":"Farr","gender":"Male"},
{"eid":27,"first_name":"Carri","gender":"Female"},
{"eid":28,"first_name":"Symon","gender":"Male"},
{"eid":29,"first_name":"Gavin","gender":"Male"},
{"eid":30,"first_name":"Rollie","gender":"Male"},
{"eid":31,"first_name":"Cleon","gender":"Male"},
{"eid":32,"first_name":"Dimitry","gender":"Male"},
{"eid":33,"first_name":"Janela","gender":"Female"},
{"eid":34,"first_name":"Page","gender":"Male"},
{"eid":35,"first_name":"Shaughn","gender":"Male"},
{"eid":36,"first_name":"Justina","gender":"Female"},
{"eid":37,"first_name":"Payton","gender":"Male"},
{"eid":38,"first_name":"Nevsa","gender":"Female"},
{"eid":39,"first_name":"Ewen","gender":"Male"},
{"eid":40,"first_name":"Emlyn","gender":"Male"},
{"eid":41,"first_name":"Tarrance","gender":"Male"},
{"eid":42,"first_name":"Beniamino","gender":"Male"},
{"eid":43,"first_name":"Olivier","gender":"Male"},
{"eid":44,"first_name":"Ellery","gender":"Male"},
{"eid":45,"first_name":"Lock","gender":"Male"},
{"eid":46,"first_name":"Huntington","gender":"Male"},
{"eid":47,"first_name":"Vassili","gender":"Male"},
{"eid":48,"first_name":"Clio","gender":"Female"},
{"eid":49,"first_name":"Brant","gender":"Male"},
{"eid":50,"first_name":"Gaylor","gender":"Male"},
{"eid":51,"first_name":"Karalynn","gender":"Female"},
{"eid":52,"first_name":"Indira","gender":"Female"},
{"eid":53,"first_name":"Rosalinda","gender":"Female"},
{"eid":54,"first_name":"Kally","gender":"Female"},
{"eid":55,"first_name":"Babbie","gender":"Female"},
{"eid":56,"first_name":"Cynthie","gender":"Female"},
{"eid":57,"first_name":"Jacques","gender":"Genderqueer"},
{"eid":58,"first_name":"Jody","gender":"Female"},
{"eid":59,"first_name":"La verne","gender":"Female"},
{"eid":60,"first_name":"Kaja","gender":"Female"},
{"eid":61,"first_name":"Carmelle","gender":"Female"},
{"eid":62,"first_name":"Phyllis","gender":"Female"},
{"eid":63,"first_name":"Oby","gender":"Male"},
{"eid":64,"first_name":"Waring","gender":"Male"},
{"eid":65,"first_name":"Auguste","gender":"Female"},
{"eid":66,"first_name":"Jehu","gender":"Male"},
{"eid":67,"first_name":"Russ","gender":"Male"},
{"eid":68,"first_name":"Reidar","gender":"Male"},
{"eid":69,"first_name":"Luce","gender":"Male"},
{"eid":70,"first_name":"Papagena","gender":"Female"},
{"eid":71,"first_name":"Hortense","gender":"Female"},
{"eid":72,"first_name":"Martino","gender":"Male"},
{"eid":73,"first_name":"Herman","gender":"Male"},
{"eid":74,"first_name":"Suzanne","gender":"Female"},
{"eid":75,"first_name":"Waite","gender":"Male"},
{"eid":76,"first_name":"Simeon","gender":"Male"},
{"eid":77,"first_name":"Reuben","gender":"Male"},
{"eid":78,"first_name":"Kirbee","gender":"Female"},
{"eid":79,"first_name":"Shanda","gender":"Female"},
{"eid":80,"first_name":"Ashla","gender":"Female"},
{"eid":81,"first_name":"Noel","gender":"Male"},
{"eid":82,"first_name":"Penni","gender":"Female"},
{"eid":83,"first_name":"Shantee","gender":"Female"},
{"eid":84,"first_name":"Job","gender":"Male"},
{"eid":85,"first_name":"Tana","gender":"Female"},
{"eid":86,"first_name":"Jess","gender":"Male"},
{"eid":87,"first_name":"Rodolphe","gender":"Male"},
{"eid":88,"first_name":"Kariotta","gender":"Female"},
{"eid":89,"first_name":"Aleen","gender":"Female"},
{"eid":90,"first_name":"Cher","gender":"Female"},
{"eid":91,"first_name":"Anderson","gender":"Male"},
{"eid":92,"first_name":"Gabie","gender":"Female"},
{"eid":93,"first_name":"Harlen","gender":"Male"},
{"eid":94,"first_name":"Erl","gender":"Male"},
{"eid":95,"first_name":"Dunc","gender":"Male"},
{"eid":96,"first_name":"Barbra","gender":"Female"},
{"eid":97,"first_name":"Spence","gender":"Male"},
{"eid":98,"first_name":"Joana","gender":"Female"},
{"eid":99,"first_name":"Wilona","gender":"Female"},
{"eid":100,"first_name":"Gayla","gender":"Female"}]

'''for emp in employees:
    print(emp['first_name'])

i=0
print('using while loop')
while i<=len(employees)-1:
    print(employees[i]['first_name'])
    i=i+1
print(len(employees))'''
'''for emp in employees:
    if emp['gender']=='Male':
        print(emp['first_name'])'''
'''counter=0
for emp in employees:
    if emp['gender']=='Male':
        counter+=1
print('no of male employees is:')
print(counter)'''
i=0
countf=0
while i<= len(employees)-1:
    if employees[i]['gender']=='Female':
        countf=countf+1
print(countf)