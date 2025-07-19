//const lqip = require('lqip');
//const { count } = require("console");
//const { read } = require("fs");

const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("img-input");
const imageView = document.getElementById("img-view");
const uploadedImage = document.getElementById("uploaded-img");

const canvas = document.createElement("canvas");
const ctx = canvas.getContext("2d");
const xMin=0, xMax=255;
const yMin=0, yMax=255;
const zMin=0, zMax=255;

inputFile.addEventListener("change", uploadImage);

function uploadImage(){
    console.log("Uploading...");
    let file = inputFile.files[0]
    console.log("File: ", file);
    let imgLink = URL.createObjectURL(file);
    console.log(imgLink);

    imageView.textContent = "";
    imageView.style.padding = 0;

    //imageView.style.backgroundImage = `url(${imgLink})`;
    dropArea.style.backgroundImage = `url(${imgLink})`;

    //uploadedImage.src = imgLink;
}

dropArea.addEventListener("dragover", function(e){
    e.preventDefault();
});

dropArea.addEventListener("drop", function (e) {
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
    uploadImage();
});
