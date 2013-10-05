#SERVER_NAME = '127.0.0.1:8080'
import os

# We want to seamlessy run our API both locally and on Heroku so:
if os.environ.get('PORT'):
	
    SERVER_NAME = 'lprpgapi.herokuapp.com'
else:
	SERVER_NAME = '192.168.2.102:8080'

HATEOAS = False
DEBUG = False
PROJECTION = True
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
PUBLIC_METHODS = ['GET', 'PATCH', 'POST', 'DELETE']
X_DOMAINS = "*" #allow access from admin client running on different server
X_HEADERS = ['Content-Type', 'If-Match', 'Origin', 'User-Agent', 'Referer', 'Accept'] #allow access from admin client running on different server
questions = {
		'item_title': 'question',
		#'hateoas': 'False',
		'schema': {
			'text': {
				'type': 'string',
				'minlength': 1,
				'maxlength': 50,
			},
			'results': {
				'url':'results',
				'type': 'list',
				'schema': { 
					'type': 'dict',
					'schema': {			
						'token': {
							'type': 'objectid',
							'data_relation': {
								'collection': 'tokens',
								'field': '_id',
								'embeddable': True
								}
						},
						'yes': {
							'type': 'integer'
						},
						'no': {
							'type': 'integer'
						},
					},
				},
			},
		},
}


tokens = {
	'item_title': 'token',
	#'hateoas': 'False',
	'schema': {
		'text': {
			'type':'string',
			'minlength': 1,
			'maxlength': 50,
		},
		'shortcode':{
			'type':'string',
			'minlength': 1,
			'maxlength': 3,
		},
		'color':{
			'type':'string',
			'minlength':6,
			'maxlength':6,
		},		
	},
}

DOMAIN = {
	'questions' : questions,
	'tokens' : tokens,
}

MONGO_HOST = 'widmore.mongohq.com'
MONGO_PORT = 10000
MONGO_USERNAME = 'jonnyboy'
MONGO_PASSWORD = 'ilovebeerandchips'
MONGO_DBNAME = 'LPRPG'