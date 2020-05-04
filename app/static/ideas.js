/* 
	This is a small React component that displays the topics, shows an input
	to add new topics and provides autocomplete suggestions through the API.

	It replaces, and gets its initial data, from these kind of DOM nodes:
	<div
		class="react-topic-control"
		data-topics="['Water','Wind']"
		data-idea-id="4">
	</div>
 */

const e = React.createElement;

const TopicInput = ({ideaId, initialTopics}) => {
	const [topics, setTopics] = React.useState(initialTopics);
	const [newTopic, setNewTopic] = React.useState('');
	const [suggestions, setSuggestions] = React.useState([]);

	const onChange = (event) => {
		setNewTopic(event.target.value);

		fetch(`topic_suggestions?idea_id=${ideaId}&entry=${event.target.value}`, {
			method: 'GET'
		})
			.then(response => response.json())
			.then(setSuggestions)
	}

	const onBlur = (event) => {
		event.preventDefault();
		setSuggestions([]);
	}

	const updateTopics = (topics) => {
		fetch(`ideas/${ideaId}/topics`, {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify(topics)
		})
			.then(response => response.json())
			.then(updatedTopics => setTopics(updatedTopics));
	}

	const deleteTopic = (topic) => () => {
		updateTopics(topics.filter(t => t !== topic));
	}

	const onSubmit = (event) => {
		event.preventDefault();
		updateTopics([...topics, newTopic]);
		setSuggestions([]);
		setNewTopic('');
	}

	const onClickSuggestion = (suggestion) => () => {
		updateTopics([...topics, suggestion]);
		setSuggestions([]);
		setNewTopic('');
	}

	return (
		e('div', {className: 'topics'},
			topics.map(topic =>
				e('div', {key: topic, className: 'topic', onClick: deleteTopic(topic)}, topic)
			),
			e('form', {onSubmit, className: 'pure-form'}, 
				e('input', {onChange, onBlur, name: "topic", className: '', value: newTopic, autocomplete: 'off', placeholder: 'Add a topic'}),
				e('ul', {className: 'dropdown'},
					suggestions.map(s =>
						e('li',{key: s, onMouseDown: onClickSuggestion(s)},s)
					)
				)
			)
		)
	);
}

document.addEventListener("DOMContentLoaded", event => {
	Array.from(document.getElementsByClassName('react-topic-control')).forEach((el) => {
		const ideaId = el.getAttribute('data-idea-id');
		let topics = el.getAttribute('data-topics')
		if(topics === "")
			topics = []
		else
			topics = topics.split(',');

		
		ReactDOM.render(
			e(TopicInput, {ideaId, initialTopics: topics}),
			el
		);
	});
});
