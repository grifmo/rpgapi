import os
from eve import Eve
app = Eve()
app.HATEOAS = False
if __name__ == '__main__':
    # Heroku support: bind to PORT if defined, otherwise default to 5000.
    if 'PORT' in os.environ:
        port = int(os.environ.get('PORT'))
        host = '0.0.0.0'
    else:
        port = 5000
        host = '127.0.0.1'

	app.run(host=host, port=port)