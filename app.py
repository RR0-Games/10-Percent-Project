from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suggest', methods=['POST'])
def suggest_jobs():
    data = request.get_json()
    interests = data.get('interests', '').lower()

    job_fields = {
        'coding': ['Software Engineer', 'Data Scientist', 'Web Developer'],
        'design': ['Graphic Designer', 'UX Designer', 'Product Designer'],
        'science': ['Biologist', 'Chemist', 'Physicist'],
        # Add more interest-job field mappings as needed
    }

    suggestions = []
    for interest in interests.split(','):
        interest = interest.strip()
        suggestions.extend(job_fields.get(interest, ['Unknown Field']))
    
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)
