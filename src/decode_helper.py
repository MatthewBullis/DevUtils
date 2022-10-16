import base64
import os
import requests
import json
import datetime
import binascii
import jwt
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from tomlkit import key
from Scripts.src.util.Aura_Environment import get_request_values_by_env, Aura_Admin_Bearer_Token # https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c
from collections.abc import Iterable, Mapping
from Scripts.src.util.json_helper import json_helpers as json_helper

# from jose import jwk
# from jose.backends.base import Key
# from jose.constants import ALGORITHMS
# from jose.exceptions import JWSError, JWSSignatureError
# from jose.utils import base64url_decode, base64url_encode
# from jose.jws import get_unverified_claims, get_unverified_header, get_unverified_headers
# from jose.jwt import d

class jwt_tokens:
    token = None

    def get_test_token():
        domain = 'https://api.aurasvc.io'
        endpoint = '/auth/admin/get_user'

        check_env = get_request_values_by_env.Check_Env('Prod',domain)
        url = f"{check_env[0]}{endpoint}"

        # Get Bearer
        print("Getting Bearer Token...")
        Get_Token = Aura_Admin_Bearer_Token.Bearer_Token_Helper()
        
        auth_response = requests.request("POST", Get_Token[0], headers=Get_Token[1], data=Get_Token[2])
        
        return auth_response.text

    def validate_access_token(token):
        if len((token).split('.')) == 3:
            json_access_token = token
        elif len((token).split('.')) != 3 and type(token) is str and 'refresh_token' in token:
            json_token = json.loads(token)
            json_access_token = json_token['session']['access_token']
            del json_token
        return json_access_token

    def decode_access_token(access_token):
        # Validate structure/format of token passed
        token = jwt_tokens.validate_access_token(token=access_token)

        # Decode header and payload
        jwt_header = jwt.get_unverified_header(token) # same as get_unverified_headers(access_token)
        jwt_payload = jwt.decode(token, key=None, options={"verify_signature":False}) # does the same as 'get_unverified_claims(access_token)', however, in the latter, 

        # return header and payload
        return jwt_header, jwt_payload
    
    def log_decoded_jwt_to_console(JWT, printJson=''):
        v_decoded_jwt = JWT
        # debug
            # v_decoded_jwt = decoded_jwt
            # print_json = 'True'
        print("##############################################\n")
        print(f"Found JWT Headers:\n{v_decoded_jwt[0]}\n")
        print(f"JWT Initialized at: {datetime.datetime.fromtimestamp(v_decoded_jwt[1]['iat'])}")
        print(f"JWT Token expires at: {datetime.datetime.fromtimestamp(v_decoded_jwt[1]['exp'])}")
        print(f"Token expires in: {((datetime.datetime.fromtimestamp(v_decoded_jwt[1]['exp'])) - datetime.datetime.fromtimestamp(v_decoded_jwt[1]['iat']))} minutes")
        print(f"JWT NBF: {datetime.datetime.fromtimestamp(v_decoded_jwt[1]['nbf'])}...not sure importance of this")
        print("\n##############################################\nJWT Payload:")
        if printJson.casefold() == 'True'.casefold():
            
            json_helper.convert_to_json(v_json=v_decoded_jwt[1], format='True', skip_logging='True', print_json='True')
        if printJson.casefold() != 'True'.casefold():
            
            print(f"{v_decoded_jwt[1]}\n") 
        print("##############################################\n")

# jwt_tokens.log_decoded_jwt_to_console(JWT=decoded_jwt, printJson='true')    
# jwt_tokens.decode_access_token(jwt_tokens.get_test_token())
# https://jwt.io/    
# jwt.decode(access_token, key=key, algorithms=["RS256"])

# jwt_header, jwt_payload, jwt_signature = access_token.split('.') # additional tests, splits the jwt into their three respective parts, header, payload, and signature.
                                                                 # signature is an encrypted string of base64url encoded header + : + payload, salt
                                                                 # not able to capture salt in this stepto further decode
                                                                 # not finding jwt or bearer in cookies

# decode_token = access_token.split('.')
# for i in decode_token:
#     print(i)


# import jwt
# from jwt import PyJWKClient
# access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5FRTFRVVJCT1RNNE16STVSa0ZETlRZeE9UVTFNRGcyT0Rnd1EwVXpNVGsxUWpZeVJrUkZRdyJ9.eyJpc3MiOiJodHRwczovL2Rldi04N2V2eDlydS5hdXRoMC5jb20vIiwic3ViIjoiYVc0Q2NhNzl4UmVMV1V6MGFFMkg2a0QwTzNjWEJWdENAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZXhwZW5zZXMtYXBpIiwiaWF0IjoxNTcyMDA2OTU0LCJleHAiOjE1NzIwMDY5NjQsImF6cCI6ImFXNENjYTc5eFJlTFdVejBhRTJINmtEME8zY1hCVnRDIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.PUxE7xn52aTCohGiWoSdMBZGiYAHwE5FYie0Y1qUT68IHSTXwXVd6hn02HTah6epvHHVKA2FqcFZ4GGv5VTHEvYpeggiiZMgbxFrmTEY0csL6VNkX1eaJGcuehwQCRBKRLL3zKmA5IKGy5GeUnIbpPHLHDxr-GXvgFzsdsyWlVQvPX2xjeaQ217r2PtxDeqjlf66UYl6oY6AqNS8DH3iryCvIfCcybRZkc_hdy-6ZMoKT6Piijvk_aXdm7-QQqKJFHLuEqrVSOuBqqiNfVrG27QzAPuPOxvfXTVLXL2jek5meH6n-VWgrBdoMFH93QEszEDowDAEhQPHVs0xj7SIzA"
# kid = "default"
# url = "https://dev-87evx9ru.auth0.com/.well-known/jwks.json"
# jwks_client = PyJWKClient(url)
# signing_key = jwks_client.get_signing_key_from_jwt(access_token)
# data = jwt.decode(
#     token,
#     signing_key.key,
#     algorithms=["RS256"],
#     audience="https://expenses-api",
#     options={"verify_exp": False},
# )
# print(data)

