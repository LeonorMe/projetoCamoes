//pRight = document.querySelector('.right');
//pLeft = document.querySelector('.left');

const coverAnim = document.getElementById("cover-anim");

console.log(coverAnim);

coverAnim.addEventListener('click', function()
{
    const book = document.querySelector(".book");

    var page = document.createElement("div");
    page.className = "page-turn";
    page.innerHTML = pRight.id - 2;
    book.appendChild(page);

    setTimeout(function() {
        page.innerHTML = pLeft.id;
    }, 500);
    
    setTimeout(function() {
        book.removeChild(page);
    }, 1000);
})

/*
pRight.addEventListener('click', function() {

    var nextId =
        parseInt(pRight.id) + 2 < texts.length
        ? parseInt(pRight.id) + 2
        : texts.length - 1;

    //console.log("nextId: " + nextId);

    
    pRight.id = nextId;
    pRight.innerHTML = texts[nextId];
    
    pRight.appendChild(addPageNumber(pRight.id));
    
    pageTurningAnimFront();
    
    pLeft.innerHTML = texts[nextId - 1];
    pLeft.id = nextId - 1;

    pLeft.appendChild(addPageNumber(pLeft.id));
});

pLeft.addEventListener('click', function() {
    var nextId =
        parseInt(pLeft.id) - 2 >= 0
        ? parseInt(pLeft.id) - 2
        : 0;

    //console.log("nextId: " + nextId);
    
    pLeft.id = nextId;
    pLeft.innerHTML = texts[nextId];
    
    pLeft.appendChild(addPageNumber(pLeft.id));

    pageTurningAnimBack();

    pRight.innerHTML = texts[nextId + 1];
    pRight.id = nextId + 1;
    
    pRight.appendChild(addPageNumber(pRight.id));
});


function pageTurningAnimFront(){
    const book = document.querySelector(".book");

    var page = document.createElement("div");
    page.className = "page-turn";
    page.innerHTML = pRight.id - 2;
    book.appendChild(page);

    setTimeout(function() {
        page.innerHTML = pLeft.id;
    }, 500);
    
    setTimeout(function() {
        book.removeChild(page);
    }, 1000);
}


function pageTurningAnimBack(){
    const book = document.querySelector(".book");

    var page = document.createElement("div");
    page.className = "page-turn-back";
    page.innerHTML = pLeft.id + 2; // TODO: bug in page numeration - 02 instead of 2
    book.appendChild(page);

    setTimeout(function() {
        page.innerHTML = pRight.id;
    }, 500);
    
    setTimeout(function() {
        book.removeChild(page);
    }, 1000);
}

*/