from src.service.auth.token import access_token_decoder

def authorization(token):
    data=access_token_decoder(token)
    return data