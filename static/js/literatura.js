function openModal(pdfUrl) {
  const modal = document.getElementById('pdfModal');
  const iframe = document.getElementById('pdfFrame');
  iframe.src = pdfUrl + "?autoplay=0";
  modal.style.display = 'block';
}

function closeModal() {
  const modal = document.getElementById('pdfModal');
  const iframe = document.getElementById('pdfFrame');
  iframe.src = "";
  modal.style.display = 'none';
}

// Fecha o modal ao clicar fora do conteúdo
window.onclick = function(event) {
  const modal = document.getElementById('pdfModal');
  if (event.target == modal) {
    closeModal();
  }
}
