// 21UM9PWFH3S7AYD3
// jen 25 requstu za den

function portfolio(){
    fetch('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&apikey=21UM9PWFH3S7AYD3')
    .then(response => response.json())
    .then(data => {
        // Extract the stock price from the API response
        // const stockPrice = data['Global Quote']['05. price'];

        // Display the stock price
        document.getElementById('price').innerHTML = data;
        console.log('Microsoft Stock Price:', data);
    })
    .catch(error => {
        console.log('Error fetching stock price:', error);
    });
}
// window.setInterval(portfolio, 10000);