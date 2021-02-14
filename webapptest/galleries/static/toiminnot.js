var index = 0;
imageSlider();

function imageSlider() {
    var i;
    var images = document.querySelectorAll(".image");
    for (i = 0; i < images.length; i++) {
        images[i].style.display = "none";
    }

    images[index].style.display = "block";
    if (index >= images.length - 1) {
        index = 0;
    } else {
        index++;
    }
    setTimeout(imageSlider, 5000);
}