# slack.py

from fastapi import Request

CLIENT_ID = 'e19917e3-8f20-4daa-8fbc-c87595da3bfd'
CLIENT_SECRET = '2c4668fd-8016-4afe-b3dd-99d41f1fca5f'
REDIRECT_URI = 'http://localhost:8000/integrations/hubspot/callback'

async def authorize_hubspot(user_id, org_id):
    # TODO
    pass

async def oauth2callback_hubspot(request: Request):
    # TODO
    pass

async def get_hubspot_credentials(user_id, org_id):
    # TODO
    pass

async def create_integration_item_metadata_object(response_json):
    # TODO
    pass

async def get_items_hubspot(credentials):
    # TODO
    pass