from suds import WebFault
from suds.client import Client


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def is_project_added(self, username, password, project):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_project_add(username, password, project)
            return True
        except WebFault:
            return False

    def is_project_deleted(self, username, password, id):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_project_delete(username, password, id)
            return True
        except WebFault:
            return False
