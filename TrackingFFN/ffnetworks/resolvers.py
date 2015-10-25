import dns
from ipwhois import IPWhois


from .models import Domain, ASN, Node



def resolver():

	for d in Domain.objects.filter(track=True):
		print(d)
		answer = d.resolve()

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
	return True


'''
				asn_info = IPWhois(str(host))

				if asn_info['asn'] != '':
					asn_object = ASN.objects.get_or_create(number=asn_info['asn'], country=asn_info['asn_country_code'])

					if asn_object[1] == True:
						asn_object[0].full_info = str(asn_info)
					# get_or_create of nodes


				else:
					print("raise Error")
'''
