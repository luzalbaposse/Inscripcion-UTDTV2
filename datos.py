""" 
	los datos de acceso deben ser strings 

	Ejemplo:
		usuario = '45123789'
		clave = '010101789'
"""

usuario = ''
clave = ''

""" 
	los datos horarios deben ser cargados como numeros y segun formato de
	24 horas 
	Ejemplo:
		anio = 2020 
		mes = 2 
		dia = 19
		hora = 15
		minutos = 30
"""

anio = 2022
mes = 2
dia = 20
hora = 13
minutos = 0
segundos = 0

"""
	cambiar el PATH (absolute path) del chromedriver, para no tener problemas
	con los distintos interpretadores.
	
	Ejemplo:
		chromedriverpath = 'users/usuario/inscripcion-utdt/chromedriver'
"""

chromedriverpath = './chromedriver'

"""
	insertar los urls descriptos en README.md dentro de la lista urls, cada uno entre comillas y separados por comas.
	
	Ejemplo:
		urls = ('https://sigedu.utdt.edu/utdt/alumnos/inscripcion_cursos.jsp?v_id_materia=17&v_n_curso=1788&v_anio=2021&grabar=1&v_qry_pagina=1',
			'https://sigedu.utdt.edu/utdt/alumnos/inscripcion_cursos.jsp?v_id_materia=11&v_n_curso=2162&v_anio=2021&grabar=1&v_qry_pagina=1',
			'https://sigedu.utdt.edu/utdt/alumnos/inscripcion_cursos.jsp?v_id_materia=7&v_n_curso=2140&v_anio=2021&grabar=1&v_qry_pagina=1',
			'https://sigedu.utdt.edu/utdt/alumnos/inscripcion_cursos.jsp?v_id_materia=15&v_n_curso=2091&v_anio=2021&grabar=1&v_qry_pagina=1')
"""

urls = ('', '', '', '', '')

"""
	Si la variable esperar es True, el programa espera hasta la hora indicada para empezar la inscripcion. Si es False, empieza ni bien es ejecutado el programa.
	La variable loops indica la cantidad de veces que el programa intenta inscribirse en cada materia.
"""

esperar = False
loops = 10