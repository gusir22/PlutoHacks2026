# Northstar CTF — Investigation report

**Student:** Gustavo Rivero  **Date:** 11/07/2026

For each of the ten exercises record the following:

## Challenge #03 — Information disclosure

**Difficulty:** Easy **Points:** 50

**1. Vulnerable feature / endpoint:**
http://127.0.0.1:8000/hidden/backups/ops.txt

**2. Reconnaissance and tools used:**
Robots.txt & Debug mode

**3. Steps to reproduce (include URL, HTTP method, input or browser-console command):**
Based on the description of the challenge, I went to the robots.txt page. I have used this to 
tell robot crawlers where I allow them to search through.

This robot.txt file had one dissallowed link at "/hidden/backups/". I appended this path to the 
URL base and it was actually a broken link path. Since this website has debug mode on, I saw all
possible URL paths. One in particular was completing the "/hidden/backups/" path by adding 
"ops.txt". Using that file path, I found the flag.

**4. Evidence (what happened, screenshot, response or console output):**
![Robots.txt File](evidence/gus/c3-1.png)
![Debug Screen](evidence/gus/c3-1.png)
![Flag](evidence/gus/c3-1.png)

**5. Flag captured:**
FLAG{robots_is_not_access_control}

**6. Root cause (what made this possible):**
First the Robots.txt exposed a hidden partial path; but ultimately got solved because
the developer left the website on Debug mode during production.

**7. Potential real-world impact:**
All URLs can be exposed; which can lead threat actors into the dangerous areas

**8. How a developer should prevent it:**
Ensure you go over your deployment checklist and NEVER leave debug on in a production website

---

## Challenge #06 — Reflected XSS

**Difficulty:** medium  **Points:** 150

**1. Vulnerable feature / endpoint:**
http://127.0.0.1:8000/greeting/?name=%3Cscript%3EclaimXssFlag%28%22reflected%22%29%3C%2Fscript%3E

**2. Reconnaissance and tools used:**
Cross Side Scripting

**3. Steps to reproduce (include URL, HTTP method, input or browser-console command):**
enter a script element with the claimXssFlag("reflected") JavaScript command into the form

**4. Evidence (what happened, screenshot, response or console output):**
![Hint](evidence/gus/c6-1.png)
![Script Input](evidence/gus/c6-2.png)
![Flag](evidence/gus/c6-3.png)

**5. Flag captured:**
FLAG{escape_reflected_input}

**6. Root cause (what made this possible):**
Not sanitizing the form input from users allowed me to
execute a script with custom JS

**7. Potential real-world impact:**
If we had this vulnerability on our production website,
we would be granting an open door to our entire website.
An attacker can execute their own code, change content
on the website and much more.

**8. How a developer should prevent it:**
Always validate and sanitize data to prevent scripting
issues. In the Django Framework specifically, all forms
should be accompanied with the {% csrf_token %} to prevent

---

## Final reflection

Which vulnerabilities were caused by trusting client input? Which were caused by accidentally exposing data? What defensive controls would you prioritize?
