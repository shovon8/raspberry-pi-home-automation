from flask import Flask, jsonify, url_for, render_template
from gpiozero import LED
from uuid import uuid4

rooms = {}

rooms['Room 1'] = [{
  'id': uuid4(), 
  'name': 'Light 1',
  'icon': 'fa fa-lightbulb',
  'status': False,
  'relayPin': 4,
  'relayInstance': False
  }, {
  'id': uuid4(), 
  'name': 'Fan 1',
  'icon': 'fa fa-fan',
  'status': False,
  'relayPin': 6,
  'relayInstance': False
}]
rooms['Bathroom 1'] = [{
  'id': uuid4(), 
  'name': 'Light 1',
  'icon': 'fa fa-lightbulb',
  'status': False,
  'relayPin': 5,
  'relayInstance': False
}]

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
  return render_template('./index.html', rooms=rooms)


def toggle_appliance_status(id):
  for room in rooms:
    for appliance in rooms[room]:
      if str(appliance['id']) == id:
        if appliance['relayInstance']:
          appliance['relayInstance'].close()
          appliance['relayInstance'] = False
        else:
          appliance['relayInstance'] = LED(appliance['relayPin'])
          appliance['relayInstance'].on()

        appliance['status'] = not appliance['status']
        return True
  return False


@app.route('/appliance/toggle/<id>')
def appliance_toggle(id):
  return jsonify({'status': toggle_appliance_status(id)})

