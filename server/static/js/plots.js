//Función de sobrevivencia

function myChart(estado, sector){
    
    var url = "http://127.0.0.1:5000/"+estado+"/"+sector;
    console.log(url);
    
    d3.json(url, function(response) {
      console.log(response);
    
    var trace1 = {
      x: response.map(row => row.Fecha),
      y: response.map(row => row.Cartera),

      //text: data.map(row => row.xxxxxx),
      //name: "xxxxx",
      type: "scatter"
    };
    var data = [trace1];
  
          // Apply the group barmode to the layout
          var layout = {
            title: "Cartera",
            barmode: "group"
          };
          
          // Render the plot to the div tag with id "plot"
          Plotly.newPlot("plot", data, layout);




          var trace2 = {
            x: response.map(row => row.Fecha),
            y: response.map(row => row.Vigente),
      
            //text: data.map(row => row.xxxxxx),
            //name: "xxxxx",
            type: "scatter"
          };
          var data2 = [trace2];
                
                // Apply the group barmode to the layout
          var layout2 = {
              title: "Cartera Vigente",
              barmode: "group"
          };
                
          // Render the plot to the div tag with id "plot"
          Plotly.newPlot("plot2", data2, layout2);





          var trace3 = {
            x: response.map(row => row.Fecha),
            y: response.map(row => row.Vencida),
      
            //text: data.map(row => row.xxxxxx),
            //name: "xxxxx",
            type: "scatter"
          };
          var data3 = [trace3];
                
                // Apply the group barmode to the layout
          var layout3 = {
              title: "Cartera Vencida",
              barmode: "group"
          };
                
          // Render the plot to the div tag with id "plot"
          Plotly.newPlot("plot3", data3, layout3);
        
        
        });

        
          
    }
    
        
       // Trace1 for the Greek Data
   /* 
          
          // Trace1 for the Greek Data
    var trace2 = {
              x: filtered_state_pred.map(row => row.Fecha),
              y: filtered_state_pred.map(row => row.Cartera),
              //text: data.map(row => row.xxxxx),
              //name: "xxxx",
              type: "scatter",
              line: {
                  dash: 'dashdot',
                  width: 4
                }
            };
          
          
          // Combining both traces
          var data = [trace1,trace2];
          
          // Apply the group barmode to the layout
          var layout = {
            title: "Cartera",
            barmode: "group"
          };
          
          // Render the plot to the div tag with id "plot"
          Plotly.newPlot("plot", data, layout)
 */