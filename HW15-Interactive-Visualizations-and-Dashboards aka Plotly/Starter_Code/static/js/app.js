

////////////////////////////////////////////////////////
//Use the D3 library to read in samples.json.
const samples = "samples.json";
//populate dropdown
let dropdown = document.getElementById('selDataset');
dropdown.length = 0;

let defaultOption = document.createElement('option');
defaultOption.text = 'Choose ID';

dropdown.add(defaultOption);
dropdown.selectedIndex = 0;

// Fetch the JSON data and console log it
function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  d3.json(samples).then(function(data) {

  var sampleNames = data.names;

  sampleNames.forEach((sample) => {
    selector
      .append("option")
      .text(sample)
      .property("value", sample);
  });
  var metadata = data.metadata;
    // Filter the data for the object with the desired sample number
    var resultArray = metadata//.filter(sampleObj => sampleObj.id == sample);
    var result = resultArray[0];
    // Use d3 to select the panel with id of `#sample-metadata`
    var PANEL = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    PANEL.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(result).forEach(([key, value]) => {
      PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
    });
  //add IDs to dropdown
  data.names.forEach(element => {
    option       = document.createElement('option');
    option.text  = element;
    option.value = element;
    dropdown.add(option);  });
  
    //get biosample data  
    data.samples.forEach(element => {
      //define variables
      var xvals = [];
      var ids   = [];
      var labels = [];
      var idNoText = [];
      
      //push each sample value into list
      element.sample_values.forEach(item => {
        xvals.push(item)
      });
      //slice to get top 10
      var topTen = xvals.slice(0,10);
      //console.log(topTen);
      //push each otu id into list
      element.otu_ids.forEach(item => {
        ids.push("OTU " + item);
        idNoText.push(item);
      });
      //slice to get top ten
      var topTenIDs = ids.slice(0,10);
      //console.log(topTenIDs);
      //push each otu label into list
      element.otu_labels.forEach(item => {
        labels.push(item)
      });
      //slice to get top ten
      var topTenLabels = labels.slice(0,10);
      //console.log(topTenlabels);  

    //build bar chart
    var data = [
      {
        x: topTen,
        y: topTenIDs,
        text: topTenLabels,
        orientation: "h",
        type: 'bar'
      }
    ];
    var layout = {
      "yaxis": {
        "autorange": 'reversed'
      }
    };
    Plotly.newPlot('bar', data, layout);
    //build bubble chart
    var bubbleData = [
      {
        x: idNoText,
        y: xvals,
        mode: "markers",
        marker: {
          size: xvals,
          color: idNoText,
          text: labels
        }
      }
    ];
    Plotly.newPlot('bubble', bubbleData);
    });
 
  ;

  });
};
function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();