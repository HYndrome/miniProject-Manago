const reviewLikeForm = document.querySelector('#review-like-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
reviewLikeForm.addEventListener('submit', function (event) {
  event.preventDefault()
  const restaurantId = event.target.dataset.restaurantId
  const reviewId = event.target.dataset.reviewId
  axios({
    method: 'post',
    url: `/reviews/${restaurantId}/${reviewId}/likes/`,
    headers: {'X-CSRFToken': csrftoken},
  })
  .then((response) => {
    const isLiked = response.data.is_liked
    const reviewLikeBtnIcon = document.querySelector('#review-like-form > button[type=submit] > i')
    
    if (isLiked === true) {
      reviewLikeBtnIcon.classList.remove('bi-heart')
      reviewLikeBtnIcon.classList.add('bi-heart-fill')
    } else {
      reviewLikeBtnIcon.classList.remove('bi-heart-fill')
      reviewLikeBtnIcon.classList.add('bi-heart')
    }
    
    const reviewLikeCountTag = document.querySelector('#review-like-count')
    const reviewLikeCountData = response.data.review_like_count
    reviewLikeCountTag.textContent = reviewLikeCountData
  })
  .catch((error) => {
    console.log(error.response)
  })
})