"use strict";

$(document).ready(function rdy() {

  var clrarr = [
  "#1abc9c", //turq
  "#3498db", //blue
  "#27ae60", //green
  "#e74c3c", //red
  "#9b59b6", //purple
];

  var clr = clrarr[Math.floor(Math.random() * clrarr.length)];

  var reclr = [$(".article-title"), $(".fab"), $(".post-icon"), $(".pro-overlay-btn"), $(".meta"), $(".article-title h1"), $(".list-title p")].forEach(function (item) {
    item.css("background-color", clr);
  });

  $(".catsw").click(function () {

    var am = $(".amenu-sub");
    var ami = $(".catsw i");

    if (am.css("display") == "flex") {
      am.hide();
      ami.css("transform", "rotate(0deg)");
    } else {
      am.css("display", "flex");
      ami.css("transform", "rotate(90deg)");
    }
  });

  $('.fab').on('click', function () {
    setTimeout(function () {
      $('aside').fadeIn().css('display', 'flex');
    }, 250);
  });

  $('article').not('.fab').on('click', function () {
    if ($('aside').css('display') == 'flex') {
      setTimeout(function () {
        if (window.innerWidth <= 800) {
          console.log("under");
          $('aside').fadeOut(function () {
            $('aside').hide();
          });
        }
      }, 250);
    }
  });

  //project section

  $('.prosqr').on('click', function () {
    setTimeout(function () {

      var ovr = $(window.location.hash);

      $(".pro-overlay-img").attr("src", ovr.data('img'));
      $(".pro-overlay-title").text(ovr.data('title'));
      $(".pro-overlay-desc").text(ovr.data('desc'));
      if (ovr.data('link') != "") {
        $(".pro-overlay-btn-link").attr("href", ovr.data('link'));$(".pro-overlay-btn-link").show();
      } else {
        $(".pro-overlay-btn-link").hide();
      }

      if (ovr.data('art') != "") {
        $(".pro-overlay-btn-more").attr("href", ovr.data('art'));$(".pro-overlay-btn-more").show();
      } else {
        $(".pro-overlay-btn-more").hide();
      }

      $('.pro-overlay').show(0);
    }, 25);
  });

  $('.pro-overlay-x').on('click', function () {
    $('.pro-overlay').hide();
  });

  $('.pro-overlay').click(function (e) {
    if (e.target.id != 'prover' && !$('#prover').find(e.target).length) {
      $(".pro-overlay").hide();
    }
  });
}); //end onload
