import string
allowed = string.letters + string.digits + '_' + '-'

class Filter:
	
	def fun(in_val):

		check=all(c in allowed for c in in_val)
		if check:
			atindex=in_val.index('@')
			dotindex=in_val.index('.')

			if atindex<1 or dotindex<atindex+1 or dotindex+3>=len(in_val):
				return False
			else:
				return True
		else:
			return False



	def filter_mail(emails):
	    return filter(fun, emails)

	if __name__ == '__main__':
	    n = int(raw_input())
	    emails = []
	    for _ in range(n):
		emails.append(raw_input())

	    filtered_emails = filter_mail(emails)
	    filtered_emails.sort()
	    print filtered_emails
