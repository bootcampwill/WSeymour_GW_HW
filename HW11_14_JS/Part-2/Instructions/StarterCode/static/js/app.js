// from data.js
var tableData = data;

// YOUR CODE HERE!

// Use D3 to select the table body
var tbody = d3.select("tbody");
// Use D3 to select the table
var table = d3.select("table");
// Use D3 to set the table class to `table table-striped`
table.attr("class", "table table-striped");
// Loop through an array of grades and build the entire table body from scratch

data.forEach((data) => {
    var row = tbody.append("tr");
    Object.entries(data).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });

  //listen for filter button click and update table
  // Grab reference to the button element
var button = d3.select("#filter-btn");

// Define button click
button.on("click", function() {

  d3.event.preventDefault();  
  tbody.selectAll('*').remove();
  
  //define input variables
  var inputDate = d3.select("#datetime");
  var inputText = inputDate.property("value")
  //commenting out my attemp at setting multiple filters
  // var inputCity = d3.select("#city");
  // var inputTextCity = inputCity.property("value")
  // var inputState = d3.select("#state");
  // var inputTextState = inputState.property("value")
  // var inputCountry = d3.select("#country");
  // var inputTextCountry = inputCountry.property("value")
  // var inputShape = d3.select("#shape");
  // var inputTextShape = inputShape.property("value")

  var filteredData = tableData.filter(x => x.datetime === inputText //i wanted to filter on multiple criteria but couldn't get it to work. might come back to this&  
                                          // x.city     === inputTextCity //&
                                          //  x.state    === inputTextState &
                                          //  x.country  === inputTextCountry &
                                           //x.shape    === inputTextShape
                                           );
  filteredData.forEach(function(data) {
    var row = tbody.append("tr");
    Object.entries(data).forEach(function([key, value]) {
        var cell = tbody.append("td");
        cell.text(value)
        
    })
    
  })
  
})
// Define button click -- city
var cityButton = d3.select("#city-filter-btn");

cityButton.on("click", function() {

  d3.event.preventDefault();  
  tbody.selectAll('*').remove();
  var inputCity = d3.select("#city");
  var inputTextCity = inputCity.property("value")
  var filteredData = tableData.filter(x => x.city === inputTextCity);
  filteredData.forEach(function(data) {
    var row = tbody.append("tr");
    Object.entries(data).forEach(function([key, value]) {
        var cell = tbody.append("td");
        cell.text(value)
        
    })
    
  })
  
})
// Define button click -- state
var stateButton = d3.select("#state-filter-btn");
stateButton.on("click", function() {

  d3.event.preventDefault();  
  tbody.selectAll('*').remove();
  var inputDate = d3.select("#state");
  var inputText = inputDate.property("value")
  var filteredData = tableData.filter(x => x.state === inputText);
  filteredData.forEach(function(data) {
    var row = tbody.append("tr");
    Object.entries(data).forEach(function([key, value]) {
        var cell = tbody.append("td");
        cell.text(value)
        
    })
    
  })
  
})
// Define button click -- country
var countryButton = d3.select("#country-filter-btn");
countryButton.on("click", function() {

  d3.event.preventDefault();  
  tbody.selectAll('*').remove();
  var inputDate = d3.select("#country");
  var inputText = inputDate.property("value")
  var filteredData = tableData.filter(x => x.country === inputText);
  filteredData.forEach(function(data) {
    var row = tbody.append("tr");
    Object.entries(data).forEach(function([key, value]) {
        var cell = tbody.append("td");
        cell.text(value)
        
    })
    
  })
  
})
// Define button click -- shape
var shapeButton = d3.select("#shape-filter-btn");
shapeButton.on("click", function() {


  d3.event.preventDefault();  
  tbody.selectAll('*').remove();
  var inputDate = d3.select("#shape");
  var inputText = inputDate.property("value")
  var filteredData = tableData.filter(x => x.shape === inputText);
  filteredData.forEach(function(data) {
    var row = tbody.append("tr");
    Object.entries(data).forEach(function([key, value]) {
        var cell = tbody.append("td");
        cell.text(value)
        
    })
    
  })
  
})