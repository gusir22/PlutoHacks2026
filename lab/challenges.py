"""Training-only flags; never treat source-embedded flags as secrets."""
DATA=[
 ('source','A Note in Plain Sight','Easy','HTML comments',50,'Inspect the public homepage source.','Use View Page Source.'),
 ('javascript','Frontend Exposure','Easy','JavaScript exposure',50,'Find an accidentally exposed secret in public JS.','Inspect the Sources tab in developer tools.'),
 ('robots','A Helpful Crawler','Easy','Information disclosure',50,'Find a supposedly hidden path disclosed to crawlers.','Try /robots.txt.'),
 ('idor','Someone Else’s Profile','Medium','IDOR',100,'Find a nonpublic employee record by manipulating a numeric URL.','Neighboring record IDs may still be accessible.'),
 ('sqli','The Leaky Archive','Medium','SQL injection',150,'Find a restricted document using the archive search.','Think about quotation marks and OR conditions.'),
 ('reflected','Unsafe Greeting','Medium','Reflected XSS',150,'Demonstrate script execution through a greeting parameter.','Execute claimXssFlag("reflected") from injected HTML.'),
 ('stored','The Guestbook','Medium','Stored XSS',150,'Persist HTML in the guestbook and trigger script execution.','Execute claimXssFlag("stored") in a submitted message.'),
 ('cookie','Trusting the Browser','Easy','Cookie-based access',100,'Gain staff access by modifying browser-controlled data.','A role cookie controls the staff portal.'),
 ('mass','Too Many Fields','Hard','Mass assignment',200,'Change a hidden attribute using the profile JSON API.','Look for is_vip in GET /api/profile/.'),
 ('reset','Predictable Recovery','Hard','Weak reset token',200,'Derive a reset code from fictional employee metadata.','The token is the last four digits of alex’s employee number.'),
]
CHALLENGES=[dict(zip(('id','name','difficulty','category','points','description','hint'),x)) for x in DATA]
FLAGS={
 'source':'FLAG{html_comments_are_public}',
 'javascript':'FLAG{frontend_code_is_not_secret}',
 'robots':'FLAG{robots_is_not_access_control}',
 'idor':'FLAG{ids_are_not_permissions}',
 'sqli':'FLAG{parameterize_your_sql}',
 'reflected':'FLAG{escape_reflected_input}',
 'stored':'FLAG{sanitize_stored_content}',
 'cookie':'FLAG{never_trust_client_roles}',
 'mass':'FLAG{allowlist_mutable_fields}',
 'reset':'FLAG{randomize_reset_tokens}',
}
