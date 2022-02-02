from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/API_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accountName = db.Column(db.String(100), unique=True)
    domain = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    address_1 = db.Column(db.String(200))
    address_2 = db.Column(db.String(200))
    state = db.Column(db.String(200))

    def __init__(self, accountName, domain, phone, address_1, address_2, state):
        self.accountName = accountName
        self.domain = domain
        self.phone = phone
        self.address_1 = address_1
        self.address_2 = address_2
        self.state = state

db.create_all()

class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id', 'accountName', 'domain', 'phone', 'address_1', 'address_2', 'state')


Account_schema = AccountSchema()
Accounts_schema = AccountSchema(many=True)

@app.route('/accounts', methods=['Post'])
def create_account():
  accountName = request.json['accountName']
  domain = request.json['domain']
  phone = request.json['phone']
  address_1 = request.json['address_1']
  address_2 = request.json['address_2']
  state = request.json['state']

  new_account= Account(accountName, domain, phone, address_1, address_2, state)

  db.session.add(new_account)
  db.session.commit()

  return Account_schema.jsonify(new_account)

@app.route('/accounts', methods=['GET'])
def get_accounts():
  all_accounts = Account.query.all()
  result = Accounts_schema.dump(all_accounts)
  return jsonify(result)

@app.route('/accounts/<id>', methods=['GET'])
def get_account(id):
  account = Account.query.get(id)
  return Account_schema.jsonify(account)

@app.route('/accounts/<id>', methods=['PUT'])
def update_account(id):
  account = Account.query.get(id)

  accountName = request.json['accountName']
  domain = request.json['domain']
  phone = request.json['phone']
  address_1 = request.json['address_1']
  address_2 = request.json['address_2']
  state = request.json['state']

  account.accountName = accountName
  account.domain = domain
  account.phone = phone
  account.address_1 = address_1
  account.address_2 = address_2
  account.state = state

  db.session.commit()

  return Account_schema.jsonify(account)

@app.route('/accounts/<id>', methods=['DELETE'])
def delete_account(id):
  account = Account.query.get(id)
  db.session.delete(account)
  db.session.commit()
  return Account_schema.jsonify(account)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my API'})



if __name__ == "__main__":
    app.run(debug=True)