$(document).ready(function() {
  $("img").click(function() {

    if(window.innerWidth > 400){
    $(this).data('link');

    $('.pho-overlay-img').attr('src', $(this).data('link'));
    $(".pho-overlay").show();

  }});

  $('.pho-overlay').click(function(e) {
    if (e.target.id != 'phower' && !$('#phower').find(e.target).length) {
      $(".pho-overlay").hide();
      $('.pho-overlay-img').attr('src', '');
    }
  });
});
