from flask import request, jsonify
from api import api as blueprint
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


@blueprint.route('/prompt', methods=['POST'])
def prompt():
    data = request.get_json(force=True)
    prompt_text = data.get('prompt')
    if prompt_text:
        response = openai.Completion.create(
            engine="text-davinci-002", prompt=prompt_text, max_tokens=100)
        return jsonify(result=response.choices[0].text.strip())
    else:
        return jsonify(error='No prompt provided'), 400
