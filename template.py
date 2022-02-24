from selenium import webdriver
from selenium.webdriver.common.by import By 
from datetime import datetime
import datos

### PATH DEL DRIVER DE GOOGLE
chromedriver = datos.chromedriverpath

### URL DE SIGEDU
login = 'https://sigedu.utdt.edu/utdt/principal/login.jsp'

### DATOS DE LA INSCRIPCION
esperar = datos.esperar
user = datos.usuario
contra = datos.clave

hora_de_inscripcion = datetime(datos.anio, datos.mes, datos.dia, datos.hora, datos.minutos)
loops = datos.loops

### LOG IN EN SIGEDU
try:
	driver = webdriver.Chrome()
except:
	driver = webdriver.Chrome(chromedriver)
driver.get(login)
driver.find_element(By.XPATH,'\
	/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[1]/td[3]/input[2]'\
	).send_keys(user)
driver.find_element(By.XPATH,'\
	/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[2]/td[3]/input'\
	).send_keys(contra)
driver.find_element(By.XPATH,'\
	/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[3]/td/input[1]'\
	).click()
driver.find_element(By.XPATH,'/html/body/table[2]/tbody/tr/td[1]/div[2]/table\
	/tbody/tr/td/table[1]/tbody/tr/td/a').click()

### INSCRIBIRSE SECUENCIALMENTE EN MATERIAS
if esperar == True:
	while hora_de_inscripcion > datetime.now():
		pass
for _ in range(loops):
	driver.get(url)