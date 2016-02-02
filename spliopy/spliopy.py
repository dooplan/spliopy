# -*- coding: utf-8 -*-
import requests
import json 
import base64

API_ENDPOINT = 's3s.fr/api/rest/2/'

STATUS_CODES = {
    200: 'OK',
    201: 'Created',
    202: 'Accepted, The request has been accepted for processing',
    204: 'No Content',
    304: 'Not Modified',
    400: 'Bad Request',
    401: 'Unauthorized, You must enter a valid ID \
        and password to access this resource',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable, Requested data format not supported',
    500: 'Internal Server Error, Something is broken',
    501: 'Not Implemented',
}

class SplioConnection(object):

    def __init__(self, api_key, universe,):
        '''
        An api connection is defined by an api_key and a universe
        '''
        self._api_key = api_key
        self._universe = universe

    def request(self, method, path, payload={}):
        '''
        Make an api request 
        '''
        headers = {}
        headers['Content-Type'] = 'application/json; charset:utf-8'
        headers['Authorization'] = 'Basic %s' % base64.b64encode("%s:%s" % \
            (self._universe, self._api_key))

        response = getattr(requests, method)(
                        'https://%s' % API_ENDPOINT + path,
                        headers=headers,
                        data=json.dumps(payload),
                    )
        return response

    def get_lists(self):
        '''
        Returns all lists defined for the universe.
        '''
        return self.request('get','lists').json()

    def get_fields(self):
        '''
        Returns custom fields relevant for the universe.
        '''
        return self.request('get','fields').json()

    def get_contact(self, email):
        '''
        Returns all known attributes for a contact identified by email.
        '''
        return self.request('get', 'contact/%s' % email).json()

    def add_contact(self, contact_data={}):
        '''
        Creates a new contact. It is mandatory to provide the email address 
        within the fields.
        '''
        return self.request('post','contact', contact_data).json()

    def update_contact(self, email, update_data={}):
        '''
        Updates an existing contact identified by email.
        '''
        return self.request('put','contact/%s' % email, update_data).json()

    def blacklist(self, email):
        '''
        Blacklist email in the universe.
        '''
        return self.request('post','blacklist/%s' % email)

    def is_blacklisted(self, email):
        '''
        Check if email is blacklisted in the universe.
        '''
        response = self.request('get','blacklist/%s' % email)
        return True if response.status_code == 200 else False