from src.utils.token import refresh_token_decoder

def authorization(token):
    response=refresh_token_decoder(token)
    return response