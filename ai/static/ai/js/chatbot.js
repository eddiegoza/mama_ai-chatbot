// ai/static/js/chatbot.js

document.getElementById('sendBtn').addEventListener('click', async function () {
    const userMessageInput = document.getElementById('userMessage');
    const userMessage = userMessageInput.value.trim();
    
    if (userMessage) {
        // Clear the input field and add user message to the chat area
        const messagesDiv = document.getElementById('messages');
        userMessageInput.value = '';
        
        addMessageToChat('You', userMessage, 'user');

        try {
            // Send user message to the server
            const response = await fetch('/ai/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessage }),
            });

            if (response.ok) {
                const data = await response.json();
                addMessageToChat('Bot', data.message, 'bot');
            } else {
                addMessageToChat('Bot', 'Sorry, something went wrong. Please try again later.', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            addMessageToChat('Bot', 'Unable to connect to the server. Please check your connection.', 'error');
        }

        // Scroll to the bottom of the chat
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
});

// Function to append messages to the chat area
function addMessageToChat(sender, message, messageType) {
    const messagesDiv = document.getElementById('messages');
    const messageBubble = document.createElement('div');
    messageBubble.classList.add('chat-bubble', messageType);
    messageBubble.innerHTML = `<strong>${sender}:</strong> ${message}`;
    messagesDiv.appendChild(messageBubble);
}
