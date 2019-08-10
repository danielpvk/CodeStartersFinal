
$(document).ready(function() {
  AOS.init( { //AOS is the animation for the scrolling
 
  });
});

//scroll for links
$('a.smooth-scroll')
.click(function(event) {
 
  if (
    location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
    && 
    location.hostname == this.hostname
  ) {
    var target = $(this.hash);
    target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
   
    if (target.length) {
 
      event.preventDefault();
      $('html, body').animate({
        scrollTop: target.offset().top
      }, 1000, function() {

        var $target = $(target);
        $target.focus();
        if ($target.is(":focus")) { 
          return false;
        } else {
          $target.attr('tabindex','-1'); 
          $target.focus(); 
        };
      });
    }
  }
});


function getData_estados(estado){
  console.log("selector de estados");
}

function getData(estado){
  console.log("selector de estados");
}


function prepareEstado(estado){
    switch(estado){
      case "Baja California Norte":x="BajaCaliforniaNorte"; break;
      case "Baja California Sur":x="BajaCaliforniaSur"; break;
      case "Ciudad de Mexico": x="CiudaddeMexico"; break;
      case "Estado de Mexico": x="EstadodeMexico"; break;
      case "Nuevo Leon": x="NuevoLeon"; break;
      case "Quintana Roo": x="QuintanaRoo"; break;
      case "San Luis Potosi": x="SanLuisPotosi"; break;
      default: x=estado;
    }
    
    return (x);
}
$("#actionButton").on('click',function(event){
  var e = document.getElementById("selDataset");
  var estado = prepareEstado(e.options[e.selectedIndex].text);
  var s = document.getElementById("selDataset2");
  var sector = s.options[s.selectedIndex].text;
  console.log(estado,sector);

  myChart(estado,sector);
});