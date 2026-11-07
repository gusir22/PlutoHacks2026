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

## Challenge #___ — ______________________

**Difficulty:** ______  **Points:** ______

**1. Vulnerable feature / endpoint:**

**2. Reconnaissance and tools used:**

**3. Steps to reproduce (include URL, HTTP method, input or browser-console command):**

**4. Evidence (what happened, screenshot, response or console output):**

**5. Flag captured:**

**6. Root cause (what made this possible):**

**7. Potential real-world impact:**

**8. How a developer should prevent it:**

---

## Final reflection

Which vulnerabilities were caused by trusting client input? Which were caused by accidentally exposing data? What defensive controls would you prioritize?
