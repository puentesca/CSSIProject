#SubmissionRecord, SubmissionDatabase, UserAccount
import time
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
# Import smtplib for the actual sending function
import smtplib
import ssl
#from smtplib import SMTP

# Import the email modules we'll need
#from email.mime.text import MIMEText

#for emailing



# Stores data representing a submission (report)
class LocalSubmissionRecord(object):
    def __init__(self, name, email, image_url, description, location, tags, urgency):

        self.time_submitted = time.time()
        self.name = name
        self.email = email
        self.image_url = image_url
        self.description = description
        self.location = location
        self.tags = tags
        self.urgency = urgency

    def ConvertToCloudReadable(self):
        cloudRecord = CloudSubmissionRecord(time_submitted = self.time_submitted, name = self.name, email = self.email, image_url = self.image_url, description = self.description, location = self.location, tags = self.tags, urgency = self.urgency)
        return cloudRecord

    def __str__(self):
        msg = ""
        msg += "TIME: %s NAME: '%s' EMAIL: '%s': \n\nSubmission: (Urgency: %s)\n" % (datetime.datetime.fromtimestamp(self.time_submitted).strftime('%c'), self.name, self.email, self.urgency)
        msg += "Image url: %s\n" % (self.image_url)
        msg += "Description: %s\n" % (self.description)
        msg += "Location: %s\n" % (self.location)
        msg += "Tags: %s\n" % (self.tags)
        return msg

class CloudSubmissionRecord(ndb.Model):
    time_submitted = ndb.FloatProperty(required = True)
    name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    image_url = ndb.StringProperty(required = False)
    description = ndb.StringProperty(required = False)
    location = ndb.StringProperty(required = True)
    tags = ndb.StringProperty(required = True)
    urgency = ndb.StringProperty(required = True)


#Holds submission records
class SubmissionHandler(object):


    def sendSubmission(self,submissionRecord):
        smtpServer = "smtp.gmail.com"
        smtpPort = 587
        forwardEmail = "cfcreportforward@gmail.com"
        forwardPassword = "CFCREPORT"
        recipientsEmail = "puentesc121@gmail.com" #submissionRecord.email
        print("Would be email: " + submissionRecord.email)
        subject = "Submission by: " + submissionRecord.name
        text = submissionRecord.__str__()
        smtp_server = smtplib.SMTP(smtpServer, smtpPort)
        smtp_server.ehlo()
        smtp_server.starttls()
        print("Server SMTP established")
        smtp_server.login(forwardEmail, forwardPassword)
        print("Server Login successful")
        message = "Subject: {}\n\n{}".format(subject, text)
        smtp_server.sendmail(forwardEmail, recipientsEmail, message)
        smtp_server.close()
        pass


class UserAccount(ndb.Model):
    username = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    report_database = ndb.StringProperty(required = True)
