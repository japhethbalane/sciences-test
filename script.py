
######################################################################################

mainFormat = {
	"faculties": [], # based on personFormat
	"news": []       # based on newsFormat
}

personFormat = {
	"name": "",
	"college": "",
	"position": "",
	"photo": "",
	"introduction": "",
	"research": [], # based on researchFormat
	"training": []  # based on trainingFormat
}

researchFormat = {
	"title": "",
	"year-published": 0,
	"abstract": "",
	"authors": [], # string array
	"link": ""
}

trainingFormat = {
	"title": "",
	"date": "",
	"description": ""
}

newsFormat = {
	"title": "",
	"tags": [], # string array
	"date": "",
	"body": "",
	"author": "",
	"photo": ""
}

######################################################################################

print main

######################################################################################