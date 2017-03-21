# ba68a030b6ef1fb25c47f1894e8b430867916a18 # github token

# import base64
# import requests

# person = {
# 	'name': 'japheth balane',
# 	'quote': 'play to win'
# }

# static = """
# 	<!doctype html>
# 	<html>
# 		<head>
# 			<title>Faculty: {}</title>
# 		</head>
# 		<body>
# 			<h1>{}</h1>
# 			<p>Lorem ipsum dolor sit amet.</p>
# 		</body>
# 	</html>
# """.format(person.get('name'), person.get('quote'))

# encoded = base64.b64encode(static)

# d = {
# 	'message': 'my first commit message',
# 	'committer': {
# 		'name': 'Japheth C. Balane',
# 		'email': 'japheth162gmail.com'
# 	},
# 	'content': encoded
# }

# print encoded
# print '................................'
# print d
# print '................................'

# r = requests.put('https://github.com/japhethbalane/sciences-test', data = d)

# print r

# ###

import requests

r = requests.get('https://api.github.com/events')

print r
