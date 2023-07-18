
$(document).ready(function () {
  $('.item').on("click", function(){
    console.log("object");
    $('.item').removeClass("item-active")
    $(this).addClass('item-active')
  })
})

console.log("object");
