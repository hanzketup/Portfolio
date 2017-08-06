
window.onload = function(){
let arr = [
"#f1c40f", //yellow
"#1abc9c", //turq
"#3498db", //blue
"#27ae60", //green
"#e74c3c", //red
"#9b59b6" //purple
];
let clr = arr[Math.floor(Math.random() * arr.length)];
$(".article-title").css("background-color", clr);
$(".fab").css("background-color", clr);

$( ".catsw" ).click(function() {

  let am = $(".amenu-sub");
  let ami = $(".catsw i");

  if(am.css("display") == "flex"){
    am.hide();
    ami.css("transform","rotate(0deg)")
  }
  else{
    am.css("display","flex");
    ami.css("transform","rotate(90deg)")
  }


});


}
