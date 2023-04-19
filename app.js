function processDescription() {
    var productDescription = document.getElementById("product-description").value;
    var pattern = /\b([A-Z][a-z]+(?: [A-Z][a-z]+)*)\b/g;
    var matches = productDescription.match(pattern);
    var results = matches.join(", ");
    document.getElementById("results").innerHTML = "Results: " + results;
  }

  