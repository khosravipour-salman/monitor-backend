INTERN = 'intern'
COMPANY = 'company'
MENTOR = 'mentor'
ADMIN = 'admin'

USER_ROLE_CHOICES = (
	(INTERN, 'Intern'),
	(COMPANY, 'Company'),
	(MENTOR, 'Mentor'),
	(ADMIN, 'Admin'),
)

EXEMPT = 'exempt'
NOT_SERVED = 'not_served'
SERVING = 'serving'
SERVED = 'served'
SCHOLAR = 'scholar'

MILITARY_STATUS_CHOICES = (
	(EXEMPT, 'Exempt'),
	(NOT_SERVED, 'NotServed'),
	(SERVING, 'Serving'),
	(SERVED, 'Served'),
	(SCHOLAR, 'Scholar'),
)