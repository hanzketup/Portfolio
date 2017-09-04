"use strict";

$(document).ready(function () {

  $(".cirfill").toArray().forEach(function (item) {
    var pattern = Trianglify({
      height: item.clientHeight,
      width: item.clientWidth + 600,
      variance: "0.95",
      x_colors: 'random'
    });
    item.style['background-image'] = 'url(' + pattern.png() + ')';
  });
});
