from instaloader import Instaloader
import instaloader
def getFollowList(num):
	if num < 10000:
		return str(num)
	elif num >= 10000 and num < 1000000:
		return str(round(num/1000,1))+'K'
	elif num >= 1000000 and num < 1000000000:
		return str(round(num/1000000,1))+'M'
	return str(round(num/10000,1)-0.2)+'B'


class getIgProfile:
	def __init__(self, userName):
		L = Instaloader()
		profile=instaloader.Profile.from_username(L.context,userName)
		self.full_name = profile.full_name
		self.user_id = profile.userid
		self.is_private = profile.is_private
		self.biography = profile.biography.split('\n')
		self.putBio = self.biography[0]
		self.get_posts = profile.get_posts()
		self.posts = self.get_posts.count
		self.followers = getFollowList(profile.followers)
		self.followees = getFollowList(profile.followees)
		self.profilePic = profile.get_profile_pic_url()
		self.is_verified =  profile.is_verified
		self.business = profile.is_business_account
		self.business_category_name = profile.business_category_name
		self.exURL = profile.external_url

L = Instaloader()
class featured:
	def popularcelebs(self):
		
		accounts = ['cristiano','therock', 'arianagrande', 'kyliejenner','selenagomez', 'kimkardashian','leomessi']
		
		popAccounts = []
		for account in accounts:
			popAccounts.append(getIgProfile(account))
		return popAccounts

	def fashionPages(self):
		accounts = ['camilacoelho', 'negin_mirsalehi', 'sincerelyjules', 'weworewhat', 'carodaur']
		popFashAccounts = []
		for account in accounts:
			popFashAccounts.append(getIgProfile(account))
		return popFashAccounts

	def popularPages(self):
		pass

	def popularAthletes(self):
		pass

	def popularActors(self):
		pass

	def popularModels(self):
		pass