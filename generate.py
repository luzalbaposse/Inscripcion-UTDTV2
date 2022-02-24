import datos

urls = datos.urls

# CREAR UN SCRIPT POR MATERIA EN DATOS.URLS
def make_file(url, filename):
	with open('template.py','r') as template, open(filename, 'a') as file:
		for _ in range(15):
			file.write(template.readline())
		file.write("url = '" + url + "'")
		for _ in range(16, 44):
			file.write(template.readline())

filenum = 1
for url in urls:
	make_file(url, "materia" + str(filenum) + ".py")
	filenum += 1

# CREAR UN BASH FILE QUE CORRE LOS SCRIPTS DE LAS MATERIAS EN SIMULTANEO
def create_run(numfiles, filename):
	with open(filename,'a') as run:
		for i in range(1, numfiles):
			if i == (numfiles - 1):
				run.write("python3 materia" + str(i) + ".py")
			else:
				run.write("python3 materia" + str(i) + ".py" + " &\n")

create_run(filenum, 'run.sh')
