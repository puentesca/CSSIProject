#SubmissionRecord, SubmissionDatabase, UserAccount
import time
import datetime
from google.appengine.ext import ndb, users


# Stores data representing a submission (report)
class LocalSubmissionRecord(object):
    def __init__(self, username, email, image_url, description, location, tags, urgency):

        self.time_submitted = time.time()
        self.username = username
        self.email = email
        self.image_url = image_url
        self.description = description
        self.location = location
        self.tags = tags
        self.urgency = urgency

    def ConvertToCloudReadable(self):
        cloudRecord = CloudSubmissionRecord(time_submitted = self.time_submitted, username = self.username, email = self.email, image_url = self.image_url, description = self.description, location = self.location, tags = self.tags, urgency = self.urgency)
        return cloudRecord

    def __str__(self):
        msg = ""
        msg += "TIME: %s USERNAME: '%s' EMAIL: '%s': \n\nSubmission: (Urgency: %s)\n" % (datetime.datetime.fromtimestamp(self.time_submitted).strftime('%c'), self.username, self.email, self.urgency)
        msg += "Image url: %s\n" % (self.image_url)
        msg += "Description: %s\n" % (self.description)
        msg += "Location: %s\n" % (self.location)
        msg += "Tags: %s\n" % (self.tags)
        return msg

class CloudSubmissionRecord(ndb.Model):
    time_submitted = ndb.FloatProperty(required = True)
    username = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    image_url = ndb.StringProperty(required = False)
    description = ndb.StringProperty(required = False)
    location = ndb.StringProperty(required = True)
    tags = ndb.StringProperty(required = True)
    urgency = ndb.StringProperty(required = True)
            #CONVERT TO DATASTORE


#Holds submission records
class SubmissionDatabase(ndb.Model):

    submissions = []

    def __init__(self, name):
        self.name = name
    # Adds a record of a submission
    def logS(self, submission):
        self.submissions.append(submission)

    def __str__(self):
        msg = "%s Database" % (self.name)
        msg += "\n\nTransactions:\n"
        for t in self.submissions:
            msg += str(t) + "----------------------------------------------------------\n"
        return msg

class UserAccount(ndb.Model):
    username = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    report_database = ndb.StringProperty(required = True)
