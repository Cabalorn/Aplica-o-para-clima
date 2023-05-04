const form = document.querySelector('form');
const previsaoDiv = document.querySelector('#previsao');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const cidade = form.elements['cidade'].value;
    const estado = form.elements['estado'].value;

    fetch(`/previsao?cidade=${cidade}&estado=${estado}`)
        .then(response => response.json())
        .then(data => {
            previsaoDiv.innerHTML = `
                <h2>Previsão do Tempo para ${data['cidade']}, ${data['estado']}</h2>
                <p>Temperatura: ${data['temperatura']}°C</p>
                <p>Condições: ${data['condicoes']}</p>
            `;
            previsaoDiv.style.display = 'block';
        });
});
