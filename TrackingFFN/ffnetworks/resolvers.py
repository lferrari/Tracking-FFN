import dns
from ipwhois import IPWhois


from .models import Domain, ASN, Node



def resolver():
	'''
		Take into account this http://tools.ietf.org/html/rfc1035#section-3.3.9 for the records A and NS
	'''


	for d in Domain.objects.filter(track=True):
		print(d)
		answer = d.resolve("A")

		if len(answer) > 0:

			for rdata in answer:
				print(rdata)
				obj, created = Node.objects.get_or_create(domain=d, 
													ip=rdata.to_text(), 
													dns_registry_type=1)
				if created:
					print("New Host: " + rdata.to_text())
				else: 
					print("Host already in DB")
				'''
				Check ASN Host
				'''
				if not obj.asn:
					'''
						retrieve and asign ASN information
					'''
					asn_info = IPWhois(rdata.to_text()).lookup()


					if asn_info['asn'] != '':
						asn_object, created = ASN.objects.get_or_create(number=asn_info['asn'], \
							country=asn_info['asn_country_code'], isp=asn_info['asn_registry'])

						if created:
							asn_object.full_info = str(asn_info)
							asn_object.save()

	return True

