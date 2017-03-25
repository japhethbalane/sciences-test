
###################################################################################### global variable definitions

mainFormat = {}
personFormat = {}
researchFormat = {}
trainingFormat = {}
newsFormat = {}

###################################################################################### initializations

def initMain():
	return {
		"faculties": [], # based on personFormat
		"news": []       # based on newsFormat
	}
def initPerson():
	return {
		"name": "",
		"college": "",
		"position": "",
		"photo": "",
		"introduction": "",
		"research": [], # based on researchFormat
		"training": []  # based on trainingFormat
	}
def initResearch():
	return {
		"title": "",
		"year-published": 0,
		"abstract": "",
		"authors": [], # string array
		"link": ""
	}
def initTraining():
	return {
		"title": "",
		"date": "",
		"description": ""
	}
def initNews():
	return {
		"title": "",
		"tags": [], # string array
		"date": "",
		"body": "",
		"author": "",
		"photo": ""
	}

mainFormat = initMain()
personFormat = initPerson()
researchFormat = initResearch()
trainingFormat= initTraining()
newsFormat = initNews()

######################################################################################

######################################################################################

######################################################################################

######################################################################################

print mainFormat
print personFormat
print researchFormat
print trainingForma
print newsFormat

######################################################################################