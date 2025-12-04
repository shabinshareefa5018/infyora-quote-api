async function getQuote() {
    try {
        const response = await fetch("https://quote-api-shabinshareefa5018-dev.apps.rm2.thpm.p1.openshiftapps.com//quote");
        const data = await response.json();
        document.getElementById("quoteText").innerText = data.quote;
    } catch (error) {
        document.getElementById("quoteText").innerText = "Error fetching quote.";
    }
}
