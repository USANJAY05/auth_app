from src.utils.token import refresh_token_decoder,refresh_token_gen,access_token_gen

def refresh(token):
    res=refresh_token_decoder(token)
    if res:
        response=access_token_gen(res.get('id'))
        return response
    return 'res'