document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('http://localhost:4000/conso', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const data = await response.json();
    const tableBody = document.querySelector('#dataTable tbody');

    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.id}</td>
            <td>${item.name}</td>
            <td>${item.value}</td>
        `;
        tableBody.appendChild(row);
    });
});
