function upDate(previewPic){

    var image = document.getElementById("image");
    image.style.background = "url(" + previewPic.src + ") #8e68ff";
    image.innerHTML = previewPic.alt;


}

function unDo(){
    var image = document.getElementById("image");
    image.style.background = "#8e68ff";
    image.innerHTML = "Hover over an image below to display here.";
   
    
}