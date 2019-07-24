import webapp2
import jinja2
import os
import json
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
from data_classes import LocalSubmissionRecord,  CloudSubmissionRecord, SubmissionHandler#, UserAccount
api2key="AIzaSyAxRqWmRH0WoaqkSYbLOMIg3roBnPJTqFo"

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

        url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + api2key
        api_location = urlfetch.fetch( url, method="POST")
        json_data = json.loads(api_location.content)
        lat = json_data["location"]["lat"]
        lng = json_data["location"]["lng"]
        url2 = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat)+","+str(lng)+"&key=" + api2key
        api_location = urlfetch.fetch(url2, method="POST")
        json_data = json.loads(api_location.content)
        location_addresses = json_data["results"]
        formatted_addresses = []
        for address in location_addresses:
            formatted_addresses.append(address["formatted_address"])
        print("formatted_addresses")
        url3 = "https://www.google.com/maps/embed/v1/view?center=" + str(lat) + "," + str(lng) + "&key=AIzaSyAxRqWmRH0WoaqkSYbLOMIg3roBnPJTqFo"
        print(url3)
        # location_suggestions = json_data[results][0, 15]["formatted_address"]
        template_values =  {
        "addr": formatted_addresses,
        # "suggestions": location_suggestions
        }

        #AIzaSyAxRqWmRH0WoaqkSYbLOMIg3roBnPJTqFo



        self.response.write(welcome_template.render(template_values))
    def post(self):
        report_name =  self.request.get("name")
        report_email = self.request.get("email")


        report_image_url = self.request.get("image-url")
        report_description = self.request.get("description")
        report_location = self.request.get("location")
        report_location = self.request.get("location suggestions")
        report_tags = self.request.get("tags")
        report_urgency = self.request.get("urgency-level")
        report_record = LocalSubmissionRecord(name = report_name, email = report_email, image_url = report_image_url, description = report_description, location = report_location, tags = report_tags, urgency = report_urgency)
        cloud_record = report_record.ConvertToCloudReadable()
        #print(cloud_record)
        print(cloud_record.put())
        emailer = SubmissionHandler()
        emailer.sendSubmission(report_record)


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
