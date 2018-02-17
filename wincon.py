import urllib.request, urllib.error, urllib.parse
import json
import sys, os, zipfile
from urllib.request import urlopen
import builtins as bi
class WinCon:

	def __init__(self):
		pass

	def loadFromJSON(self, json_url, to_download_to):
		#Load data from json onto string
		req = urllib.request.Request(json_url)
		opener = urllib.request.build_opener()
		file = opener.open(req)
		j = json.loads(file.read())
		title = ""
		description = ""
		download_url = ""
		for line in range(len(j)):
			title = j[line]['title']
			description = j[line]['description']
			download_url = j[line]['download_url']

			self.print("<<TITLE>>")
			self.print(title)
			self.print("<<DESCRIPTION>>")
			self.print(description)
			self.print("<<URL>>")
			self.print(download_url)

		#Downloading

		urllib.request.urlretrieve(download_url, to_download_to)
		print("<<DONE>>")

	def print(self,*args, **kwargs):
		if("--output-logs" in sys.argv):
			return bi.print(*args, **kwargs)
		else:
			return None

	def zipWinCon(self, path, ziph):
		for root, dirs, files in os.walk(path):
			for file in files:
				ziph.write(os.path.join(root, file))

	def makeWinCon(self, path, to):
		zipf = zipfile.ZipFile(to + ".win", 'w', zipfile.ZIP_DEFLATED)
		self.zipWinCon(path, zipf)
		zipf.close()

	def decompressWinCon(self, path, to):
		zip_ref = zipfile.ZipFile(path, 'r')
		zip_ref.extractall(to)
		zip_ref.close()
