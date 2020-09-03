from __future__ import print_function
from pkg_resources import resource_string
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.utils.crumb_requester import CrumbRequester

url = "url"
username = "username"
password = "password"
crumb_requester = CrumbRequester(baseurl=url, username=username, password=password)
j = Jenkins(url, username=username, password=password, requester=crumb_requester)
job_name = 'jobName'

job = j.delete_job(jobname=job_name)
print ("Job", job_name, "deleted")
