from flask import Flask, request, jsonify, render_template
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Initialize Flask app
app = Flask(__name__)

# Load the fine-tuned T5 model and tokenizer
model_name = "./trained_t5_model"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Function to generate insights
def generate_insights(input_text):
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    output_ids = model.generate(inputs["input_ids"], max_length=150, num_beams=4, early_stopping=True)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

@app.route('/generate', methods=['POST'])
def generate():
    print("Received Content-Type:", request.content_type)
    
    if request.content_type == 'application/x-www-form-urlencoded':
        input_data = request.form.get("input_text")
    elif request.content_type == 'application/json':
        input_data = request.json.get("input_text")
    else:
        return jsonify({"error": "Unsupported Media Type. Please send data as application/json or use a form submission."}), 415

    if not input_data:
        return jsonify({"error": "No input_text provided"}), 400

    generated_text = generate_insights(input_data)
    return jsonify({"generated_text": generated_text})

@app.route('/')
def index():
    return render_template('index.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
