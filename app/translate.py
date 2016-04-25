try:
    import httplib
except ImportError:
    import http.client as httplib
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
import json
from config import MS_TRANSLATOR_CLIENT_ID, MS_TRANSLATOR_CLIENT_SECRET

def microsoft_translate(text, sourceLang, destLang):
    if MS_TRANSLATOR_CLIENT_ID == '' or MS_TRANSLATOR_CLIENT_SECRET == '':
        return 'Error: translation service not configured.'

    try:
        #get access token
        params = urlencode({
            'client_id': MS_TRANSLATOR_CLIENT_ID,
            'client_secret': MS_TRANSLATOR_CLIENT_SECRET,
            'scope': 'http://api.microsofttranslator.com', 
            'grant_type': 'client_credentials'
            })
        conn = httplib.HTTPSConnection("datamarket.accesscontrol.windows.net")
        conn.request("POST", "/v2/OAuth2-13",params)
        res = conn.getresponse().read()
        response = json.loads(res)
        token = response[u'access_token']
        
        #translate
        conn = httplib.HTTPConnection('api.microsofttranslator.com')
        params = {'appId':'Bearer '+token,
                    'from':sourceLang,
                    'to':destLang,
                    'text':text.encode("utf-8")}
        conn.request("GET", '/V2/Ajax.svc/Translate?' + urlencode(params))
        resd = conn.getresponse().read().decode('utf-8-sig')
        response = json.loads("{\"response\":" + resd + "}")
        return response["response"]
    except:
        return 'Error: Unexpected error.'



def  main():
    print microsoft_translate('Hi, how are you today?', 'en', 'zh') 
if __name__ == '__main__':
    main()