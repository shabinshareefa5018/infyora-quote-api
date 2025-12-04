async function getQuote() {
    try {
        const response = await fetch("https://infyora-quote-api-azeemroshan111-dev.apps.rm1.0a51.p1.openshiftapps.com//quote");
        const data = await response.json();
        document.getElementById("quoteText").innerText = data.quote;
    } catch (error) {
        document.getElementById("quoteText").innerText = "Error fetching quote.";
    }
}
