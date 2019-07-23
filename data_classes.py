#SubmissionRecord, SubmissionDatabase, UserAccount
import time
import datetime


# Stores data representing a submission (report)
class SubmissionRecord(object):
    def __init__(self, username, email, image_url, description, location, tags, urgency):
        self.time_submitted = time.time()
        self.username = username
        self.email = email
        self.image_url = image_url
        self.description = description
        self.location = location
        self.tags = tags
        self.urgency = urgency

    def __str__(self):
        msg = ""
        msg += "TIME: %s USERNAME: '%s' EMAIL: '%s': \n\nSubmission: (Urgency: %s)\n" % (datetime.datetime.fromtimestamp(self.time_submitted).strftime('%c'), self.username, self.email, self.urgency)
        msg += "Image url: %s\n" % (self.image_url)
        msg += "Description: %s\n" % (self.description)
        msg += "Location: %s\n" % (self.location)
        msg += "Tags: %s\n" % (self.tags)
        return msg




#Holds submission records
class SubmissionDatabase(object):

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

#class UserAccount(object):
