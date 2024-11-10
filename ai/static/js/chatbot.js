// ai/static/js/chatbot.js

document.getElementById('sendBtn').addEventListener('click', async function() {
    const userMessage = document.getElementById('userMessage').value;
    if (userMessage) {
        const messagesDiv = document.getElementById('messages');
        messagesDiv.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
        const response = await fetch('/ai/chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage }),
        });
        const data = await response.json();
        messagesDiv.innerHTML += `<p><strong>Bot:</strong> ${data.message}</p>`;
    }
});
