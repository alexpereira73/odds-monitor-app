# app.py - VERSÃO TESTE PARA LOVABLE
import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-key')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>⚽ Odds Monitor - TESTE</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                color: white;
                margin: 0;
                padding: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                max-width: 600px;
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
            h1 {
                color: #4cc9f0;
                margin-bottom: 10px;
            }
            .status {
                background: rgba(76, 201, 240, 0.2);
                padding: 10px 20px;
                border-radius: 50px;
                display: inline-block;
                margin: 20px 0;
                font-weight: bold;
            }
            .btn {
                background: #4361ee;
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 10px;
                font-size: 16px;
                cursor: pointer;
                margin: 10px;
                text-decoration: none;
                display: inline-block;
            }
            .btn:hover {
                background: #3a56d4;
                transform: scale(1.05);
            }
            .steps {
                text-align: left;
                margin: 30px 0;
                background: rgba(0, 0, 0, 0.3);
                padding: 20px;
                border-radius: 10px;
            }
            .step {
                margin: 15px 0;
                display: flex;
                align-items: center;
            }
            .step-number {
                background: #4361ee;
                color: white;
                width: 30px;
                height: 30px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-right: 15px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>⚽ Odds Monitor</h1>
            <p>App profissional para monitoramento de odds de futebol</p>
            
            <div class="status">✅ APLICAÇÃO FUNCIONANDO</div>
            
            <div class="steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <div>
                        <strong>Configure suas chaves</strong><br>
                        Odds API + Telegram Bot
                    </div>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <div>
                        <strong>Escolha ligas e bookmakers</strong><br>
                        Premier League + Brasileirão • Bet365 + Betano
                    </div>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <div>
                        <strong>Defina odds alvo</strong><br>
                        Alertas para odds combinadas ≥ 1.70
                    </div>
                </div>
                <div class="step">
                    <div class="step-number">4</div>
                    <div>
                        <strong>Receba alertas automáticos</strong><br>
                        No Telegram em tempo real
                    </div>
                </div>
            </div>
            
            <div>
                <a href="/api/test" class="btn">Testar API</a>
                <a href="/api/settings" class="btn" style="background: #4cc9f0;">Ver Configurações</a>
            </div>
            
            <p style="margin-top: 30px; color: rgba(255, 255, 255, 0.7); font-size: 14px;">
                Pronto para começar? Configure suas chaves no Lovable!
            </p>
        </div>
    </body>
    </html>
    '''

@app.route('/api/test')
def test_api():
    return jsonify({
        "success": True,
        "message": "✅ API funcionando perfeitamente!",
        "status": "operational",
        "next_step": "Configure suas chaves de API no Lovable"
    })

@app.route('/api/settings')
def get_settings():
    return jsonify({
        "app_name": "Odds Monitor",
        "version": "1.0.0",
        "features": [
            "Monitoramento Premier League + Brasileirão",
            "Alertas Telegram em tempo real",
            "Suporte Bet365 e Betano",
            "Odd alvo configurável",
            "Rate limiting automático"
        ],
        "config_required": [
            "ODDS_API_KEY - Obtenha em https://odds-api.io",
            "TELEGRAM_TOKEN - Crie bot com @BotFather",
            "TELEGRAM_CHAT_ID - Use @userinfobot"
        ]
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
