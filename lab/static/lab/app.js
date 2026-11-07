/* VULN 2: An exposed synthetic secret: FLAG{frontend_code_is_not_secret} */
const PUBLIC_BUILD_CONFIG={api:'/api',theme:'dark'};
function cookie(name){return document.cookie.split('; ').find(s=>s.startsWith(name+'='))?.split('=').slice(1).join('=')||''}
async function post(url,data){const r=await fetch(url,{method:'POST',headers:{'Content-Type':'application/json','X-CSRFToken':decodeURIComponent(cookie('csrftoken'))},body:JSON.stringify(data)});return r.json()}
// Student helper for proving reflected / stored script execution.
window.claimXssFlag=async function(kind){const r=await post('/api/xss-proof/',{kind});const output=document.createElement('div');output.className='success xss-result';output.textContent='XSS proof: '+r.flag;document.body.appendChild(output);return r.flag};
document.addEventListener('DOMContentLoaded',()=>{
document.querySelector('#flag-form')?.addEventListener('submit',async e=>{e.preventDefault();const input=document.querySelector('#flag-input');const data=await post('/api/submit/',{flag:input.value});const status=document.querySelector('#flag-status');status.textContent=data.message;status.className=data.ok?'good':'bad';if(data.ok)setTimeout(()=>location.reload(),650)});
document.querySelectorAll('.hint-toggle').forEach(b=>b.addEventListener('click',()=>{const hint=b.closest('.card').querySelector('.hint');hint.hidden=!hint.hidden;b.textContent=hint.hidden?'Hint':'Hide hint'}));
document.querySelector('#reset-progress')?.addEventListener('click',async()=>{if(!confirm('Reset solved flags and demo profile?'))return;await post('/api/progress/reset/',{});location.reload()});
document.querySelector('#profile-form')?.addEventListener('submit',async e=>{e.preventDefault();const data=await post('/api/profile/',Object.fromEntries(new FormData(e.target).entries()));document.querySelector('#profile-output').textContent=JSON.stringify(data,null,2)});

});
