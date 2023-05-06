const card = document.querySelector('.card')

card.addEventListener('mouseenter', (e) => {
  const bgImg = document.querySelector('.bg-img')
  // console.log(bgImg);
  bgImg.style.transform = 'translate(-50%, -50%) scale(1)'
  bgImg.style.opacity = '0.5'
  bgImg.style.transition = 'all 0.5s'
})
card.addEventListener('mouseleave', (e) => {
  const bgImg = document.querySelector('.bg-img');
  bgImg.style.transform = 'translate(-50%, -50%) scale(1.15)';
  bgImg.style.opacity = '1'
  bgImg.style.transition = 'all 0.5s';
})