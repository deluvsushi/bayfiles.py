from requests import get
from requests import post


class BayFiles:
	def __init__(self) -> None:
		self.api = "https://api.bayfiles.com"
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Android; U; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/33.0"
		}
		
	def upload_file(self, file: str) -> dict:
		files = {"file": open(file, "rb")}
		return post(
			f"{self.api}/upload",
			files=files,
			headers=self.headers).json()
		
	def get_file_info(self, file_id: str) -> dict:
		return get(
			f"{self.api}/v2/file/{file_id}/info",
			headers=self.headers).json()
