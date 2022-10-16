import re # regex
import requests
import json
from Scripts.src.util.api_get_creds import Get_Creds # https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c

class get_request_values_by_env:
    # properties
    Env = None
    api_url = None

    def Check_Env(Env, E_url):
        if Env.casefold() == "Test".casefold():
            if "identityguard" in E_url:
                if "api.identityguard" in E_url:
                    index = E_url.find('api.identityguard')
                    api_url = E_url[:index] + 'test.' + E_url[index:]
                    creds = (Get_Creds()).idg_test_api_key

                if "app.identityguard" in E_url:
                    index = E_url.find('app.identityguard')
                    api_url = E_url[:index] + 'test.' + E_url[index:] 
                    creds = (Get_Creds()).idg_test_app_api_key

            if "aurasvc" in E_url:
                index = E_url.find('aurasvc.io')
                api_url = E_url[:index] + 'test.' + E_url[index:]
                creds = {}
                creds['without_bearer_token'] = (Get_Creds()).idg_test_api_key
                creds['with_bearer_token'] = (Get_Creds()).suite_test_basic_auth

        elif Env.casefold() == "Prod".casefold():
            if "identityguard" in E_url:
                if "api.identityguard" in E_url:
                    creds   = (Get_Creds()).idg_prod_api_key
                    api_url = E_url
                if "app.identityguard" in E_url:
                    creds   = (Get_Creds()).idg_prod_app_api_key
                    api_url = E_url
            if "aurasvc" in E_url:
                api_url = E_url
                creds   = {}
                creds['without_bearer_token'] = (Get_Creds()).idg_prod_api_key
                creds['with_bearer_token'] = (Get_Creds()).suite_test_basic_auth

        return api_url, creds  

class Aura_Admin_Bearer_Token:
    # Properties
    auth_url     = None
    auth_headers = None
    auth_payload = None

    def Bearer_Token_Helper():
        auth_url = "https://api.aurasvc.io/auth/attempt/signin"
        auth_payload = json.dumps({
        "auth_provider": "ALIAS_PASSWORD",
        "payload": {
            "alias": (Get_Creds()).suite_admin_userName,
            "password": (Get_Creds()).suite_admin_pass
        }
        })
        auth_headers = {
        'Authorization': (Get_Creds()).suite_basic_auth,
        'Content-Type': 'application/json'
        }
        
        return auth_url, auth_headers, auth_payload