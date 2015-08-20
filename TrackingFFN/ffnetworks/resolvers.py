import dns
from ipwhois import IPWhois


from .models import Domain, ASN, Node



def resolver():

	for d in Domain.objects.filter(track=True):
		print(d)
		new_hosts = d.resolve()

		if len(new_hosts) > 0:

			for host in new_hosts:
				print(host)
				#d.nodes.filter()

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
