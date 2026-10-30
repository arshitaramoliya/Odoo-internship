from flask import Flask, jsonify
from model import Partner

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello"

@app.route("/partners")
def get_partners():
    partners = Partner.search()

    data = []

    for partner in partners:
        data.append({
            "id": partner.id,
            "name": partner.name,
            "email": partner.email,
            "city": partner.city,
            "credit_limit": float(partner.credit_limit)
                if partner.credit_limit is not None else None,
        })

    return jsonify(data)


@app.route("/partners/<int:partner_id>")
def get_partner(partner_id):
    partner = Partner.browse(partner_id)

    if partner is None:
        return jsonify({"error": "Partner not found"}), 404

    return jsonify({
        "id": partner.id,
        "name": partner.name,
        "email": partner.email,
        "city": partner.city,
        "credit_limit": (
            float(partner.credit_limit)
            if partner.credit_limit is not None
            else None
        ),
    })


@app.route("/orders/<int:partner_id>")
def get_orders(partner_id):
    partner = Partner.browse(partner_id)

    if partner is None:
        return jsonify({"error": "Partner not found"}), 404

    data = []

    for order in partner.orders():
        data.append({
            "id": order.id,
            "reference": order.reference,
            "order_date": order.order_date.isoformat(),
            "partner_id": order.partner_id,
            "total": float(order.total()),
        })

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)








