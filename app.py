from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize the list of available slots and selected slot to None
available_slots = list(range(1, 5))
selected_slot = None

# Define a route to handle requests for the availability of parking slots
@app.route('/parking', methods=['GET', 'POST'])
def get_parking_availability():
    global available_slots, selected_slot
    
    if request.method == 'POST':
        # Check if the entered slot number is available
        slot_number = int(request.form.get('slot-number'))
        if slot_number in available_slots:
            # Park the car in the selected slot
            selected_slot = slot_number
            # Remove the selected slot from the list of available slots
            available_slots.remove(selected_slot)
        else:
            # Inform the user that the selected slot is not available
            return '<h1>Slot not available</h1>'
    
    # If all slots are filled, inform the user that no slots are available
    if not available_slots:
        return '<h1>No slots available at the moment..</h1>'
    
    # Return the template with the available slots and selected slot
    return render_template('index.html', available_slots=available_slots, selected_slot=selected_slot)

# Define a main function to start the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5005)
