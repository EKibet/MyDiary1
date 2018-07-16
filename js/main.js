jQuery(document).ready(function($) {
 $('.form').find('input, textarea').on('keyup blur focus', function(e) {

  var $this = $(this),
   label = $this.prev('label');

  if (e.type === 'keyup') {
   if ($this.val() === '') {
    label.removeClass('active highlight');
   } else {
    label.addClass('active highlight');
   }
  } else if (e.type === 'blur') {
   if ($this.val() === '') {
    label.removeClass('active highlight');
   } else {
    label.removeClass('highlight');
   }
  } else if (e.type === 'focus') {

   if ($this.val() === '') {
    label.removeClass('highlight');
   } else if ($this.val() !== '') {
    label.addClass('highlight');
   }
  }

 });

 $('.tab a').on('click', function(e) {

  e.preventDefault();

  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');

  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();

  $(target).fadeIn(600);

 });
 var contentModal = $('.content-modal');
$( "#view" ).on( "click", function(e) {
 e.preventDefault();
 $( contentModal ).toggleClass('content-modal-show');
});
$( ".overlay" ).on( "click", function() {
 $( contentModal ).toggleClass('content-modal-show');
});
$( ".content-modal_close" ).on( "click", function() {
 $( contentModal ).toggleClass('content-modal-show');
});
$(".mobile-close").on("click", function(){
 $( contentModal ).toggleClass('content-modal-show');
});

});
