import os
from flask import Flask, render_template, request

app = Flask(__name__)

QUIZ_DATA = [
    {
        "id": 1,
        "question": "Python ka invension kisne kiya tha?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
        "correct": "Guido van Rossum"
    },
    {
        "id": 2,
        "question": "Inme se kaun sa Python ka framework web development ke liye use hota hai?",
        "options": ["Pandas", "NumPy", "Django", "Scikit-Learn"],
        "correct": "Django"
    },
    {
        "id": 3,
        "question": "Python file ka extension kya hota hai?",
        "options": [".py", ".python", ".pt", ".pyt"],
        "correct": ".py"
    },
    {
        "id": 4,
        "question": "Python mein 'self' keyword kya represent karta hai?",
        "options": ["Class ke instance", "Class ke method", "Class ke variable", "Class ke constructor"],
        "correct": "Class ke instance"
    },
    {
        "id": 5,
        "question": "Python mein 'len()' function kya return karta hai?",
        "options": ["String", "Integer", "Float", "Boolean"],
        "correct": "Integer"
    },
    {
        "id": 6,
        "question": "Python mein 'print()' function kya karta hai?",
        "options": ["Output ko console par dikhata hai", "Input leta hai", "Variable ko define karta hai", "Function ko call karta hai"],
        "correct": "Output ko console par dikhata hai"
    },
    {
        "id": 7,
        "question": "Python mein 'if' statement kya use hota hai?",
        "options": ["Loop ke liye", "Condition ke liye", "Function ke liye", "Variable ke liye"],
        "correct": "Condition ke liye"
    },
    {
        "id": 8,
        "question": "Python mein 'for' loop ka use kya hai?",
        "options": ["Condition check karne ke liye", "List ke elements par iterate karne ke liye", "Function call karne ke liye", "Variable define karne ke liye"],
        "correct": "List ke elements par iterate karne ke liye"
    },
    {
        "id": 9,
        "question": "Python mein 'import' statement ka use kya hai?",
        "options": ["Module ko load karne ke liye", "Variable ko define karne ke liye", "Function ko call karne ke liye", "Class ko create karne ke liye"],
        "correct": "Module ko load karne ke liye"
    },
    {
        "id": 10,
        "question": "Python mein 'list' aur 'tuple' mein kya difference hai?",
        "options": ["List mutable hoti hai, tuple immutable hoti hai", "List immutable hoti hai, tuple mutable hoti hai", "Dono same hain", "List aur tuple dono mutable hain"],
        "correct": "List mutable hoti hai, tuple immutable hoti hai"
    },
    {
        "id": 11,
        "question": "Python mein 'dict' kya hai?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "correct": "Dictionary"
    },
    {
        "id": 12,
        "question": "Python mein 'set' kya hai?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "correct": "Set"
    },
    {
        "id": 13,
        "question": "Python mein 'str' kya hai?",
        "options": ["List", "Tuple", "Dictionary", "String"],
        "correct": "String"
    },
    {
        "id": 14,
        "question": "Python mein 'int' kya hai?",
        "options": ["List", "Tuple", "Integer", "String"],
        "correct": "Integer"
    },
    {
        "id": 15,
        "question": "Python mein 'float' kya hai?",
        "options": ["List", "Tuple", "Float", "String"],
        "correct": "Float"
    }
]

@app.route('/')
def home():
    return render_template('quiz.html', questions=QUIZ_DATA)

@app.route('/submit', methods=['POST'])
def submit_quiz():
    score = 0
    for item in QUIZ_DATA:
        field_name = f"question-{item['id']}"
        if request.form.get(field_name) == item['correct']:
            score += 1
            
    return render_template('result.html', score=score, total=len(QUIZ_DATA))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)