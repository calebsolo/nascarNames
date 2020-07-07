import random

random.seed()


raceNames= dict()
raceNames={"Sam B":random.random(),"Cass":random.random(),"Heath":random.random(),"John":random.random(),"Caleb":random.random(),"Bradley":random.random(),"Connon":random.random(),"Dodds":random.random(),"Reagan":random.random(),"Sam R":random.random()}
print(raceNames)

sort_names = sorted(raceNames.items(), key=lambda x: x[1], reverse=False)
file_object = open('/var/www/html/index.html', 'w')
num = 0
for i in sort_names:
    print(num, i[0])
    txtOut = str(num) + ' ' + i[0] + "<br>\n"
    file_object.write(txtOut)
    num=num+1
file_object.close()
