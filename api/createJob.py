from __future__ import print_function
from pkg_resources import resource_string
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.utils.crumb_requester import CrumbRequester

url = "jenkinsURL"
username = "username"
password = "password"
crumb_requester = CrumbRequester(baseurl=url, username=username, password=password)
j = Jenkins(url, username=username, password=password, requester=crumb_requester)
job_name = 'jaydeepCreatedByPythonTest-4'
xml = resource_string(__name__, 'job.xml')

print(xml)

job = j.create_job(jobname=job_name, xml=xml)

# Get job from Jenkins by job name
my_job = j[job_name]
print(my_job)
