$(function() {  // When document loads

  // When the element with id "click" is clicked
  $("#click").on("click",function(e) {

    // Cancel the default link action
    e.preventDefault();

    // Make a POST request
    $.post(
      this.href,  // Send it to this url (the href of anchor)

      // Do this function when the post was successful
      function (data) {
        $("#num-clicks").text(data);  // Update the number of clicks
        changeImage();
      }
    );
  });
});

function changeImage() {
  const randomDegs = Math.floor(Math.random() * 300) + 30;  // Random number between 30 and 330
  $("img").css("filter", "hue-rotate(" + randomDegs + "deg) saturate(300%)");  // Change hue and saturation of img
  setTimeout(() => $("img").css("filter", "none"), 300);  // Change it back after 300ms
}