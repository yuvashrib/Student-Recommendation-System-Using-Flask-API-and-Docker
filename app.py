from flask import Flask, request, jsonify
import json
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API. Use the /upload-student-data endpoint to upload and process your data."})

@app.route('/favicon.ico')
def favicon():
    return '', 204 

def flatten_json(nested_json, parent_key='', sep='_'):
    """Flatten JSON object with nested keys into a single level."""
    items = {}
    for k, v in nested_json.items():
        new_key = f"{parent_key}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key + sep, sep))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.update(flatten_json(item, f"{new_key}{sep}{i}", sep))
        else:
            items[new_key] = v
    return items

def normalize_questions(quiz_data):
    """Extract and flatten the questions part from quiz data."""
    questions = quiz_data.get('quiz', {}).get('questions', [])
    normalized_questions = []
    for question in questions:
        flattened_question = flatten_json(question)
        normalized_questions.append(flattened_question)
    return pd.DataFrame(normalized_questions)

def read_json_file(file):
    """Reads a JSON file and returns the data."""
    return json.load(file)


@app.route('/upload-student-data', methods=['POST'])
def upload_student_data():
    """Handle student data upload and processing."""
    if 'student_data' not in request.files:
        return jsonify({"error": "No student data file part"}), 400
    
    student_file = request.files['student_data']
    try:
        student_data = read_json_file(student_file)
    except Exception as e:
        return jsonify({"error": f"Failed to read student data file: {str(e)}"}), 400
 
    quiz_data_json_file_path = 'C:/Users/yuvas/Desktop/My Activities/Small Project/Quiz Data.json'
    
    try:
        with open(quiz_data_json_file_path, 'r') as quiz_file:
            quiz_data = read_json_file(quiz_file)
    except Exception as e:
        return jsonify({"error": f"Failed to read quiz data file: {str(e)}"}), 400


    # Flatten data
    flat_student_data = flatten_json(student_data)
    questions_df = normalize_questions(quiz_data)
    student_df = pd.DataFrame([flat_student_data])
    response_mapping_results = []

    for response_column in student_df.columns:
        if "response_map" in response_column:
            response_value = student_df.iloc[0][response_column]
            question_id = int(response_column.split('_')[-1]) 
    
            question_data = questions_df[questions_df['id'] == question_id]
    
            if not question_data.empty:
                question_description = question_data['description'].values[0]
    
                options = [
                    {
                        "option_id": question_data[f"options_{i}id"].values[0],
                        "option_description": question_data[f"options_{i}description"].values[0],
                        "is_correct": question_data[f"options_{i}is_correct"].values[0],
                    }
                    for i in range(4) 
                ]
    
                selected_option = next((o for o in options if o["option_id"] == response_value), None)
                correct_option = selected_option["is_correct"] if selected_option else False
    
                result = {
                    "response_map": response_column,
                    "question_id": question_id,
                    "question_description": question_description,
                    #"selected_option_id": response_value,
                    "selected_option_description": selected_option["option_description"] if selected_option else None,
                    "answered_correctly": "Yes" if correct_option else "No",
                }
    
                # Add options to the result
                for i, option in enumerate(options):
                    #result[f"option_{i}_id"] = option["option_id"]
                    result[f"option_{i}_description"] = option["option_description"]
                    #result[f"option_{i}_is_correct"] = option["is_correct"]
    
                response_mapping_results.append(result)

    response_results_df = pd.DataFrame(response_mapping_results)
    incorrect_answers_df = response_results_df[response_results_df["answered_correctly"] == "No"]

    if not incorrect_answers_df.empty:
        
        results = {"questions_to_revise": []}
        for _, row in incorrect_answers_df.iterrows():
            results["questions_to_revise"].append({
                "question_id": row['question_id'],
                "question_description": row['question_description']
            })
        response_results_dict = response_results_df.to_dict(orient='records')
        results["response_results"] = response_results_dict
        return jsonify(results)

    return jsonify({"message": "Great job! All questions answered correctly."})

if __name__ == '__main__':
    app.run(debug=True)
