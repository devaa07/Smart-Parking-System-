from flask import Flask, render_template, request

app = Flask(__name__)

available_slots = list(range(1, 11))
selected_slot = None

@app.route('/parking', methods=['GET', 'POST'])
def get_parking_availability():
    global available_slots, selected_slot
    
    if request.method == 'POST':
        
        slot_number = int(request.form.get('slot-number'))
        if slot_number in available_slots:
            
            selected_slot = slot_number
            available_slots.remove(selected_slot)
    
    if not available_slots:
        available_slots = []
        selected_slot = None
    
    return render_template('index.html', available_slots=available_slots, selected_slot=selected_slot)

if __name__ == '__main__':
    app.run(debug=True, port=5005, host='0.0.0.0')
