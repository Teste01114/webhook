from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Dados enviados pelo PushinPay
        data = request.json

        if data and "event" in data:
            if data["event"] == "payment.paid":
                payment_id = data["data"]["id"]
                # Aqui você pode verificar o ID do pagamento e executar ações
                print(f"Pagamento confirmado: {payment_id}")
                # Adicione o usuário ao grupo ou atualize o status no banco de dados

        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print(f"Erro no webhook: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
#FG