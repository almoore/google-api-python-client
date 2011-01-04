# Copyright (C) 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Do the OAuth 1.0a three legged dance.

Do the OAuth 1.0a three legged dance for
a Buzz command line application. Store the generated
credentials in a common file that is used by
other example apps in the same directory.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

from apiclient.discovery import build
from apiclient.oauth import FlowThreeLegged
from apiclient.ext.authtools import run

moderator_discovery = build("latitude", "v1").auth_discovery()

flow = FlowThreeLegged(moderator_discovery,
                       # You MUST have a consumer key and secret tied to a
                       # registered domain to use the latitude API.
                       #
                       # https://www.google.com/accounts/ManageDomains
                       consumer_key='REGISTERED DOMAIN NAME',
                       consumer_secret='KEY GIVEN DURING REGISTRATION',
                       user_agent='google-api-client-python-latitude/1.0',
                       domain='REGISTERED DOMAIN NAME',
                       scope='https://www.googleapis.com/auth/latitude',
                       xoauth_displayname='Google API Latitude Example',
                       location='current',
                       granularity='city'
                       )

run(flow, 'latitude.dat')
