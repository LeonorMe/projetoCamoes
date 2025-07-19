function playVideo(el) {
  let videoUrl = el.getAttribute('data-video');

  // Adiciona autoplay na URL
  if (videoUrl.includes('?')) {
    videoUrl += '&autoplay=1';
  } else {
    videoUrl += '?autoplay=1';
  }

  // Seleciona modal e iframe
  const modal = document.getElementById('video-modal');
  const iframe = modal.querySelector('iframe');

  // Atualiza o src do iframe
  iframe.src = videoUrl;

  // Mostra o modal
  modal.style.display = 'flex';
}

document.getElementById('close-modal').addEventListener('click', () => {
  const modal = document.getElementById('video-modal');
  const iframe = modal.querySelector('iframe');
  
  // Esconde modal
  modal.style.display = 'none';

  // Para o vídeo removendo o src do iframe (para parar o autoplay)
  iframe.src = '';
});