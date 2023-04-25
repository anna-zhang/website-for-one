const slides = document.querySelectorAll('.slide')
const arrowLeft = document.querySelector('.arrow-left')
const arrowRight = document.querySelector('.arrow-right')

// Set the default slide to the middle slide
var currentSlide = parseInt(
  document.getElementById('slideshow').getAttribute('startingSlide')
)

// Move to the next slide when the right arrow is clicked
arrowRight.addEventListener('click', () => {
  if (currentSlide < slides.length - 1) {
    currentSlide++
  } else {
    currentSlide = 0
  }
  moveSlides()
})

// Move to the previous slide when the left arrow is clicked
arrowLeft.addEventListener('click', () => {
  if (currentSlide > 0) {
    currentSlide--
  } else {
    currentSlide = slides.length - 1
  }
  moveSlides()
})

// Move the slides to the appropriate position based on the current slide
function moveSlides () {
  slides.forEach((slide, index) => {
    slide.style.transform = `translateX(-${currentSlide * 100}vw)`
    var link = slide.querySelector('a')
    if (link != null) {
      if (index == currentSlide) {
        link.setAttribute('tabIndex', 0)
      } else {
        link.setAttribute('tabIndex', -1)
      }
    }
  })
}
