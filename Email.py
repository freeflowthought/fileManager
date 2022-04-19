#create a email class

'''Import the email module'''
import smtplib
from email.mime.application import MIMEApplication
from socket import gethostname
import json
from utility import findFileByType
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





class Email:
    def __init__(self,srcEmail:str, toEmail:str):
        self.srcEmail = srcEmail
        self.toEmail = toEmail
        self.attachments = []

    '''this method load the attachment into the self.attachments properties'''
    def loadAttachments(self, fileType:str, filePath:str) ->list[str]:
        allFiles = findFileByType(fileType,filePath)
        self.attachments = [file for file in allFiles]


    def sendEmail(self,fileType:str,filePath:str):
        attachments = self.loadAttachments(fileType='.pdf',filePath='.')
        msg = MIMEMultipart()
        msg['From'] = self.srcEmail
        msg['To'] = self.toEmail
        #loop through all the attachments which being found
        for attachment in attachments:
            with open(attachment,"rb") as file:
                attach = MIMEApplication(file.read(),_subtype=fileType)
            '''add the header'''
            attach.add_header('Content-Disposition','attachment',filename=str(attachment))
        msg.attach(attach)



   

