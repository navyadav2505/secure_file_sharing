# RESTAPI-flask
 secure file-sharing system between two different types of users.
 
 Notice: Technical Issues Preventing Database Posting

Due to unforeseen technical constraints on my computer, I regret to inform you that I am currently unable to share the database associated with this project. I apologize for any inconvenience this may cause. However, I encourage you to explore the codebase thoroughly. Should you wish to witness the API in action, please do not hesitate to reach out. I am more than happy to assist in providing a demonstration. Your understanding and cooperation are greatly appreciated.

File-Sharing System with Secure Authentication
This repository contains a Python-based REST API for a secure file-sharing system. The system is designed to facilitate secure file sharing between two types of users: Operation User and Client User.
Features
Framework
This API can be integrated with Flask.
Database
Supports Mysql databases for data storage.
Implementation Details
Operation User Actions
Login

Authenticate using valid credentials.
Upload File

Only Operation Users are allowed to upload files.
Uploaded files must be in pptx, docx, or xlsx format.
Client User Actions
Sign Up

Register as a Client User.
Returns an encrypted URL for account activation.
Email Verification

A verification email will be sent to the registered email upon sign up.
Login

Authenticate using valid credentials.
Download File

Allows Client Users to download files shared by Operation Users.
List Uploaded Files

Provides a list of all uploaded files available for download.

#please add your email through which you want to send the mail at config.json
