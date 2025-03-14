import requests

# Configurações do seu aplicativo Mercado Livre
CLIENT_ID = "4207752727981094"
CLIENT_SECRET = "xkNwFueMaMk2ji7tbm57ndUqfLdXCQkm"
REDIRECT_URI = "https://google.com"

AUTH_URL = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"

# Imprimir o link para o navegador
print(f"Acesse o seguinte link para autorizar a aplicação: {AUTH_URL}")

#colar o codigo que vai estar como paramtro na URL
auth_code = input("Cole aqui o código de autorização: ")

# gerar token de acesso
TOKEN_URL = "https://api.mercadolibre.com/oauth/token"
payload = {
    "grant_type": "authorization_code",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "code": auth_code,
    "redirect_uri": REDIRECT_URI
}

response = requests.post(TOKEN_URL, data=payload)
if response.status_code == 200:
    token_data = response.json()
    print("Access Token:", token_data["access_token"])
    print("Token expira em:", token_data["expires_in"], "segundos")
else:
    print("Erro ao obter token:", response.text)