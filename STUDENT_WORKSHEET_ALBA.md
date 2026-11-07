# Northstar CTF — Investigation report

**Student:** Albany Tafuro  **Date:** 11/07/2026

For each of the ten exercises record the following:

## Challenge #1 — HTML Comments

**Difficulty:** Easy  **Points:** 50

**1. Vulnerable feature / endpoint:** 
The flag was exposed in an HTML comment within the homepage source code. 

URL: `view-source:http://127.0.0.1:8000/`

**2. Reconnaissance and tools used:** 
Browser Developer Tools and the View Page Source feature.

**3. Steps to reproduce (include URL, HTTP method, input or browser-console command):**

1. Navigate to `http://127.0.0.1:8000/` using a web browser.
2. Right-click anywhere on the homepage and select "View Page Source."
3. Examine the HTML source code for comments containing sensitive information.
4. Locate the exposed flag within an HTML comment.

**4. Evidence (what happened, screenshot, response or console output):** 

The homepage source code contained an HTML comment exposing the challenge flag.

![Challenge 1 screenshot](evidence/alba/c1-1.png)

**5. Flag captured:** Public deployment comment: 

`FLAG{html_comments_are_public}`

**6. Root cause (what made this possible):** 

The developer included sensitive information in an HTML comment. Although HTML comments are not displayed on the rendered webpage, they remain accessible to anyone inspecting the page's source code.

**7. Potential real-world impact:**

In a real-world application, exposing sensitive information through HTML comments could allow attackers to discover internal application details, hidden endpoints, or accidentally disclosed credentials. This information could assist attackers in identifying additional vulnerabilities or gaining unauthorized access.

**8. How a developer should prevent it:** 

Developers should never include sensitive information, such as passwords, API keys, authentication tokens, or internal configuration details, in HTML comments or other client-side code. Sensitive information should remain on the server and should never be included in the HTML response sent to the browser. 

---

## Challenge #2 — JavaScript Exposure

**Difficulty:** Easy  **Points:** 50 

**1. Vulnerable feature / endpoint:** Finding a secret flag in the app.js file 
http://127.0.0.1:8000/static/lab/app.js

**2. Reconnaissance and tools used:** View page source

**3. Steps to reproduce (include URL, HTTP method, input or browser-console command):** View page source, followed by clicking on app.js file flag was there

**4. Evidence (what happened, screenshot, response or console output):** ![Challange 2 screenshot](evidence/alba/c2-2.png)

**5. Flag captured:** An exposed synthetic secret: FLAG{frontend_code_is_not_secret}

**6. Root cause (what made this possible):** The flag was hidden into the app.js file within a comment. 

**7. Potential real-world impact:** JavaScript can be use to inject malicious code. A comment like this can contribute to the use of such.

**8. How a developer should prevent it:** 

---

## Challenge #3 — Information disclosure

**Difficulty:** Easy  **Points:** 50

**1. Vulnerable feature / endpoint:** 
http://127.0.0.1:8000/hidden/backups/ops.txt

**2. Reconnaissance and tools used:** View page source, 404 page url's

**3. Steps to reproduce (include URL, HTTP method, input or browser-console command):**
/robots.txt was input in the url, then user agent was allowed to everyone and provided additional piece of information '/hidden/backups/' this took me to 404 page where debug was enable and expose the remainder of the URL ops.txt 

**4. Evidence (what happened, screenshot, response or console output):**
![Challenge 3 screenshot 1](evidene/alba/c3-1.png)
![Challenge 3 screenshot 2](evidence/alba/c3-2.png)
![Challenge 3 screenshot 3](evidence/alba/c3-3.png)

**5. Flag captured:** FLAG{robots_is_not_access_control}

**6. Root cause (what made this possible):** The Robot.txt was allowed to everyone and debug was allowed

**7. Potential real-world impact:** Debug was enable allowing to have a 404 page with expose url's

**8. How a developer should prevent it:**

---

## Challenge #4 —  IDOR

**Difficulty:** Medium  **Points:** 100

**1. Vulnerable feature / endpoint:** http://127.0.0.1:8000/directory/3/

**2. Reconnaissance and tools used:** Followed URL pattern, no additional tools

**3. Steps to reproduce (include URL, HTTP method, input or browser-console command):**
I checked the URL pattern to see if adding additional number would bring me to an employee that may not be displayed. Took me to where the Flag was

**4. Evidence (what happened, screenshot, response or console output):**
![Challenge 4](evidence/alba/c4-1.png)

**5. Flag captured:** 

**6. Root cause (what made this possible):**

**7. Potential real-world impact:**

**8. How a developer should prevent it:**

---

## Challenge #5 — SQL Injection

**Difficulty:** Medium  **Points:** 100

**1. Vulnerable feature / endpoint:** http://127.0.0.1:8000/archive/?q=%27+OR+%271%27%3D%271%27%3B+--

**2. Reconnaissance and tools used:** Google search engine to find SQL injections

**3. Steps to reproduce (include URL, HTTP method, input or browser-console command):**
Use google to find SQL injection code and implemented in the search bar in the document archive page

**4. Evidence (what happened, screenshot, response or console output):**
![Challenge 5](evidence/alba/c5-1.png)

**5. Flag captured:** FLAG{parameterize_your_sql}

**6. Root cause (what made this possible):** An attacker can manipulate this by injecting: ' OR '1'='1'; --

**7. Potential real-world impact:** Atacker can manipulate a dabate.

**8. How a developer should prevent it:** Add restrictions to true. 

---

## Challenge #6 — Reflected XSS

**Difficulty:** Medium  **Points:** Medium

**1. Vulnerable feature / endpoint:**

**2. Reconnaissance and tools used:**

**3. Steps to reproduce (include URL, HTTP method, input or browser-console command):**

**4. Evidence (what happened, screenshot, response or console output):**

**5. Flag captured:**

**6. Root cause (what made this possible):**

**7. Potential real-world impact:**

**8. How a developer should prevent it:**

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
