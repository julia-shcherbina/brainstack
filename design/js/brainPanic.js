$(function(){
  
  // SHOW/HIDE POPUP
  (function() {
    var popup = $('.js-popup-task-add'),
        showPopup = $('.js-task-add'),
        close = popup.find('.popup-close');
        console.log(popup);
        
    showPopup.click('live', function(e) {
      popup.hide();       
      popup.fadeIn('slow');
      e.preventDefault();    
    });

    close.click('live', function(e) {
      popup.hide();   
      e.preventDefault();    
    });
  })();
  
});