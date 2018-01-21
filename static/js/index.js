$(document).ready(function() {
  
  var windowHeight = $( window ).height();
  $("div.body-text").css({top: windowHeight});
  $("div.body-text").css({height: windowHeight});

  $("img.facebook").on('mouseover',function() {
    var halfWidth = $("img.facebook").width() * 0.6;
    var halfHeight = $("img.facebook").height() * 0.6;
    $(this)
      .animate({
        height: "120%", 
        width: "120%", 
        // left: -=halfWidth, 
        // top: -=halfHeight  
      }, 400)
  });

  $("img.facebook").on('mouseout',function() {
    $(this)
      .animate({
        height: "100%", 
        width: "100%",  
      }, 400)
  });

  $('p').on('click', function() {
      $(this).toggleClass('bold');
  });

});




