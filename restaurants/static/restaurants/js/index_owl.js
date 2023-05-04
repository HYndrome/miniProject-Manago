// owl carousel

$('.owl-carousel--category').owlCarousel({
  loop:true,
  margin:10,
  responsive:{
      0:{
          items:2
      },
      768:{
          items:4
      },
      1400:{
          items:6
      },
  }
})

$('.owl-carousel--region').owlCarousel({
  loop:false,
  margin:10,
  responsive:{
      0:{
          items:2
      },
      768:{
          items:4
      },
      1400:{
          items:6
      },
  }
})