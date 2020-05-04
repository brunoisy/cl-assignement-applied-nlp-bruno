from app import app, ideas
from flask import render_template, request, jsonify


@app.route('/')
@app.route('/index')
def index():
    search_str = request.args.get('search')
    ids = ideas.get_ideas(search=search_str)
    return render_template('ideas.html', ideas=ids)


@app.route('/insights')
def insights():
    return render_template('insights.html')


@app.route('/topic_suggestions')
def topic_suggestions():
    idea_id = request.args.get('idea_id')
    entry = request.args.get('entry')
    suggestions = ideas.get_topic_suggestions(idea_id, entry)
    return jsonify(suggestions)


@app.route('/ideas/<idea_id>/topics', methods=['POST'])
def update_topics(idea_id):
    topics = request.json
    ideas.update_topics(idea_id, topics)
    return jsonify(topics)
