import requests
import string
import json
import os

class ZapSignRepository:
    base_url = os.getenv('URL_ZAPSIGN')

    def sign_document_from_url(name, document_url, api_token, signers):
        try:
            endpoint = f"{ZapSignRepository.base_url}/docs"
            headers = {
                "Authorization": f"Bearer {api_token}",
                "Content-Type": "application/json"
            }
            
            valid_signers = [signer for signer in signers if signer.get('email') and signer.get('name')]

            payload = {
                "url_pdf": document_url,
                "signers": valid_signers,
                "name": name,
                "lang": "pt-br"
            }
            response = requests.post(endpoint, json=payload, headers=headers)
            return response.json()
        except Exception as e:
            return {'error': str(e)}
