document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    // Exibe a mensagem de carregamento
    document.getElementById('loading-message').style.display = 'block';

    // Coleta os dados do formulário
    const formData = new FormData(this);
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        message: formData.get('message'),
        city: formData.get('city'),
        services: formData.getAll('services') // Coleta todos os checkboxes selecionados
    };

    fetch('/send', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response-message').innerText = data.status;
        document.getElementById('contact-form').reset();

        // Redireciona para a página de agradecimento
        window.location.href = '/thank_you';
    })
    .catch(error => {
        document.getElementById('response-message').innerText = 'Ocorreu um erro. Por favor, tente novamente.';
        console.error('Error:', error);
    })
    .finally(() => {
        // Oculta a mensagem de carregamento
        document.getElementById('loading-message').style.display = 'none';
    });
});
