import os
from simple_salesforce import Salesforce
from simple_salesforce.exceptions import SalesforceAuthenticationFailed

class SalesforceIntegration:
    def __init__(self):
        self.sf = None
        self._authenticate()

    def _authenticate(self):
        try:
            self.sf = Salesforce(
                username=os.environ.get('SALESFORCE_USERNAME'),
                password=os.environ.get('SALESFORCE_PASSWORD'),
                security_token=os.environ.get('SALESFORCE_SECURITY_TOKEN')
            )
        except SalesforceAuthenticationFailed:
            print("Salesforce authentication failed. Please check your credentials.")

    def attach_file_to_opportunity(self, opportunity_id, file_path, file_name):
        if not self.sf:
            print("Salesforce connection not established.")
            return False

        try:
            with open(file_path, 'rb') as file:
                body = file.read()

            attachment = self.sf.Attachment.create({
                'ParentId': opportunity_id,
                'Name': file_name,
                'Body': body
            })

            print(f"File attached successfully. Attachment ID: {attachment['id']}")
            return True
        except Exception as e:
            print(f"Error attaching file to opportunity: {str(e)}")
            return False

def attach_to_salesforce(opportunity_id, file_path):
    sf_integration = SalesforceIntegration()
    file_name = os.path.basename(file_path)
    return sf_integration.attach_file_to_opportunity(opportunity_id, file_path, file_name)