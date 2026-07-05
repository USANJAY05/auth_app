from src.utils.token import access_token_decoder

def authorization(token):
    response=access_token_decoder(token)
    return response