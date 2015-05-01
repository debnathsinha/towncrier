import webapp2
import pdb
import urllib
try:
    import json
except ImportError:
    import simplejson as json
import datetime
import os
import jinja2
import re
from datetime import datetime

IS_DEV_APPSERVER = 'development' in os.environ.get('SERVER_SOFTWARE', '').lower()

if IS_DEV_APPSERVER:
    redirect_uri = "http%3A%2F%2Flocalhost%3A8080%2Flinkedinoauthcallback"
    CLIENT_ID = '780s9463lf31t6'
    CLIENT_SECRET = 'Ik8mfwDMYGgTn3By'
else:
    # redirect_uri = "http%3A%2F%2Fgethelloapp.com%2Flinkedinoauthcallback"
    redirect_uri = "http://gethelloapp.com/linkedinoauthcallback"
    CLIENT_ID = '78y3j5z7tnzwt5'
    CLIENT_SECRET = '1K89KxkniwWTOyrf'


ROOT_PATH = os.path.dirname(__file__)
GMAILYTICS_TEMPLATE_PATH = os.path.join(ROOT_PATH,"templates") 
JINJA_ENV = jinja2.Environment(
                               loader=jinja2.FileSystemLoader(GMAILYTICS_TEMPLATE_PATH),
                                extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class MainPage(webapp2.RequestHandler):
    
    def get(self):
        template = JINJA_ENV.get_template("news.html")
        self.response.write(template.render())

class DetailPage(webapp2.RequestHandler):
    
    def get(self, detail_name):
        print detail_name
        template = JINJA_ENV.get_template(detail_name)
        self.response.write(template.render())

config = {}
config['webapp2_extras.sessions'] = {
                                     'secret_key' : 'tcsecret',
                                     'cookie_name': 'tcsession'
                                     }

routes = [
    ('/', MainPage),
    ('/(.*)', DetailPage)
]

def app():
    from google.appengine.ext.appstats import recording
    app = webapp2.WSGIApplication(routes, config = config, debug=True)
    app = recording.appstats_wsgi_middleware(app)
    return app

application = app()
