"""INTENTIONALLY VULNERABLE views. Run on 127.0.0.1 only."""
import json
from django.db import connection
from django.http import HttpResponse,HttpResponseBadRequest,JsonResponse
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Employee,Document,Comment
from .challenges import CHALLENGES,FLAGS

def dashboard(request):
 solved=request.session.get('solved',[])
 return render(request,'lab/dashboard.html',{'challenges':CHALLENGES,'solved':solved,'points':sum(c['points'] for c in CHALLENGES if c['id'] in solved),'total':sum(c['points'] for c in CHALLENGES)})

def page(request,heading,section,**kwargs):
 return render(request,'lab/page.html',{'heading':heading,'section':section,**kwargs})

def robots(request):
 return HttpResponse('User-agent: *\nDisallow: /hidden/backups/\n',content_type='text/plain')

def robot_secret(request):
 return HttpResponse('Fictional backup note\n'+FLAGS['robots'],content_type='text/plain')

def directory(request):
 return page(request,'Employee directory','directory',people=Employee.objects.filter(is_public=True))

def employee(request,employee_id):
 # VULN 4: No access check on the requested record.
 return page(request,'Employee record','employee',person=get_object_or_404(Employee,pk=employee_id))

def archive(request):
 q=request.GET.get('q','');rows=[]
 if q:
  # VULN 5: Query constructed from untrusted input, rather than parameters.
  sql=f"SELECT id,title,body FROM lab_document WHERE title LIKE '%{q}%' AND is_public=1"
  try:
   with connection.cursor() as cursor:
    cursor.execute(sql)
    rows=[{'title':r[1],'body':r[2]} for r in cursor.fetchall()]
  except Exception:
   rows=[]
 return page(request,'Document archive','archive',q=q,rows=rows)

def greeting(request):
 # VULN 6: name output deliberately rendered through |safe.
 return page(request,'Greeting terminal','greeting',name=request.GET.get('name','visitor'))

@csrf_exempt
def guestbook(request):
 if request.method=='POST':
  message=request.POST.get('message','')[:800]
  if message: Comment.objects.create(author=request.POST.get('author','Guest')[:40],message=message)
 # VULN 7: persisted HTML rendered with |safe; CSRF disabled for exercise.
 return page(request,'Guestbook','guestbook',comments=Comment.objects.order_by('-id')[:20])

def staff(request):
 # VULN 8: role comes from unsigned cookie.
 role=request.COOKIES.get('role','guest')
 return page(request,'Staff console','staff',role=role,staff_flag=FLAGS['cookie'] if role=='admin' else None)

def current_profile(request):
 return request.session.get('profile',{'display_name':'Guest Analyst','theme':'dark','is_vip':False})

def profile(request):
 return page(request,'Profile settings','profile',profile=current_profile(request))

@csrf_exempt
def profile_api(request):
 data=current_profile(request)
 if request.method=='POST':
  try: payload=json.loads(request.body)
  except (ValueError,UnicodeDecodeError):return HttpResponseBadRequest('Expected JSON')
  if not isinstance(payload,dict):return HttpResponseBadRequest('Expected JSON object')
  # VULN 9: attacker can update privileged is_vip field, not just public form fields.
  data.update({k:v for k,v in payload.items() if k in data})
  request.session['profile']=data
 return JsonResponse(data)

def vip(request):
 return page(request,'VIP area','vip',vip_flag=FLAGS['mass'] if current_profile(request)['is_vip'] is True else None)

@csrf_exempt
def reset(request):
 result=None
 if request.method=='POST':
  person=Employee.objects.filter(username=request.POST.get('username','')).first()
  # VULN 10: Recovery token derived deterministically from employee number.
  result=FLAGS['reset'] if person and request.POST.get('token')==str(person.employee_number)[-4:] else 'Invalid token.'
 return page(request,'Account recovery','reset',result=result)

@csrf_exempt
@require_POST
def xss_proof(request):
 # Educational proof helper, NOT strong verification of actual XSS execution.
 try: kind=json.loads(request.body).get('kind')
 except (ValueError,TypeError):return HttpResponseBadRequest('Invalid request')
 if kind not in ('reflected','stored'):return HttpResponseBadRequest('Invalid challenge')
 return JsonResponse({'flag':FLAGS[kind]})

@require_POST
def submit_flag(request):
 try: flag=json.loads(request.body).get('flag','').strip()
 except (ValueError,TypeError,AttributeError):return HttpResponseBadRequest('Expected flag JSON')
 kind=next((k for k,v in FLAGS.items() if v==flag),None)
 if not kind:return JsonResponse({'ok':False,'message':'Incorrect flag.'})
 solved=set(request.session.get('solved',[]));already=kind in solved;solved.add(kind)
 request.session['solved']=sorted(solved)
 return JsonResponse({'ok':True,'message':'Already solved.' if already else 'Flag captured!','challenge':kind})

@require_POST
def reset_progress(request):
 request.session['solved']=[]
 request.session['profile']={'display_name':'Guest Analyst','theme':'dark','is_vip':False}
 return JsonResponse({'ok':True})
