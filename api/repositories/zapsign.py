import requests
import string
import json
import os

class ZapSignRepository:
    api_key = os.getenv('API_KEY_ZAPSIGN')
    base_url = os.getenv('URL_ZAPSIGN')

    def sign_document_from_url(name, document_url, signers, lang):
        try:
            endpoint = f"{ZapSignRepository.base_url}/docs"
            headers = {
                "Authorization": f"Bearer {ZapSignRepository.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "url_pdf": document_url,
                "signers": signers,
                "lang": lang,
                "name": name
            }
            response = requests.post(endpoint, json=payload, headers=headers)
            return response.json()
        except Exception as e:
            return {'error': str(e)}
