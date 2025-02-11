function fetchData() {
    fetch("/data")
    .then(response => response.json())
    .then(data => {
        let table = document.getElementById("priceTable");
        table.innerHTML = "<tr><th>Product Name</th><th>Date</th><th>Price</th></tr>"; // Reset table

        data.forEach(row => {
            let newRow = table.insertRow();
            row.forEach(cell => {
                let newCell = newRow.insertCell();
                newCell.textContent = cell;
            });
        });
    });
}

setInterval(fetchData, 5000); // Refresh every 5 seconds
window.onload = fetchData;

const socket = io();  // Connect to WebSocket server

socket.on("update_data", function(data) {
    let table = document.getElementById("priceTable");
    table.innerHTML = "<tr><th>Product Name</th><th>Date</th><th>Price</th></tr>";  // Reset table

    data.forEach(row => {
        let newRow = table.insertRow();
        row.forEach(cell => {
            let newCell = newRow.insertCell();
            newCell.textContent = cell;
        });
    });
});

