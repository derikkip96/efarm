var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {

        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";

        }
    });
}


    $(document).ready(function(){
     $('button').click(function(){
        $(this).find('span').toggleClass('glyphicon-menu-up').toggleClass('glyphicon-menu-down');
     });
    });
//    function to close one accordion while openin another
$(function() {
  $('.accordion').on('click', function() {

    var x = $('.accordion').hasClass('active');
    if (x) {
      $('.active').removeClass('active');
      $('div').removeClass('show');
      $(this).toggleClass('active');
      $(this).next().toggleClass('show');
    } else {
      console.log("x");
      $(this).toggleClass('active');
      $(this).next().toggleClass('show');
    }
  });
});

