import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from data-classes import SubmissionRecord, SubmissionDatabase, UserAccount

the_jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    undefined = jinja2.StrictUndefined,
    autoescape = True
)


# the handler section
class HomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('/templates/main-page.html')
        self.response.write(welcome_template.render())
    def post(self):
        pass

# the handler section
class TagInfoPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('/templates/tag-info.html')
        self.response.write(welcome_template.render())
    def post(self):
        pass

# the handler section
class DepartmentInfoPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('/templates/department-info.html')
        self.response.write(welcome_template.render())
    def post(self):
        reportdescription = self.request.get("")
        pass

# the handler section
class FormPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('/templates/form-page.html')
        self.response.write(welcome_template.render())
    def post(self):

        pass

# the handler section
class SubmissionConfirmedPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('/templates/submission-confirmed-page.html')
        self.response.write(welcome_template.render())
    def post(self):
        pass



# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/tag-info', TagInfoPage),
    ('/department-info', DepartmentInfoPage),
    ('/report', FormPage),
    ('/report-confirmed', SubmissionConfirmedPage)
], debug = True)
