// galeria.js

document.addEventListener("DOMContentLoaded", () => {
  const dadosImagens = [/*
    { classe: "img1", texto: "Canto IX <br> Autor/a: Ana Freitas." },
    { classe: "img2", texto: "Autor(a): Ana Maria." },
    { classe: "img3", texto: "Autor(a): Catarina Pereira." },
    { classe: "img4", texto: "Caravela <br> Autor(a): Daniela Filipa Aleluia Lemos." },
    { classe: "img5", texto: "Autor(a): Francisca Leal." },
    { classe: "img6", texto: "Autor(a): Gil Pena Marques Piedade." },
    { classe: "img7", texto: "Autor(a): Tomás M." },
    { classe: "img8", texto: "Autor(a): Liliana Dias." },
    { classe: "img9", texto: "Autor(a): Marco Neves." },
    { classe: "img10", texto: "Autor(a): Margarida Ferreira." },
    { classe: "img11", texto: "Autor(a): Mingli Han." },
    { classe: "img12", texto: "Autor(a): Rodrigo Soares." },
    { classe: "img13", texto: "Autor(a): Teresa Guerreiro." },
    { classe: "img14", texto: "Autor(a): Tomas Carrasqueira Pinto." },
    { classe: "img15", texto: "Autor(a): Tomás M." },*/
  ]; 

  const galeria = document.getElementById("galeria");

  if (galeria) {
    dadosImagens.forEach(item => {
      galeria.innerHTML += `
        <div class="col-md-6 col-lg-4">
          <div class="flip-box">
            <div class="flip-box-inner">
              <div class="flip-box-front ${item.classe}"></div>
              <div class="flip-box-back">
                <p>${item.texto}</p>
              </div>
            </div>
          </div>
        </div>
      `;
    });
  }
});
