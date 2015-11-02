
from django.db import models
import dns



class Domain(models.Model):

	FAST_FLUX_NETWORK_TYPE = (
		('SINGLE', 'Single-Flux Networks'),
		('DOUBLE', 'Double-Flux Networks'),
	)

	url = models.CharField(max_length=50,verbose_name="URL");
	submit_date = models.DateField(verbose_name="Submit Date", auto_now_add=True)
	last_seen = models.DateField(verbose_name="Last Seen")
	live = models.BooleanField(verbose_name="Live")
	track = models.BooleanField(verbose_name="Track")
	domain_type = models.CharField(verbose_name="Fast Flux Network Type", choices=FAST_FLUX_NETWORK_TYPE, default='SINGLE', max_length=6)


	def resolve(self, type):
		return dns.resolver.query(self.url, type)


	def __str__(self):
		return self.url

class ASN(models.Model):
	
	#We need to define in the model some place to save the IP Blocks of the ASNs

	number = models.CharField(verbose_name="ASN Number", max_length=50)
	
	as_name = models.CharField(verbose_name="AS Name", max_length=200, null=True, blank=True)
	country = models.CharField(verbose_name="Country", max_length="2")
	domain = models.CharField(verbose_name="Domain URL", max_length="50", null=True, blank=True)
	isp = models.CharField(verbose_name="ISP Name", max_length="200", null=True, blank=True)

	full_info = models.TextField(null=True,blank=True)

	def __str__(self):
		return str(self.number) + "-" + str(self.country)



class Node(models.Model):

	DNS_REGISTRY_TYPE = (
		(1, 'A'),
		(2, 'NS'),
	)

	asn = models.ForeignKey(ASN, related_name="nodes", null=True, blank=True)
	domain = models.ForeignKey(Domain, related_name="nodes")
	ip = models.GenericIPAddressField(protocol="both", verbose_name="IP")
	date_detected = models.DateField(verbose_name="Date Detected", auto_now_add=True)
	dns_registry_type = models.CharField(verbose_name="DNS Registry Type", choices=DNS_REGISTRY_TYPE, max_length="2")

	submit_date = models.DateField(verbose_name="Submit Date", auto_now_add=True, blank=True)

	def __str__(self):
		return self.ip