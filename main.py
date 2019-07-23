import webapp2
import jinja2
import os
from google.appengine.ext import ndb
<<<<<<< HEAD
# from data_classes import SubmissionRecord, SubmissionDatabase, UserAccount
=======
from data_classes import SubmissionRecord, SubmissionDatabase#, UserAccount
>>>>>>> d722c6acc510735983a75e4b627e0a4f2d6297c1

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
        pass

# the handler section
class FormPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('/templates/form-page.html')
        self.response.write(welcome_template.render())
    def post(self):
        report_username = "test username" #self.request.get("username")
        report_email = "test email" #self.request.get("email")
        report_image_url = self.request.get("image-url")
        report_description = self.request.get("description")
        report_location = self.request.get("location")
        report_tags = self.request.get("tags")
        report_urgency = self.request.get("urgency-level")
        record = SubmissionRecord(username = report_username, email = report_email, image_url = report_image_url, description = report_description, location = report_location, tags = report_tags, urgency = report_urgency)
        print(record)

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
