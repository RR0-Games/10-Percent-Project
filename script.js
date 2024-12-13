document.getElementById('interest-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const interests = document.getElementById('interests').value;
    
    fetch('/suggest', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ interests: interests }),
    })
    .then(response => response.json())
    .then(data => {
        const suggestionsDiv = document.getElementById('suggestions');
        suggestionsDiv.innerHTML = `<h2>Suggested Job Fields:</h2><ul>${data.suggestions.map(job => `<li>${job}</li>`).join('')}</ul>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
