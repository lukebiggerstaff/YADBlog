var navMenuButton = document.querySelector('#navMenuButton');
var navMenuSlider = document.querySelector('#navMenuSlider');

var createClickEvent  = navMenuButton.addEventListener('click', function(){
  navMenuSlider.classList.toggle('onscreen');
});
