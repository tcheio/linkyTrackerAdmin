document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('loginForm').addEventListener('submit', async (event) => {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        const response = await fetch('http://localhost:4000/connexion', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (!response.ok) {
            throw new Error('Erreur lors de la requête vers le serveur');
        }

        const result = await response.json();
        const messageElement = document.getElementById('message');

        if (result.message === 'Connexion réussie') {
            messageElement.innerText = result.message;
            // Rediriger vers admin.php après une connexion réussie
            window.location.href = 'admin.php';
        } else {
            messageElement.innerText = result.error;
        }
    });
});
