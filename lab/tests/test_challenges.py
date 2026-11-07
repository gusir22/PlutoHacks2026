"""End-to-end checks for all ten deliberately vulnerable training scenarios."""
import json
from django.core.management import call_command
from django.test import TestCase
from lab.challenges import FLAGS,CHALLENGES

class LabTests(TestCase):
 @classmethod
 def setUpTestData(cls):
  call_command('seed_lab',verbosity=0)

 def test_dashboard_and_asset_flags(self):
  r=self.client.get('/')
  self.assertEqual(r.status_code,200)
  self.assertContains(r,FLAGS['source'])
  self.assertEqual(len(CHALLENGES),10)

 def test_robots_discloses_hidden_page(self):
  self.assertContains(self.client.get('/robots.txt'),'hidden/backups/')
  self.assertContains(self.client.get('/hidden/backups/ops.txt'),FLAGS['robots'])

 def test_idor_private_record(self):
  self.assertContains(self.client.get('/directory/3/'),FLAGS['idor'])

 def test_sql_injection_reveals_restricted_document(self):
  self.assertNotContains(self.client.get('/archive/',{'q':'Restricted'}),FLAGS['sqli'])
  self.assertContains(self.client.get('/archive/',{'q':"' OR 1=1 -- "}),FLAGS['sqli'])

 def test_reflected_xss_is_unescaped(self):
  self.assertContains(self.client.get('/greeting/',{'name':'<script>claimXssFlag("reflected")</script>'}),'<script>claimXssFlag("reflected")</script>',html=False)

 def test_stored_xss_is_unescaped(self):
  self.client.post('/guestbook/',{'author':'Tester','message':'<script>claimXssFlag("stored")</script>'})
  self.assertContains(self.client.get('/guestbook/'),'<script>claimXssFlag("stored")</script>',html=False)

 def test_role_cookie(self):
  self.assertNotContains(self.client.get('/staff/'),FLAGS['cookie'])
  self.client.cookies['role']='admin'
  self.assertContains(self.client.get('/staff/'),FLAGS['cookie'])

 def test_mass_assignment(self):
  self.assertNotContains(self.client.get('/vip/'),FLAGS['mass'])
  r=self.client.post('/api/profile/',data=json.dumps({'is_vip':True}),content_type='application/json')
  self.assertTrue(r.json()['is_vip'])
  self.assertContains(self.client.get('/vip/'),FLAGS['mass'])

 def test_predictable_reset(self):
  self.assertContains(self.client.post('/reset/',{'username':'alex','token':'1042'}),FLAGS['reset'])

 def test_flag_submission_and_scoring(self):
  response=self.client.post('/api/submit/',data=json.dumps({'flag':FLAGS['source']}),content_type='application/json')
  self.assertTrue(response.json()['ok'])
  self.assertContains(self.client.get('/'),'50 <sub>/')
  self.client.post('/api/progress/reset/',data='{}',content_type='application/json')
  self.assertContains(self.client.get('/'),'0 <sub>/')

 def test_xss_proof_helper(self):
  response=self.client.post('/api/xss-proof/',data=json.dumps({'kind':'stored'}),content_type='application/json')
  self.assertEqual(response.json()['flag'],FLAGS['stored'])
