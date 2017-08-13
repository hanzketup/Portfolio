$(document).ready(function() {

  var clrarr = [
    "#f1c40f", //yellow
    "#1abc9c", //turq
    "#3498db", //blue
    "#27ae60", //green
    "#e74c3c", //red
    "#9b59b6", //purple
    "#795548", //brown
  ];


  $(".cirfill").toArray().forEach(function(item) {
    let clr = clrarr[Math.floor(Math.random() * clrarr.length)];
    $(item).css('background-color', clr);
  });
});
