"""Restore fictional records; no real identities or passwords."""
from django.core.management.base import BaseCommand
from lab.challenges import FLAGS
from lab.models import Employee,Document,Comment
class Command(BaseCommand):
 help='Reset fictional CTF data'
 def handle(self,*args,**kwargs):
  Comment.objects.all().delete();Document.objects.all().delete();Employee.objects.all().delete()
  Employee.objects.create(id=1,name='Jamie Chen',username='jamie',employee_number=1008,is_public=True,private_note='Public team member')
  Employee.objects.create(id=2,name='Taylor Ross',username='taylor',employee_number=1033,is_public=True,private_note='Public team member')
  Employee.objects.create(id=3,name='Alex Morgan',username='alex',employee_number=1042,is_public=False,private_note='CONFIDENTIAL: '+FLAGS['idor'])
  Document.objects.create(title='Company Handbook',body='Welcome to Northstar.',is_public=True)
  Document.objects.create(title='Holiday Calendar',body='Office closed on public holidays.',is_public=True)
  Document.objects.create(title='Restricted Board Minutes',body=FLAGS['sqli'],is_public=False)
  Comment.objects.create(author='Facilities',message='Welcome to the guestbook.')
  self.stdout.write(self.style.SUCCESS('Fictional CTF data seeded.'))
