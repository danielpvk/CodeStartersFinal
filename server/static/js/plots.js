//Función de sobrevivencia

function myChart(estado, sector){
    
    var url = "http://127.0.0.1:5000/"+estado+"/"+sector;
    console.log(url);
    
    d3.json(url, function(response) {
      console.log(response);

    //Predicted data
    var filtered_sector_pred = cartera_data_predicted.filter(function(item){
        return item.Sector==sector;
      });
    var filtered_state_pred = filtered_sector_pred.filter(function(item){
        return item.Estado==estado;
    });
    var filtered_date_pred = filtered_state_pred.filter(function(item){
      return item.Fecha=="2019-07";
    });
    console.log(filtered_date_pred.map(row => row.Cartera_vigente))
    console.log(filtered_date_pred.map(row => row.Pago))
    var filtered_date_historic = response.filter(function(item){
      return item.Fecha=="2019-06";
    });
    console.log(filtered_date_historic.map(row => row.Cartera))
    // Trace1 for the Greek Data
    var tracepred = {
      x: filtered_date_pred.map(row => row.Fecha),
      y: filtered_date_pred.map(row => row.Cartera_vigente),
      //text: data.map(row => row.xxxxx),
      name: "Forecast",
      type: "scatter",
      line: {
          dash: 'dashdot',
          width: 4
        }
    };
    
    var trace1 = {
      x: response.map(row => row.Fecha),
      y: response.map(row => row.Cartera),

      //text: data.map(row => row.xxxxxx),
      name: "Historico",
      type: "scatter"
    };
    var data = [trace1,tracepred];
  
          // Apply the group barmode to the layout
          var layout = {
            title: "Cartera",
            barmode: "group"
          };
          
          // Render the plot to the div tag with id "plot"
          Plotly.newPlot("plot", data, layout);

          document.getElementById("carteranumerototal_pred").innerHTML = filtered_date_pred.map(row => row.Cartera_vigente);
          document.getElementById("carteranumerototal_pred_text").innerHTML = "asciende a "+filtered_date_pred.map(row => row.Cartera_vigente);
          document.getElementById("carteranumerototal_pred_pago").innerHTML = "Probabilidad de Pago "+filtered_date_pred.map(row => row.Pago);
          document.getElementById("carteranumerototal_pred_impago").innerHTML = "Probabilidad de Impago "+filtered_date_pred.map(row => row.Impago);
          var cart=filtered_date_historic.map(row => row.Cartera);
          var cartvig=filtered_date_historic.map(row => row.Vigente);
          var cartven=filtered_date_historic.map(row => row.Vencida);
          document.getElementById("carteratotalanimadatexto").innerHTML=cart;
          var c = document.getElementById("carteratotalanimada");  
          if (c.hasAttribute("style")) {       
            c.setAttribute("style", "width: 100%");
          }


          vigstr="width: "+filtered_date_pred.map(row => row.Pago)+"%"
          var v = document.getElementById("carteravigenteanimada");  
          if (v.hasAttribute("style")) {       
            v.setAttribute("style", vigstr);
          }
          
          document.getElementById("carteravigenteanimadatexto").innerHTML=filtered_date_pred.map(row => row.Pago)+"%";

          impstr="width: "+filtered_date_pred.map(row => row.Impago)+"%"
          var ven = document.getElementById("carteravencidaanimada");  
          if (ven.hasAttribute("style")) {       
            ven.setAttribute("style", impstr);
          }
          
          document.getElementById("carteravencidaanimadatexto").innerHTML=filtered_date_pred.map(row => row.Impago)+"%";
          

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

        document.getElementById("carteratextototal").innerHTML = estado+", del sector "+sector;
        document.getElementById("carteratextovigente").innerHTML = estado+", del sector "+sector;
        document.getElementById("carteratextvencida").innerHTML = estado+", del sector "+sector;
        
        
    }

  
    
